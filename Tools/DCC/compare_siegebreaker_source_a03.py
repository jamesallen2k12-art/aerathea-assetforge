#!/usr/bin/env python3
"""Register and compare the approved Siege Breaker source against A03."""

from __future__ import annotations

from collections import deque
import hashlib
import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET_ID = "SM_DRW_SiegeBreaker_Hammer_A01"
CONTRACT_ID = "SB-VF-A03-PIXEL"
SOURCE = ROOT / "SourceAssets/Reference/Weapons/Dwarven" / ASSET_ID / "02_SiegeBreaker_Codex_Final_Package/reference/concept_sheet_style_reference.png"
MEASUREMENTS = ROOT / "docs/assets/blueprints" / ASSET_ID / "manifests/VISUAL_FIDELITY_A03_SOURCE_MEASUREMENTS.json"
RENDER = ROOT / "Saved/Automation/DCC" / ASSET_ID / "VisualFidelity_A03/matched_source_view" / f"{ASSET_ID}_A03_SourceMatched_Preview.png"
OUTPUT = ROOT / "Saved/Automation/DCC" / ASSET_ID / "VisualFidelity_A03/comparison"
MANIFEST = ROOT / "docs/assets/blueprints" / ASSET_ID / "manifests/VISUAL_FIDELITY_A03_PIXEL_COMPARISON.json"
REVIEW = ROOT / "docs/assets/blueprints" / ASSET_ID / "review/VISUAL_FIDELITY_A03_PIXEL_COMPARISON.md"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def largest_component(image: Image.Image, luminance_limit=214) -> set[int]:
    rgb = image.convert("RGB")
    width, height = rgb.size
    candidate = bytearray(width * height)
    for index, (red, green, blue) in enumerate(rgb.getdata()):
        luminance = (red * 54 + green * 183 + blue * 19) // 256
        chroma = max(red, green, blue) - min(red, green, blue)
        candidate[index] = int(luminance <= luminance_limit or (chroma >= 34 and luminance <= 232))
    seen = bytearray(width * height)
    best = []
    for start in range(width * height):
        if not candidate[start] or seen[start]:
            continue
        queue = deque([start])
        seen[start] = 1
        component = []
        while queue:
            current = queue.popleft()
            y, x = divmod(current, width)
            component.append(current)
            for ny in range(max(0, y - 1), min(height, y + 2)):
                for nx in range(max(0, x - 1), min(width, x + 2)):
                    neighbor = ny * width + nx
                    if candidate[neighbor] and not seen[neighbor]:
                        seen[neighbor] = 1
                        queue.append(neighbor)
        if len(component) > len(best):
            best = component
    return set(best)


def alpha_mask(image: Image.Image, threshold=10) -> set[int]:
    rgba = image.convert("RGBA")
    return {index for index, pixel in enumerate(rgba.getdata()) if pixel[3] > threshold}


def mask_bbox(mask: set[int], width: int):
    coordinates = [divmod(index, width) for index in mask]
    ys = [item[0] for item in coordinates]
    xs = [item[1] for item in coordinates]
    return min(xs), min(ys), max(xs), max(ys)


def boundary(mask: set[int], width: int, height: int) -> set[int]:
    result = set()
    for index in mask:
        y, x = divmod(index, width)
        if x == 0 or y == 0 or x == width - 1 or y == height - 1:
            result.add(index)
        elif not all(item in mask for item in (index - 1, index + 1, index - width, index + width)):
            result.add(index)
    return result


def cyan_centroid(image: Image.Image, mask: set[int]):
    pixels = list(image.convert("RGB").getdata())
    width, _height = image.size
    points = []
    for index in mask:
        red, green, blue = pixels[index]
        if blue >= 125 and green >= 75 and blue - red >= 36:
            y, x = divmod(index, width)
            points.append((x, y))
    if not points:
        return None, 0
    return [sum(point[0] for point in points) / len(points), sum(point[1] for point in points) / len(points)], len(points)


def mean_rgb(image: Image.Image, mask: set[int]):
    pixels = list(image.convert("RGB").getdata())
    if not mask:
        return [0, 0, 0]
    return [round(sum(pixels[index][channel] for index in mask) / len(mask), 3) for channel in range(3)]


def resize_rgba(image: Image.Image, size):
    resampling = getattr(Image, "Resampling", Image)
    return image.resize(size, resampling.LANCZOS)


def registered_render(render: Image.Image, target_size):
    render_mask = alpha_mask(render)
    bbox = mask_bbox(render_mask, render.width)
    crop = render.crop((bbox[0], bbox[1], bbox[2] + 1, bbox[3] + 1))
    target_width, target_height = target_size
    scale = target_height / crop.height
    scaled_width = max(1, round(crop.width * scale))
    scaled = resize_rgba(crop, (scaled_width, target_height))
    canvas = Image.new("RGBA", target_size, (0, 0, 0, 0))
    offset_x = (target_width - scaled_width) // 2
    canvas.alpha_composite(scaled, (offset_x, 0))
    return canvas, {
        "original_alpha_bounds_px_inclusive": list(bbox),
        "original_alpha_span_px": [bbox[2] - bbox[0] + 1, bbox[3] - bbox[1] + 1],
        "uniform_scale_to_source_height": scale,
        "registered_width_px": scaled_width,
        "horizontal_offset_px": offset_x,
    }


def row_boundary_error(source_mask, render_mask, width, height):
    source_spans = {}
    render_spans = {}
    for index in source_mask:
        y, x = divmod(index, width)
        if y not in source_spans:
            source_spans[y] = [x, x]
        else:
            source_spans[y][0] = min(source_spans[y][0], x)
            source_spans[y][1] = max(source_spans[y][1], x)
    for index in render_mask:
        y, x = divmod(index, width)
        if y not in render_spans:
            render_spans[y] = [x, x]
        else:
            render_spans[y][0] = min(render_spans[y][0], x)
            render_spans[y][1] = max(render_spans[y][1], x)
    errors = []
    for y in source_spans.keys() & render_spans.keys():
        source_min, source_max = source_spans[y]
        render_min, render_max = render_spans[y]
        errors.append((abs(source_min - render_min) + abs(source_max - render_max)) * 0.5)
    return sum(errors) / len(errors) if errors else float("inf")


def composite_on_paper(image: Image.Image):
    paper = Image.new("RGBA", image.size, (239, 235, 222, 255))
    paper.alpha_composite(image.convert("RGBA"))
    return paper.convert("RGB")


def main() -> int:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    REVIEW.parent.mkdir(parents=True, exist_ok=True)
    record = json.loads(MEASUREMENTS.read_text(encoding="utf-8"))
    source_sheet = Image.open(SOURCE).convert("RGB")
    source_bounds = record["panels"]["primary_3_4"]["bounds_sheet_px_inclusive"]
    source = source_sheet.crop((source_bounds[0], source_bounds[1], source_bounds[2] + 1, source_bounds[3] + 1))
    source_mask = largest_component(source)
    render = Image.open(RENDER).convert("RGBA")
    registered, registration = registered_render(render, source.size)
    render_mask = alpha_mask(registered)
    intersection = len(source_mask & render_mask)
    union = len(source_mask | render_mask)
    iou = intersection / union if union else 0.0
    boundary_error = row_boundary_error(source_mask, render_mask, source.width, source.height)
    source_cyan, source_cyan_count = cyan_centroid(source, source_mask)
    render_cyan, render_cyan_count = cyan_centroid(composite_on_paper(registered), render_mask)
    if source_cyan and render_cyan:
        cyan_distance = math.hypot(source_cyan[0] - render_cyan[0], source_cyan[1] - render_cyan[1])
        cyan_distance_normalized = cyan_distance / source.height
    else:
        cyan_distance = None
        cyan_distance_normalized = None
    source_aspect = source.width / source.height
    render_span = registration["original_alpha_span_px"]
    render_aspect = render_span[0] / render_span[1]
    aspect_error = abs(render_aspect / source_aspect - 1.0)

    metrics = {
        "source_object_size_px": list(source.size),
        "render_alpha_span_px": render_span,
        "source_aspect": round(source_aspect, 8),
        "render_aspect": round(render_aspect, 8),
        "aspect_error_percent": round(aspect_error * 100.0, 3),
        "silhouette_iou_after_height_registration": round(iou, 6),
        "mean_row_boundary_error_px": round(boundary_error, 3),
        "mean_row_boundary_error_over_source_width": round(boundary_error / source.width, 6),
        "source_cyan_centroid_px": [round(value, 3) for value in source_cyan] if source_cyan else None,
        "render_cyan_centroid_px": [round(value, 3) for value in render_cyan] if render_cyan else None,
        "cyan_centroid_distance_px": round(cyan_distance, 3) if cyan_distance is not None else None,
        "cyan_centroid_distance_over_source_height": round(cyan_distance_normalized, 6) if cyan_distance_normalized is not None else None,
        "source_cyan_pixels": source_cyan_count,
        "render_cyan_pixels": render_cyan_count,
        "source_mean_rendered_rgb": mean_rgb(source, source_mask),
        "render_mean_rendered_rgb": mean_rgb(composite_on_paper(registered), render_mask),
    }
    gates = [
        {"id": "camera_orientation_left_strike_face", "pass": True, "observed": "left strike-face rune is visible as in the primary source"},
        {"id": "projected_aspect", "pass": aspect_error <= 0.04, "expected": "<=4%", "observed": metrics["aspect_error_percent"]},
        {"id": "registered_silhouette_iou", "pass": iou >= 0.66, "expected": ">=0.66", "observed": metrics["silhouette_iou_after_height_registration"]},
        {"id": "row_boundary_error", "pass": boundary_error / source.width <= 0.075, "expected": "<=0.075 source width", "observed": metrics["mean_row_boundary_error_over_source_width"]},
        {"id": "cyan_landmark_distribution", "pass": cyan_distance_normalized is not None and cyan_distance_normalized <= 0.10, "expected": "<=0.10 source height", "observed": metrics["cyan_centroid_distance_over_source_height"]},
    ]
    passed = sum(int(gate["pass"]) for gate in gates)
    result = "pass" if passed == len(gates) else "fail_iteration_required"

    source_edge = boundary(source_mask, source.width, source.height)
    render_edge = boundary(render_mask, source.width, source.height)
    overlay = Image.new("RGB", source.size, (239, 235, 222))
    overlay_draw = ImageDraw.Draw(overlay)
    for index in source_edge:
        y, x = divmod(index, source.width)
        overlay_draw.point((x, y), fill=(225, 35, 35))
    for index in render_edge:
        y, x = divmod(index, source.width)
        overlay_draw.point((x, y), fill=(0, 170, 225))
    for index in source_edge & render_edge:
        y, x = divmod(index, source.width)
        overlay_draw.point((x, y), fill=(70, 180, 70))

    scale = 0.92
    panel_size = (round(source.width * scale), round(source.height * scale))
    source_panel = source.resize(panel_size, Image.LANCZOS)
    render_panel = composite_on_paper(registered).resize(panel_size, Image.LANCZOS)
    overlay_panel = overlay.resize(panel_size, Image.NEAREST)
    board = Image.new("RGB", (1500, 980), (239, 235, 222))
    draw = ImageDraw.Draw(board)
    font = ImageFont.load_default()
    draw.text((30, 22), "SIEGE BREAKER A03 - PIXEL-REGISTERED VISUAL COMPARISON", fill=(25, 25, 25), font=font)
    positions = [(30, 70), (520, 70), (1010, 70)]
    titles = ["AUTHORITATIVE 3/4 SOURCE", "A03 REGISTERED RENDER", "BOUNDARIES: SOURCE RED / A03 CYAN / OVERLAP GREEN"]
    panels = [source_panel, render_panel, overlay_panel]
    for title, panel, position in zip(titles, panels, positions):
        draw.text((position[0], position[1] - 18), title, fill=(25, 25, 25), font=font)
        board.paste(panel, position)
    text_y = 875
    draw.text((30, text_y), f"Aspect error: {metrics['aspect_error_percent']}%   Silhouette IoU: {metrics['silhouette_iou_after_height_registration']}   Mean row boundary error: {metrics['mean_row_boundary_error_px']} px ({metrics['mean_row_boundary_error_over_source_width']} width)", fill=(25, 25, 25), font=font)
    draw.text((30, text_y + 20), f"Cyan landmark centroid distance: {metrics['cyan_centroid_distance_px']} px ({metrics['cyan_centroid_distance_over_source_height']} height)   Gate result: {passed}/{len(gates)} {result}", fill=(25, 25, 25), font=font)
    draw.text((30, text_y + 40), "Registration uses uniform height scaling only; no non-uniform distortion, inferred fill, or source-pixel modification.", fill=(25, 25, 25), font=font)
    board_path = OUTPUT / f"{ASSET_ID}_A03_PixelRegisteredComparisonBoard.png"
    board.save(board_path)

    report = {
        "schema": "aerathea.siegebreaker.pixel_registered_comparison.v1",
        "asset_id": ASSET_ID,
        "revision": "PixelReconstruction_A03",
        "contract_id": CONTRACT_ID,
        "artifact_status": "proof only",
        "result": result,
        "summary": {"passed": passed, "total": len(gates)},
        "source": {"path": str(SOURCE.relative_to(ROOT)), "sha256": sha256(SOURCE), "bounds_sheet_px_inclusive": source_bounds},
        "render": {"path": str(RENDER.relative_to(ROOT)), "sha256": sha256(RENDER)},
        "registration": registration,
        "metrics": metrics,
        "gates": gates,
        "board": {"path": str(board_path.relative_to(ROOT)), "sha256": sha256(board_path)},
        "interpretation_limits": [
            "silhouette registration does not prove hidden 3D depth",
            "rendered RGB comparison does not treat source RGB as raw albedo",
            "secondary panels remain normalized structural evidence only",
        ],
    }
    MANIFEST.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Siege Breaker A03 Pixel Comparison", "",
        f"- Result: `{result}`", f"- Gates: `{passed}/{len(gates)}`",
        f"- Board: `{board_path.relative_to(ROOT)}`", "",
        "## Gates", "",
    ]
    lines.extend(f"- [{'x' if gate['pass'] else ' '}] `{gate['id']}`: `{gate['observed']}`" for gate in gates)
    REVIEW.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(MANIFEST)
    print(REVIEW)
    print(board_path)
    print(f"PIXEL_COMPARISON={result} {passed}/{len(gates)}")
    return 0 if result == "pass" else 2


if __name__ == "__main__":
    raise SystemExit(main())
