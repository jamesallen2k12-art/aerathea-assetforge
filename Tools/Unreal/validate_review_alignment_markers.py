import math
import sys
from pathlib import Path

import unreal


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from Tools.review_alignment_markers import REVIEW_ALIGNMENT_MARKERS, REVIEW_MARKER_TAG  # noqa: E402


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"


def all_level_actors():
    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    return list(actor_subsystem.get_all_level_actors())


def vector_distance(a, b):
    return math.sqrt(((a.x - b.x) ** 2) + ((a.y - b.y) ** 2) + ((a.z - b.z) ** 2))


def actor_hidden(actor):
    try:
        return bool(actor.get_actor_hidden_in_game())
    except Exception:
        try:
            return bool(actor.get_editor_property("hidden"))
        except Exception:
            return False


def component_hidden_or_invisible(component):
    hidden = False
    visible = True
    try:
        hidden = bool(component.is_hidden_in_game())
    except Exception:
        pass
    try:
        visible = bool(component.is_visible())
    except Exception:
        pass
    return hidden or not visible


def main():
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    actors_by_label = {actor.get_actor_label(): actor for actor in all_level_actors()}
    failures = []
    plane_z_values = []

    for marker in REVIEW_ALIGNMENT_MARKERS:
        marker_id = marker["id"]
        marker_label = "AET_REVIEW_MARKER_{}".format(marker_id)
        label_actor_label = "AET_REVIEW_MARKER_LABEL_{}".format(marker_id)
        expected = unreal.Vector(*marker["location"])
        marker_actor = actors_by_label.get(marker_label)
        text_actor = actors_by_label.get(label_actor_label)
        if marker_actor is None:
            failures.append("Missing {}".format(marker_label))
            continue
        if text_actor is None:
            failures.append("Missing {}".format(label_actor_label))
            continue

        if unreal.Name(REVIEW_MARKER_TAG) not in marker_actor.get_editor_property("tags"):
            failures.append("{} missing {}".format(marker_label, REVIEW_MARKER_TAG))
        if unreal.Name(REVIEW_MARKER_TAG) not in text_actor.get_editor_property("tags"):
            failures.append("{} missing {}".format(label_actor_label, REVIEW_MARKER_TAG))

        distance = vector_distance(marker_actor.get_actor_location(), expected)
        if distance > 1.0:
            failures.append("{} location is {:.2f} cm from expected {}".format(marker_label, distance, expected))

        if marker_id != "E":
            plane_z_values.append(marker_actor.get_actor_location().z)
        elif marker_actor.get_actor_location().z <= max(plane_z_values or [0.0]) + 200.0:
            failures.append("{} is not high enough above the A/B/C/D plane".format(marker_label))

        if not actor_hidden(marker_actor):
            failures.append("{} should be hidden in game by default".format(marker_label))
        if not actor_hidden(text_actor):
            failures.append("{} should be hidden in game by default".format(label_actor_label))

        for actor in (marker_actor, text_actor):
            for component in actor.get_components_by_class(unreal.PrimitiveComponent):
                if not component_hidden_or_invisible(component):
                    failures.append("{} component {} should be hidden/invisible by default".format(actor.get_actor_label(), component.get_name()))

    if failures:
        raise RuntimeError("Review marker validation failed: {}".format("; ".join(failures)))

    unreal.log("Aerathea review marker validation complete: {} markers plus labels, hidden by default.".format(len(REVIEW_ALIGNMENT_MARKERS)))


main()
