#!/usr/bin/env bash
set -euo pipefail

ROOT="${AET_ROOT:-/home/james/Projects/Aerathea}"
BENCHMARK_ID="${BENCHMARK_ID:-bloodaxe_a1_target_multiview_mesh}"
TRELLIS_ROOT="$ROOT/Tools/External/TRELLIS-AMD"
PY="$TRELLIS_ROOT/.venv/bin/python"
RUNNER="$ROOT/Saved/AssetForgeResearch/benchmarks/trellis_amd_multiview_benchmark_runner.py"
INPUT_ROOT="$ROOT/Saved/AssetForgeResearch/benchmarks/inputs/bloodaxe_a1_target_multiview"
OUTPUT_ROOT="$ROOT/Saved/AssetForgeResearch/benchmarks/outputs/trellis-amd"
LOG_ROOT="$ROOT/Saved/AssetForgeResearch/benchmarks/logs"
LOG_FILE="$LOG_ROOT/${BENCHMARK_ID}.log"

inputs=(
    "$INPUT_ROOT/bloodaxe_a1_target_multiview_front.png"
    "$INPUT_ROOT/bloodaxe_a1_target_multiview_right.png"
    "$INPUT_ROOT/bloodaxe_a1_target_multiview_back.png"
    "$INPUT_ROOT/bloodaxe_a1_target_multiview_left.png"
    "$INPUT_ROOT/bloodaxe_a1_target_multiview_hero.png"
)

mkdir -p "$LOG_ROOT" "$OUTPUT_ROOT"

for input in "${inputs[@]}"; do
    if [[ ! -f "$input" ]]; then
        echo "Missing TRELLIS input: $input" >&2
        exit 1
    fi
done

echo "Starting $BENCHMARK_ID"
echo "Log: $LOG_FILE"

(
    cd "$TRELLIS_ROOT"
    export PYTHONPATH="$TRELLIS_ROOT"
    export HUGGINGFACE_HUB_CACHE="$ROOT/Saved/AssetForgeResearch/TRELLIS-AMD/weights/hub"
    export TORCH_HOME="$ROOT/Saved/AssetForgeResearch/TRELLIS-AMD/weights/torch"
    export TORCH_EXTENSIONS_DIR="$ROOT/Saved/AssetForgeResearch/TRELLIS-AMD/torch_extensions"
    export LD_LIBRARY_PATH="$TRELLIS_ROOT/.venv/lib/python3.10/site-packages/torch/lib:/opt/rocm/lib:/opt/rocm/hip/lib:${LD_LIBRARY_PATH:-}"
    export SPCONV_ALGO="native"
    export TORCH_ROCM_AOTRITON_ENABLE_EXPERIMENTAL="1"
    export PYTHONUNBUFFERED="1"

    exec systemd-inhibit --what=idle:sleep --who=Codex --why="Aerathea Blood Axe A1 TRELLIS-AMD reference" \
        /usr/bin/time -v "$PY" "$RUNNER" \
        --benchmark-id "$BENCHMARK_ID" \
        --input "${inputs[0]}" \
        --input "${inputs[1]}" \
        --input "${inputs[2]}" \
        --input "${inputs[3]}" \
        --input "${inputs[4]}" \
        --output-root "$OUTPUT_ROOT" \
        --seed 1 \
        --ss-steps 12 \
        --ss-cfg-strength 7.5 \
        --slat-steps 12 \
        --slat-cfg-strength 3.0 \
        --mode multidiffusion \
        --formats mesh \
        --preprocess-image
) > "$LOG_FILE" 2>&1

echo "Completed $BENCHMARK_ID"
echo "Log: $LOG_FILE"
tail -n 80 "$LOG_FILE"
