#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
TARGET="$ROOT/SourceAssets/ArmorPaint/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01/SM_GIA_BloodAxeCairnSlabCluster_A01_LOD0_PaintTarget.fbx"

exec /home/Flamestrike/Tools/ArmorPaint/ArmorPaint "$TARGET"
