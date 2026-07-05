#!/usr/bin/env python3
"""Create a lossless RGB scanline capture and reconstruction proof for an image."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import struct
from pathlib import Path

from PIL import Image, ImageChops, ImageOps, ImageStat


SCAN_MAGIC = b"AET_RGB_SCANLINE_V1\n"


def pixel_sha256(image: Image.Image) -> str:
    return hashlib.sha256(image.convert("RGB").tobytes("raw", "RGB")).hexdigest()


def iter_scanlines(image: Image.Image):
    rgb = image.convert("RGB")
    width, height = rgb.size
    raw = rgb.tobytes("raw", "RGB")
    stride = width * 3
    for y in range(height):
        start = y * stride
        yield y, raw[start : start + stride]


def write_scan_record(image: Image.Image, path: Path) -> tuple[str, list[str], int]:
    width, height = image.size
    digest = hashlib.sha256()
    row_hashes: list[str] = []
    byte_count = 0
    with gzip.open(path, "wb") as scan:
        scan.write(SCAN_MAGIC)
        scan.write(f"{width} {height} 3 RGB\n".encode("ascii"))
        for y, row_bytes in iter_scanlines(image):
            digest.update(row_bytes)
            row_hashes.append(hashlib.sha256(row_bytes).hexdigest())
            byte_count += len(row_bytes)
            scan.write(struct.pack(">I", y))
            scan.write(row_bytes)
    return digest.hexdigest(), row_hashes, byte_count


def read_scan_record(path: Path) -> Image.Image:
    with gzip.open(path, "rb") as scan:
        magic = scan.readline()
        if magic != SCAN_MAGIC:
            raise ValueError(f"Unsupported scanline record: {path}")
        meta = scan.readline().decode("ascii").strip().split()
        if len(meta) != 4 or meta[2] != "3" or meta[3] != "RGB":
            raise ValueError(f"Invalid scanline metadata in {path}: {meta}")
        width = int(meta[0])
        height = int(meta[1])
        stride = width * 3
        rows: list[bytes] = []
        for expected_y in range(height):
            raw_index = scan.read(4)
            if len(raw_index) != 4:
                raise ValueError(f"Unexpected end of record before row {expected_y}")
            (actual_y,) = struct.unpack(">I", raw_index)
            if actual_y != expected_y:
                raise ValueError(f"Scanline order mismatch: expected {expected_y}, got {actual_y}")
            row = scan.read(stride)
            if len(row) != stride:
                raise ValueError(f"Short scanline {expected_y}: expected {stride}, got {len(row)}")
            rows.append(row)
    return Image.frombytes("RGB", (width, height), b"".join(rows))


def write_difference(target: Image.Image, rebuild: Image.Image, path: Path) -> tuple[int, int, float]:
    diff = ImageChops.difference(target.convert("RGB"), rebuild.convert("RGB"))
    extrema = diff.getextrema()
    max_delta = max(channel[1] for channel in extrema)
    gray = ImageOps.grayscale(diff)
    histogram = gray.histogram()
    nonzero_pixels = sum(histogram[1:])
    mean_delta = float(ImageStat.Stat(gray).mean[0])
    if max_delta == 0:
        visible = Image.new("RGB", target.size, (0, 0, 0))
    else:
        visible = diff
    visible.save(path, optimize=True)
    return max_delta, nonzero_pixels, mean_delta


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="Source PNG/JPG/etc. to scan.")
    parser.add_argument("--out-dir", required=True, type=Path, help="Output directory for scan proof files.")
    parser.add_argument("--asset-id", required=True, help="Stable asset/reference identifier used in output names.")
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    target_path = args.out_dir / f"{args.asset_id}_ScanTarget.png"
    scan_path = args.out_dir / f"{args.asset_id}.rgbscan.gz"
    rebuild_path = args.out_dir / f"{args.asset_id}_RebuiltFromScanlines.png"
    diff_path = args.out_dir / f"{args.asset_id}_Difference.png"
    manifest_path = args.out_dir / f"{args.asset_id}_ScanlineManifest.json"

    with Image.open(args.input) as source:
        target = source.convert("RGB")
    target.save(target_path, optimize=True)
    scan_sha256, row_hashes, byte_count = write_scan_record(target, scan_path)
    rebuild = read_scan_record(scan_path)
    rebuild.save(rebuild_path, optimize=True)
    max_delta, nonzero_pixels, mean_delta = write_difference(target, rebuild, diff_path)

    manifest = {
        "format": "AET_RGB_SCANLINE_V1",
        "asset_id": args.asset_id,
        "source": str(args.input),
        "target_image": str(target_path),
        "scan_record": str(scan_path),
        "rebuilt_image": str(rebuild_path),
        "difference_image": str(diff_path),
        "width": target.width,
        "height": target.height,
        "scanlines": target.height,
        "rgb_bytes": byte_count,
        "scan_sha256": scan_sha256,
        "target_pixel_sha256": pixel_sha256(target),
        "rebuild_pixel_sha256": pixel_sha256(rebuild),
        "max_rgb_delta": max_delta,
        "changed_pixels": nonzero_pixels,
        "mean_grayscale_delta": mean_delta,
        "first_row_sha256": row_hashes[0],
        "middle_row_sha256": row_hashes[len(row_hashes) // 2],
        "last_row_sha256": row_hashes[-1],
        "pixel_exact": max_delta == 0 and nonzero_pixels == 0 and pixel_sha256(target) == pixel_sha256(rebuild),
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(manifest_path)
    print(rebuild_path)
    print(diff_path)
    print(f"pixel_exact={manifest['pixel_exact']} max_rgb_delta={max_delta} changed_pixels={nonzero_pixels}")
    return 0 if manifest["pixel_exact"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
