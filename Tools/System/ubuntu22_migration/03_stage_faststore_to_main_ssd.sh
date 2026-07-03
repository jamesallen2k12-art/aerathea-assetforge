#!/usr/bin/env bash
set -euo pipefail

DEST="${1:-/home/Flamestrike/FastStore_Staging}"
LOG_DIR="${DEST}/_migration_logs"

if [[ ! -d /faststore ]]; then
  echo "/faststore is not mounted; refusing to stage." >&2
  exit 1
fi

mkdir -p "${LOG_DIR}"

echo "Staging /faststore to ${DEST}"
echo "This is non-destructive and does not remove anything from /faststore."

rsync \
  -aHAX \
  --numeric-ids \
  --human-readable \
  --info=stats2 \
  --protect-args \
  /faststore/ "${DEST}/" | tee "${LOG_DIR}/faststore_stage.log"

find "${DEST}" -xdev -type f -printf '%P\t%s\n' | sort >"${LOG_DIR}/file_manifest.tsv"
du -sh "${DEST}" >"${LOG_DIR}/stage_size.txt"

echo "FastStore staged to ${DEST}"
echo "Manifest: ${LOG_DIR}/file_manifest.tsv"
