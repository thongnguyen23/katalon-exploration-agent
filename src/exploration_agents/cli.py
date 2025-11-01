"""Exploration Agents CLI entry point (Python).

Runs the end-to-end flow: optional S3 pull → graph build → KB retrieval.
Logs to a file and prints a concise summary to stdout.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import os
import sys
import time
from pathlib import Path
from typing import Optional, Tuple

import boto3
from botocore.client import Config

from shared import load_config, get_env
from exploration_agents.graph_builder import build_graph
from exploration_agents.agent_runtime import retrieve_context


def _setup_logging(log_path: str) -> logging.Logger:
    logger = logging.getLogger("exploration_agents.cli")
    logger.setLevel(logging.INFO)
    fmt = logging.Formatter("%(asctime)s %(levelname)s [%(name)s] %(message)s")
    # File handler
    fh = logging.FileHandler(log_path, encoding="utf-8")
    fh.setFormatter(fmt)
    fh.setLevel(logging.INFO)
    # Console handler (concise)
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(fmt)
    ch.setLevel(logging.INFO)
    logger.handlers.clear()
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger


def _parse_s3(src: str) -> Tuple[str, str]:
    """Return (bucket, prefix) from s3:// or ARN forms.

    Accepts:
      - s3://bucket/prefix
      - arn:aws:s3:::bucket
      - arn:aws:s3:::bucket/prefix (convenience)
    """
    if src.startswith("s3://"):
        rest = src[5:]
        bucket, _, prefix = rest.partition("/")
        return bucket, prefix
    if src.startswith("arn:aws:s3:::"):
        rest = src[len("arn:aws:s3:::") :]
        if "/" in rest:
            bucket, _, prefix = rest.partition("/")
        else:
            bucket, prefix = rest, ""
        return bucket, prefix
    raise ValueError(f"Unsupported S3 source: {src}")


def _s3_client():
    region = os.getenv("AWS_REGION") or get_env("AWS_REGION", "us-east-1")
    return boto3.client("s3", region_name=region, config=Config(signature_version="s3v4"))


def _download_markdown(src: str, out_dir: str, flatten: bool, logger: logging.Logger) -> int:
    bucket, prefix = _parse_s3(src)
    s3 = _s3_client()
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    logger.info("[pull] bucket=%s prefix=%s out=%s flatten=%s", bucket, prefix, out_dir, flatten)

    token = None
    total = 0
    seen_flat: set[str] = set()
    while True:
        kwargs = {"Bucket": bucket, "Prefix": prefix}
        if token:
            kwargs["ContinuationToken"] = token
        resp = s3.list_objects_v2(**kwargs)
        for obj in resp.get("Contents", []):
            key = obj["Key"]
            if not key.lower().endswith(".md"):
                continue
            body = s3.get_object(Bucket=bucket, Key=key)["Body"].read()
            if flatten:
                flat = key.replace("/", "-")
                # avoid collisions: add short hash if needed
                if flat in seen_flat:
                    h = hashlib.sha1(key.encode()).hexdigest()[:8]
                    flat = f"{flat.rsplit('.',1)[0]}-{h}.md"
                seen_flat.add(flat)
                dest = out / flat
            else:
                dest = out / key
                dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(body)
            total += 1
            if total % 200 == 0:
                logger.info("[pull] downloaded %d markdown files...", total)
        if resp.get("IsTruncated"):
            token = resp.get("NextContinuationToken")
        else:
            break

    logger.info("[pull] done. markdown files: %d", total)
    return total


def main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Exploration Agents — full flow runner")
    p.add_argument("--s3", default="arn:aws:s3:::public-mcp-test", help="S3 source (s3://... or arn:aws:s3:::bucket[/prefix])")
    p.add_argument("--out", default="in", help="Local output directory for markdown")
    p.add_argument("--flatten", action="store_true", help="Place all .md in the out dir root")
    p.add_argument("--no-pull", action="store_true", help="Skip the S3 pull step")
    p.add_argument("--query", default="How do I generate steps with AI in Katalon?", help="Query text for retrieval")
    p.add_argument("--topk", type=int, default=int(os.getenv("RETRIEVAL_TOPK", "8")), help="KB retrieval top-k")
    p.add_argument("--graph-file", default=os.getenv("GRAPH_FILE", "artifacts/neighbors.jsonl"), help="Path to neighbors JSONL")
    p.add_argument("--log", default=None, help="Log file path (default under specs/.../logs)")
    args = p.parse_args(argv)

    # Load env for AWS + KB
    load_config()

    # Prepare logs
    log_dir = Path("specs/feat/exploration-agents/logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = args.log or str(log_dir / f"run-{time.strftime('%Y%m%d-%H%M%S')}.log")
    logger = _setup_logging(log_path)

    logger.info("[run] START s3=%s out=%s flatten=%s topk=%s graph=%s", args.s3, args.out, args.flatten, args.topk, args.graph_file)
    logger.info("[run] KB_ID=%s AWS_REGION=%s", os.getenv("KB_ID") or os.getenv("KNOWLEDGE_BASE_ID"), os.getenv("AWS_REGION"))

    # 1) Pull from S3
    if not args.no_pull:
        _download_markdown(args.s3, args.out, args.flatten, logger)
    else:
        logger.info("[pull] skipped (--no-pull)")

    # 2) Build graph
    Path(args.graph_file).parent.mkdir(parents=True, exist_ok=True)
    graph_path = build_graph(args.out, args.graph_file)
    edge_count = sum(1 for _ in open(graph_path, "r", encoding="utf-8")) if Path(graph_path).exists() else 0
    logger.info("[graph] wrote=%s edges=%d", graph_path, edge_count)

    # 3) Retrieve context
    os.environ["RETRIEVAL_TOPK"] = str(args.topk)
    resp = retrieve_context(args.query)
    resp_path = "artifacts/last_response.json"
    Path(resp_path).parent.mkdir(parents=True, exist_ok=True)
    with open(resp_path, "w", encoding="utf-8") as f:
        json.dump(resp, f, ensure_ascii=False, indent=2)
    logger.info("[retrieve] answer_preview=%s", (resp.get("answer") or "")[:200].replace("\n", " "))
    logger.info("[retrieve] citations=%d next_steps=%d tta_ms=%s", len(resp.get("citations", [])), len(resp.get("next_steps", [])), resp.get("tta_ms"))
    logger.info("[retrieve] wrote=%s", resp_path)

    logger.info("[run] DONE log=%s", log_path)
    print(f"Run completed. Log: {log_path}\nGraph: {graph_path}\nResponse: {resp_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

