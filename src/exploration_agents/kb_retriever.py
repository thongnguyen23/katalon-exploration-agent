"""KB Retriever

Thin wrapper around AWS Bedrock Agent Runtime `retrieve` API for Knowledge Bases.
Also resolves S3 citations to presigned URLs for client consumption.
"""

from __future__ import annotations

import os
import time
from typing import Any, Dict, List, Tuple

import boto3
from botocore.client import Config

from shared import get_env, load_config


def _bedrock_client():
    region = get_env("AWS_REGION", "us-east-1")
    return boto3.client("bedrock-agent-runtime", region_name=region)


def _s3_client():
    region = get_env("AWS_REGION", "us-east-1")
    # signature version v4
    return boto3.client("s3", region_name=region, config=Config(signature_version="s3v4"))


def _presign_s3_uri(uri: str, expires_in: int = 3600) -> str:
    if not uri.startswith("s3://"):
        return uri
    _, _, rest = uri.partition("s3://")
    bucket, _, key = rest.partition("/")
    if not bucket or not key:
        return uri
    s3 = _s3_client()
    return s3.generate_presigned_url(
        ClientMethod="get_object",
        Params={"Bucket": bucket, "Key": key},
        ExpiresIn=expires_in,
    )


def kb_search(query: str, top_k: int | None = None) -> Tuple[List[Dict[str, Any]], int]:
    """Retrieve relevant passages from Bedrock KB.

    Returns a tuple (hits, tta_ms). Each hit mirrors Bedrock's retrieval result
    with an extra field `presigned_url` for citations.
    """
    load_config()
    # Accept both KB_ID and KNOWLEDGE_BASE_ID for convenience
    kb_id = os.getenv("KB_ID") or os.getenv("KNOWLEDGE_BASE_ID")
    if not kb_id:
        kb_id = get_env("KB_ID")
    top_k = top_k or int(get_env("RETRIEVAL_TOPK", "8"))

    client = _bedrock_client()

    req = {
        "knowledgeBaseId": kb_id,
        "retrievalQuery": {"text": query},
        "retrievalConfiguration": {
            "vectorSearchConfiguration": {"numberOfResults": top_k}
        },
    }

    t0 = time.perf_counter()
    resp = client.retrieve(**req)
    tta_ms = int((time.perf_counter() - t0) * 1000)

    results: List[Dict[str, Any]] = []
    for item in resp.get("retrievalResults", []):
        loc = item.get("location", {}).get("s3Location", {})
        uri = loc.get("uri")
        presigned = _presign_s3_uri(uri) if uri else None
        enriched = dict(item)
        enriched["presigned_url"] = presigned
        results.append(enriched)

    return results, tta_ms
