"""Graph Builder

Parses Markdown files (local directory or S3 prefix) to build a lightweight
neighbors graph capturing relationships between sections:
- next/prev among sibling headings
- parent between child and its parent heading
- see_also for intra-doc anchor links

Outputs JSONL at `artifacts/neighbors.jsonl` (configurable via env).
"""

from __future__ import annotations

import io
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator, List, Optional, Tuple


from shared import get_env, load_config


HEADING_RE = re.compile(r"^(?P<hashes>#{1,6})\s+(?P<title>.+?)\s*$")
INTRA_LINK_RE = re.compile(r"\[[^\]]+\]\((?P<href>#[^)]+)\)")


@dataclass
class Section:
    level: int
    title: str
    anchor: str
    section_id: str


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def join_section_id(doc_id: str, anchor_slug: Optional[str]) -> str:
    if not anchor_slug:
        return doc_id
    # Prefer dotted style for sections: doc.section (convert '-' to '.')
    dotted = anchor_slug.replace("-", ".")
    # Avoid accidental double dots
    dotted = re.sub(r"\.\.+", ".", dotted)
    return f"{doc_id}.{dotted}"


def path_to_doc_id(root: str, path: str) -> str:
    rel = os.path.relpath(path, root)
    rel = rel.replace("\\", "/")
    if rel.endswith(".md"):
        rel = rel[:-3]
    parts = [p for p in rel.split("/") if p and p != "."]
    return ".".join(parts)


def parse_markdown_sections(doc_id: str, content: str) -> Tuple[List[Section], List[Tuple[str, str]]]:
    """Parse headings and intra-doc links.

    Returns:
        sections: ordered list of Section objects
        see_also_edges: list of (src_section_id, dst_section_id)
    """
    sections: List[Section] = []
    stack: List[Section] = []
    see_also_edges: List[Tuple[str, str]] = []

    current_section: Optional[Section] = None
    for line in content.splitlines():
        m = HEADING_RE.match(line)
        if m:
            level = len(m.group("hashes"))
            title = m.group("title").strip()
            anchor = slugify(title)
            section_id = join_section_id(doc_id, anchor)
            sec = Section(level=level, title=title, anchor=anchor, section_id=section_id)

            # Maintain a stack of headings by level
            while stack and stack[-1].level >= level:
                stack.pop()
            stack.append(sec)

            sections.append(sec)
            current_section = sec
            continue

        # Within a section, capture intra-doc links to anchors
        if current_section:
            for lm in INTRA_LINK_RE.finditer(line):
                href = lm.group("href")  # like '#create-token'
                if href.startswith("#"):
                    dst_anchor = href[1:]
                    dst_section_id = join_section_id(doc_id, dst_anchor)
                    see_also_edges.append((current_section.section_id, dst_section_id))

    return sections, see_also_edges


def build_edges_for_sections(sections: List[Section]) -> List[dict]:
    edges: List[dict] = []
    # next/prev among siblings of same level
    by_level: dict[int, List[Section]] = {}
    for s in sections:
        by_level.setdefault(s.level, []).append(s)

    for level, siblings in by_level.items():
        for i in range(len(siblings) - 1):
            a, b = siblings[i], siblings[i + 1]
            edges.append({"src": a.section_id, "dst": b.section_id, "rel": "next", "w": 1.0})
            edges.append({"src": b.section_id, "dst": a.section_id, "rel": "prev", "w": 1.0})

    # parent relationships: any heading followed by deeper level belongs to last shallower
    parent_stack: List[Section] = []
    for s in sections:
        while parent_stack and parent_stack[-1].level >= s.level:
            parent_stack.pop()
        if parent_stack:
            parent = parent_stack[-1]
            edges.append({"src": s.section_id, "dst": parent.section_id, "rel": "parent", "w": 1.0})
        parent_stack.append(s)

    return edges


def iter_local_markdown(root_dir: str) -> Iterator[Tuple[str, str]]:
    for path in Path(root_dir).rglob("*.md"):
        if path.is_file():
            yield str(path), path.read_text(encoding="utf-8", errors="ignore")


def iter_s3_markdown(s3_prefix: str, s3_client=None) -> Iterator[Tuple[str, str]]:
    # Lazy import to avoid requiring boto3 when only using local files
    import boto3  # type: ignore
    if s3_client is None:
        s3_client = boto3.client("s3", region_name=get_env("AWS_REGION", "us-east-1"))
    assert s3_prefix.startswith("s3://"), "S3 prefix must start with s3://"
    _, _, rest = s3_prefix.partition("s3://")
    bucket, _, prefix = rest.partition("/")
    continuation_token = None
    while True:
        kwargs = {"Bucket": bucket, "Prefix": prefix}
        if continuation_token:
            kwargs["ContinuationToken"] = continuation_token
        resp = s3_client.list_objects_v2(**kwargs)
        for obj in resp.get("Contents", []):
            key = obj["Key"]
            if not key.endswith(".md"):
                continue
            body = s3_client.get_object(Bucket=bucket, Key=key)["Body"].read()
            try:
                text = body.decode("utf-8")
            except Exception:
                text = body.decode("utf-8", errors="ignore")
            yield f"s3://{bucket}/{key}", text
        if resp.get("IsTruncated"):
            continuation_token = resp.get("NextContinuationToken")
        else:
            break


def build_graph(input_path: str, output_file: Optional[str] = None) -> str:
    """Build neighbors graph from Markdown under `input_path`.

    Args:
        input_path: Local directory or S3 prefix (s3://bucket/prefix)
        output_file: Where to write JSONL (defaults to env GRAPH_FILE)

    Returns:
        Path to written JSONL
    """
    load_config()
    output_file = output_file or get_env("GRAPH_FILE", "artifacts/neighbors.jsonl")
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    edges_out: List[dict] = []

    if input_path.startswith("s3://"):
        iterator = iter_s3_markdown(input_path)
        doc_root = input_path  # only used for doc id derivation below
    else:
        iterator = iter_local_markdown(input_path)
        doc_root = input_path

    for path, text in iterator:
        # Determine doc_id from path relative to the provided root
        if path.startswith("s3://"):
            # For S3, compute relative to prefix component
            # Convert s3://bucket/prefix/foo/bar.md -> doc_id prefix/foo/bar
            _, _, rest = doc_root.partition("s3://")
            bucket_root, _, prefix_root = rest.partition("/")
            rel_doc_path = path.split(f"s3://{bucket_root}/", 1)[-1]
            if rel_doc_path.startswith(prefix_root):
                rel_doc_path = rel_doc_path[len(prefix_root) :].lstrip("/")
            doc_id = ".".join([p for p in rel_doc_path.replace("\\", "/").split("/") if p]).removesuffix(".md")
        else:
            doc_id = path_to_doc_id(doc_root, path)

        sections, see_also = parse_markdown_sections(doc_id, text)
        edges_out.extend(build_edges_for_sections(sections))
        for src, dst in see_also:
            edges_out.append({"src": src, "dst": dst, "rel": "see_also", "w": 0.8})

    # Deduplicate edges
    seen = set()
    unique_edges = []
    for e in edges_out:
        key = (e["src"], e["dst"], e["rel"])  # ignore w for uniqueness
        if key not in seen:
            seen.add(key)
            unique_edges.append(e)

    with io.open(output_file, "w", encoding="utf-8") as f:
        for e in unique_edges:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")

    return output_file


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Build neighbors graph from Markdown.")
    parser.add_argument("input", help="Local directory or s3://bucket/prefix")
    parser.add_argument("--out", dest="out", default=None, help="Output JSONL path")
    args = parser.parse_args()
    out = build_graph(args.input, args.out)
    print(out)
