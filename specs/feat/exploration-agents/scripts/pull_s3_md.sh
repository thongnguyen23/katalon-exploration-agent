#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: pull_s3_md.sh s3://bucket/prefix [out_dir] [--flatten]

Copies only Markdown files (*.md) from an S3 prefix to a local directory,
preserving folder structure. Requires AWS CLI configured with credentials.

Args:
  s3://bucket/prefix   S3 prefix to sync from (also accepts bucket ARN: arn:aws:s3:::bucket[/prefix])
  out_dir              Local directory to write files (default: in)
  --flatten            Write all *.md into the out_dir root (no subfolders). Collisions are avoided by encoding path separators as dashes.

Env (optional):
  AWS_PROFILE          AWS CLI profile to use
  AWS_REGION           Region override if needed

Examples:
  ./pull_s3_md.sh s3://my-bucket/docs in
  AWS_PROFILE=prod ./pull_s3_md.sh s3://my-bucket/product-docs ./in
USAGE
}

if [ ${1:-} = "-h" ] || [ ${1:-} = "--help" ]; then
  usage; exit 0
fi

if [ $# -lt 1 ]; then
  usage; exit 1
fi

ARG1="$1"
case "$ARG1" in
  arn:aws:s3:::*)
    # convert ARN to s3:// URL
    TMP=${ARG1#arn:aws:s3:::}
    BUCKET=${TMP%%:*}
    REST=${TMP#${BUCKET}}
    if [ "$REST" = "$TMP" ]; then REST=""; fi
    REST=${REST#:}
    S3_PREFIX="s3://${BUCKET}/${REST}"
    ;;
  *)
    S3_PREFIX="$ARG1"
    ;;
esac
OUT_DIR="${2:-in}"
FLATTEN=0
if [ "${3:-}" = "--flatten" ] || [ "${2:-}" = "--flatten" ]; then
  FLATTEN=1
  # if --flatten used as second arg, reset OUT_DIR to default
  if [ "${2:-}" = "--flatten" ]; then OUT_DIR="in"; fi
fi

command -v aws >/dev/null 2>&1 || { echo "aws CLI not found. Install AWS CLI v2." >&2; exit 2; }

mkdir -p "$OUT_DIR"

# Load env from .env.defaults and .env if present (to pick up AWS_* vars)
if [ -f .env.defaults ]; then set -a; . .env.defaults; set +a; fi
if [ -f .env ]; then set -a; . .env; set +a; fi

echo "Syncing Markdown from $S3_PREFIX -> $OUT_DIR"
set -x
# If you know the bucket is public and listable anonymously, add --no-sign-request
# by exporting S3_NO_SIGN=1
EXTRA_FLAG=""
if [ "${S3_NO_SIGN:-}" = "1" ]; then EXTRA_FLAG="--no-sign-request"; fi

if [ "$FLATTEN" = "0" ]; then
  aws s3 sync "$S3_PREFIX" "$OUT_DIR" --exclude "*" --include "*.md" --no-progress $EXTRA_FLAG
else
  TMPDIR=$(mktemp -d)
  aws s3 sync "$S3_PREFIX" "$TMPDIR" --exclude "*" --include "*.md" --no-progress $EXTRA_FLAG
  while IFS= read -r -d '' f; do
    rel="${f#${TMPDIR}/}"
    flat_name=$(echo "$rel" | tr '/' '-')
    cp -f "$f" "$OUT_DIR/$flat_name"
  done < <(find "$TMPDIR" -type f -name "*.md" -print0)
  rm -rf "$TMPDIR"
fi
set +x

COUNT=$(find "$OUT_DIR" -type f -name "*.md" | wc -l | tr -d ' ')
echo "Downloaded Markdown files: $COUNT"
echo "Sample files:"
find "$OUT_DIR" -type f -name "*.md" | head -n 10

echo "Done."
