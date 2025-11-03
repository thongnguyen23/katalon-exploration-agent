"""Env-only entry point for the ontology-based graph build.

Configuration source: process environment (e.g., exported via your .venv activation).
No CLI arguments are accepted. This module can be invoked from a root-level
runner script that ensures `src/` is on `sys.path`.

Env vars (with defaults shown):
- AWS_REGION (us-east-1)
- DOCS_S3 or EA_S3 (required if SYNC_TO_LOCAL=true)
- ARTIFACTS_DIR (artifacts)
- DOCS_DIR (${ARTIFACTS_DIR}/docs)
- ONTOLOGY_FILE (configs/ontology.yaml)
- RUNS_DIR (${ARTIFACTS_DIR}/runs)
- RUN_ID (timestamp if unset)
- ENTITIES_FILE (${RUNS_DIR}/${RUN_ID}/entities.jsonl)
- EDGES_FILE (${RUNS_DIR}/${RUN_ID}/edges.jsonl)
- NEIGHBORS_FILE (${RUNS_DIR}/${RUN_ID}/neighbors.jsonl)
- GRAPH_FILE (set to this run's neighbors.jsonl after build if unset)
- ENABLE_LLM_ENTITY (false)
- LLM_PROVIDER (openai)
- LLM_MODEL (gpt-4o-mini)
- FANOUT_CAP (optional int)
- MMR_LAMBDA (optional float)
- SYNC_TO_LOCAL (true)
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
import hashlib
import json
from typing import Optional

from shared import get_env_bool
from exploration_agents.ontology_graph_builder import build_graph


def _s3_sync_md(s3_prefix: str, out_dir: str, region: Optional[str]) -> int:
    """Sync only *.md files from S3 prefix to a local folder using boto3.

    Returns number of files written.
    """
    import boto3  # lazy import

    # Accept arn:aws:s3:::bucket[/prefix] or s3://bucket/prefix
    if s3_prefix.startswith("arn:aws:s3:::"):
        tmp = s3_prefix[len("arn:aws:s3:::") :]
        if ":" in tmp:
            bucket, _, prefix = tmp.partition(":")
        else:
            if "/" in tmp:
                bucket, _, prefix = tmp.partition("/")
            else:
                bucket, prefix = tmp, ""
    else:
        assert s3_prefix.startswith("s3://"), "S3 prefix must start with s3:// or be an S3 ARN"
        _, _, rest = s3_prefix.partition("s3://")
        bucket, _, prefix = rest.partition("/")

    s3 = boto3.client("s3", region_name=region or os.getenv("AWS_REGION", "us-east-1"))
    cont: Optional[str] = None
    written = 0
    while True:
        kwargs = {"Bucket": bucket, "Prefix": prefix}
        if cont:
            kwargs["ContinuationToken"] = cont
        resp = s3.list_objects_v2(**kwargs)
        for obj in resp.get("Contents", []):
            key = obj["Key"]
            if not key.endswith(".md"):
                continue
            rel = key[len(prefix) :].lstrip("/") if prefix else key
            dest = Path(out_dir) / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            body = s3.get_object(Bucket=bucket, Key=key)["Body"].read()
            try:
                text = body.decode("utf-8")
            except Exception:
                text = body.decode("utf-8", errors="ignore")
            dest.write_text(text, encoding="utf-8")
            written += 1
        if resp.get("IsTruncated"):
            cont = resp.get("NextContinuationToken")
        else:
            break
    return written


def main() -> None:
    # Configuration must come from the environment (.venv). Do not parse CLI args.
    artifacts_dir = os.getenv("ARTIFACTS_DIR", "artifacts")
    # Single shared input folder reused across runs
    docs_dir = os.getenv("DOCS_DIR") or os.getenv("DOCS_OUT") or str(Path(artifacts_dir) / "docs")
    ontology_file = os.getenv("ONTOLOGY_FILE", str(Path("configs") / "ontology.yaml"))

    # Per-run outputs under artifacts/runs/<run_id>
    runs_root = os.getenv("RUNS_DIR", str(Path(artifacts_dir) / "runs"))
    run_id = os.getenv("RUN_ID")
    if not run_id:
        from datetime import datetime
        run_id = datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir = str(Path(runs_root) / run_id)
    Path(run_dir).mkdir(parents=True, exist_ok=True)

    entities_file = os.getenv("ENTITIES_FILE", str(Path(run_dir) / "entities.jsonl"))
    edges_file = os.getenv("EDGES_FILE", str(Path(run_dir) / "edges.jsonl"))
    neighbors_file = os.getenv("NEIGHBORS_FILE", str(Path(run_dir) / "neighbors.jsonl"))

    # Do not set GRAPH_FILE yet; after build we set it to this run's neighbors

    fanout_cap = int(os.getenv("FANOUT_CAP")) if os.getenv("FANOUT_CAP") else None
    mmr_lambda = float(os.getenv("MMR_LAMBDA")) if os.getenv("MMR_LAMBDA") else None

    sync_to_local = get_env_bool("SYNC_TO_LOCAL", True)
    s3_src = os.getenv("DOCS_S3") or os.getenv("EA_S3")
    if sync_to_local:
            
        if not s3_src and not Path(docs_dir).exists():
            print("[builder] SYNC_TO_LOCAL=true but no DOCS_S3/EA_S3 configured and docs_out missing.", file=sys.stderr)
            sys.exit(2)
        if s3_src:
            print(f"[builder] Syncing Markdown from {s3_src} -> {docs_dir}")
            Path(docs_dir).mkdir(parents=True, exist_ok=True)
            written = _s3_sync_md(s3_src, docs_dir, os.getenv("AWS_REGION", "us-east-1"))
            print(f"[builder] Synced files: {written}")
        source_path = docs_dir
    else:
        source_path = s3_src or docs_dir

    print(f"[builder] Building graph from: {source_path}")
    Path(artifacts_dir).mkdir(parents=True, exist_ok=True)
    Path(runs_root).mkdir(parents=True, exist_ok=True)

    report = build_graph(
        source=source_path,
        ontology_path=ontology_file,
        emit_entities=entities_file,
        emit_edges=edges_file,
        emit_neighbors=neighbors_file,
        synonyms_json=os.getenv("SYNONYMS_JSON"),
        product_map_yaml=os.getenv("PRODUCT_MAP_YAML"),
        entity_whitelist=os.getenv("ENTITY_WHITELIST"),
        enable_llm_entity=get_env_bool("ENABLE_LLM_ENTITY", False),
        llm_provider=os.getenv("LLM_PROVIDER", "openai"),
        llm_model=os.getenv("LLM_MODEL", "gpt-4o-mini"),
        fanout_cap=fanout_cap,
        mmr_lambda=mmr_lambda,
    )

    # Set GRAPH_FILE to this run's neighbors if not provided
    if not os.getenv("GRAPH_FILE"):
        os.environ["GRAPH_FILE"] = neighbors_file

    # Remove any old symlinks if they exist (user requires no symlinks)
    # top-level compatibility files
    for name in ("entities.jsonl", "edges.jsonl", "neighbors.jsonl"):
        p = Path(artifacts_dir) / name
        try:
            if p.is_symlink():
                p.unlink()
        except Exception:
            pass
    # runs/latest symlink
    try:
        latest = Path(runs_root) / "latest"
        if latest.is_symlink():
            latest.unlink()
    except Exception:
        pass

    # Snapshot ontology and write manifest
    ont_snapshot = None
    try:
        src = Path(ontology_file)
        snap = Path(run_dir) / "ontology.yaml"
        snap.write_bytes(src.read_bytes())
        # hash + metadata
        data = snap.read_bytes()
        sha256 = hashlib.sha256(data).hexdigest()
        try:
            import yaml  # type: ignore
            meta = yaml.safe_load(data) or {}
        except Exception:
            meta = {}
        ver_v = meta.get("version")
        upd_v = meta.get("updated_at")
        ont_snapshot = {
            "path": str(src),
            "snapshot_path": str(snap),
            "sha256": sha256,
            "version": None if ver_v is None else str(ver_v),
            "updated_at": None if upd_v is None else str(upd_v),
        }
    except Exception:
        ont_snapshot = {"path": ontology_file, "error": "snapshot_failed"}

    manifest = {
        "run_id": run_id,
        "runs_root": runs_root,
        "run_dir": run_dir,
        "docs_dir": docs_dir,
        "s3_src": s3_src,
        "ontology": ont_snapshot,
        "report": report,
    }
    (Path(run_dir) / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    print("[builder] Done.")
    print({"run_id": run_id, "runs_root": runs_root, "report": report})


if __name__ == "__main__":
    main()
