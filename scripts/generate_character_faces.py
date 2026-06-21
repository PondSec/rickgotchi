#!/usr/bin/env python3
"""Generate line-art face packs for the extra Rickgotchi characters."""

from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
SIZE = 75
SCALE = 4
LINE = (0, 0, 0, 255)

STATES = {
    "AWAKE": ("open", "neutral"),
    "BROKEN": ("dead", "open"),
    "MOTIVATED": ("happy", "smile"),
    "BORED": ("half", "flat"),
    "COOL": ("cool", "smirk"),
    "UPLOAD": ("upload0", "smile"),
    "LONELY": ("sad", "sad"),
    "ANGRY": ("angry", "frown"),
    "GRATEFUL": ("soft", "smile"),
    "LOOK_R": ("right", "neutral"),
    "FRIEND": ("heart", "smile"),
    "INTENSE": ("wide", "open"),
    "DEBUG": ("debug", "flat"),
    "EXCITED": ("star", "open"),
    "SMART": ("smart", "smirk"),
    "LOOK_R_HAPPY": ("right", "smile"),
    "SLEEP2": ("sleep2", "sleep"),
    "LOOK_L_HAPPY": ("left", "smile"),
    "LOOK_L": ("left", "neutral"),
    "SLEEP": ("sleep", "sleep"),
    "SAD": ("sad", "sad"),
    "UPLOAD1": ("upload1", "smile"),
    "DEMOTIVATED": ("half", "sad"),
    "HAPPY": ("happy", "smile"),
    "UPLOAD2": ("upload2", "smile"),
}


def s(value):
    return int(round(value * SCALE))


def coords(values):
    return tuple(s(value) for value in values)


def line(draw, points, width=1):
    draw.line([(s(x), s(y)) for x, y in points], fill=LINE, width=s(width))


def polygon(draw, points, fill=None, width=1):
    scaled = [(s(x), s(y)) for x, y in points]
    if fill:
        draw.polygon(scaled, fill=fill)
    draw.line(scaled + [scaled[0]], fill=LINE, width=s(width))


def ellipse(draw, box, width=1):
    draw.ellipse(coords(box), outline=LINE, width=s(width))


def arc(draw, box, start, end, width=1):
    draw.arc(coords(box), start, end, fill=LINE, width=s(width))


def text(draw, xy, value):
    draw.text((s(xy[0]), s(xy[1])), value, fill=LINE)


def draw_character_base(draw, character):
    if character == "jerry-smith":
        polygon(draw, [(17, 32), (21, 20), (33, 13), (48, 12), (59, 20), (64, 36),
                       (61, 56), (50, 70), (34, 71), (22, 58), (14, 42)])
        polygon(draw, [(14, 38), (17, 27), (25, 17), (38, 10), (51, 10), (61, 17),
                       (67, 27), (66, 38), (60, 48), (55, 36), (47, 29), (35, 27),
                       (25, 31), (17, 43)], fill=LINE, width=1)
        ellipse(draw, (10, 42, 21, 55))
        line(draw, [(47, 39), (53, 56), (43, 57)])
        arc(draw, (26, 52, 36, 68), 110, 250)
        arc(draw, (50, 52, 60, 68), 290, 70)
    elif character == "beth-smith":
        polygon(draw, [(20, 23), (29, 12), (45, 13), (57, 25), (62, 45), (57, 64),
                       (46, 73), (31, 72), (20, 62), (15, 44)])
        arc(draw, (9, 2, 68, 67), 185, 350, width=2)
        line(draw, [(20, 24), (31, 9), (47, 11), (61, 28)], width=2)
        line(draw, [(16, 24), (10, 44), (18, 70)], width=2)
        line(draw, [(58, 25), (67, 45), (58, 71)], width=2)
        line(draw, [(39, 38), (43, 54), (37, 56)])
        ellipse(draw, (12, 41, 21, 51))
        ellipse(draw, (57, 41, 66, 51))
    elif character == "summer-smith":
        polygon(draw, [(19, 24), (30, 13), (47, 14), (58, 26), (62, 45), (57, 63),
                       (46, 72), (31, 71), (20, 61), (15, 43)])
        arc(draw, (9, 2, 68, 67), 190, 345, width=2)
        line(draw, [(20, 24), (34, 9), (51, 15), (61, 29)], width=2)
        line(draw, [(17, 25), (10, 43), (18, 68)], width=2)
        line(draw, [(57, 26), (65, 43), (58, 68)], width=2)
        ellipse(draw, (55, 22, 72, 49), width=2)
        line(draw, [(40, 39), (44, 54), (38, 56)])
        ellipse(draw, (12, 41, 21, 51))
        ellipse(draw, (56, 41, 65, 51))


def draw_eyebrows(draw, eyes):
    if eyes == "angry":
        line(draw, [(29, 32), (36, 29)])
        line(draw, [(40, 29), (47, 32)])
    elif eyes == "sad":
        line(draw, [(29, 30), (36, 32)])
        line(draw, [(40, 32), (47, 30)])
    elif eyes == "smart":
        line(draw, [(28, 31), (36, 31)])
        line(draw, [(40, 31), (48, 31)])


def draw_eye_pair(draw, eyes, character):
    draw_eyebrows(draw, eyes)
    if character == "jerry-smith":
        left = (25, 31, 42, 48)
        right = (47, 30, 65, 47)
        left_pupil = (36, 40)
        right_pupil = (58, 39)
    else:
        left = (25, 34, 38, 47)
        right = (42, 34, 55, 47)
        left_pupil = (32, 41)
        right_pupil = (49, 41)

    if eyes in {"sleep", "sleep2"}:
        line(draw, [(left[0] + 1, left[1] + 5), (left[2] - 1, left[1] + 5)])
        line(draw, [(right[0] + 1, right[1] + 5), (right[2] - 1, right[1] + 5)])
        if eyes == "sleep2":
            text(draw, (50, 44), "z")
            text(draw, (56, 39), "z")
        return

    if eyes == "dead":
        line(draw, [(left[0] + 1, left[1] + 1), (left[2] - 1, left[3] - 1)])
        line(draw, [(left[2] - 1, left[1] + 1), (left[0] + 1, left[3] - 1)])
        line(draw, [(right[0] + 1, right[1] + 1), (right[2] - 1, right[3] - 1)])
        line(draw, [(right[2] - 1, right[1] + 1), (right[0] + 1, right[3] - 1)])
        return

    if eyes == "cool":
        draw.rectangle(coords((left[0], left[1] + 2, left[2], left[3] - 2)), outline=LINE, width=s(1))
        draw.rectangle(coords((right[0], right[1] + 2, right[2], right[3] - 2)), outline=LINE, width=s(1))
        line(draw, [(left[2], left[1] + 6), (right[0], right[1] + 6)])
        return

    if eyes == "happy":
        arc(draw, (left[0], left[1] + 2, left[2], left[3]), 200, 340)
        arc(draw, (right[0], right[1] + 2, right[2], right[3]), 200, 340)
        return

    if eyes == "soft":
        arc(draw, (left[0], left[1] + 2, left[2], left[3]), 190, 350)
        arc(draw, (right[0], right[1] + 2, right[2], right[3]), 190, 350)
        return

    if eyes == "heart":
        text(draw, (28, 32), "<")
        text(draw, (42, 32), "3")
        return

    if eyes == "star":
        text(draw, (29, 33), "*")
        text(draw, (42, 33), "*")
        return

    if eyes == "debug":
        text(draw, (29, 32), "#")
        text(draw, (42, 32), "#")
        return

    if eyes.startswith("upload"):
        values = {
            "upload0": ("0", "1"),
            "upload1": ("1", "1"),
            "upload2": ("1", "0"),
        }[eyes]
        text(draw, (29, 33), values[0])
        text(draw, (43, 33), values[1])
        return

    if eyes == "wide":
        ellipse(draw, (left[0] - 1, left[1] - 2, left[2] + 1, left[3] + 1))
        ellipse(draw, (right[0] - 1, right[1] - 2, right[2] + 1, right[3] + 1))
        ellipse(draw, (left_pupil[0] - 1, left_pupil[1] - 1, left_pupil[0] + 1, left_pupil[1] + 1))
        ellipse(draw, (right_pupil[0] - 1, right_pupil[1] - 1, right_pupil[0] + 1, right_pupil[1] + 1))
        return

    ellipse(draw, left)
    ellipse(draw, right)

    pupil_offset = 0
    if eyes == "left":
        pupil_offset = -2
    elif eyes == "right":
        pupil_offset = 2
    elif eyes == "half":
        line(draw, [(28, 36), (37, 36)])
        line(draw, [(39, 36), (48, 36)])

    ellipse(draw, (left_pupil[0] - 1 + pupil_offset, left_pupil[1] - 1,
                   left_pupil[0] + 1 + pupil_offset, left_pupil[1] + 1))
    ellipse(draw, (right_pupil[0] - 1 + pupil_offset, right_pupil[1] - 1,
                   right_pupil[0] + 1 + pupil_offset, right_pupil[1] + 1))

    if character in {"beth-smith", "summer-smith"}:
        line(draw, [(27, 35), (25, 33)])
        line(draw, [(49, 35), (51, 33)])


def draw_mouth(draw, mouth, character):
    if character == "jerry-smith":
        smile_box = (28, 56, 57, 72)
        sad_box = (29, 56, 58, 73)
        open_box = (39, 57, 49, 67)
        flat_line = [(31, 62), (56, 62)]
    else:
        smile_box = (30, 50, 51, 64)
        sad_box = (30, 53, 52, 68)
        open_box = (35, 54, 45, 64)
        flat_line = [(31, 58), (51, 58)]

    if mouth == "smile":
        arc(draw, smile_box, 20, 160)
    elif mouth == "smirk":
        line(draw, [(flat_line[0][0], flat_line[0][1]), (flat_line[1][0], flat_line[1][1] - 3)])
    elif mouth == "sad":
        arc(draw, sad_box, 200, 340)
    elif mouth == "frown":
        arc(draw, sad_box, 200, 340)
        line(draw, [(sad_box[0], sad_box[1]), (sad_box[0] - 2, sad_box[1] - 1)])
        line(draw, [(sad_box[2], sad_box[1]), (sad_box[2] + 2, sad_box[1] - 1)])
    elif mouth == "open":
        ellipse(draw, open_box)
    elif mouth == "sleep":
        text(draw, (open_box[0] + 1, open_box[1]), "o")
    else:
        line(draw, flat_line)


def draw_face(character, eyes, mouth):
    canvas = Image.new("RGBA", (SIZE * SCALE, SIZE * SCALE), (255, 255, 255, 0))
    draw = ImageDraw.Draw(canvas)
    draw_character_base(draw, character)
    draw_eye_pair(draw, eyes, character)
    draw_mouth(draw, mouth, character)
    return canvas.resize((SIZE, SIZE), Image.Resampling.LANCZOS)


def main():
    for character in ("jerry-smith", "beth-smith", "summer-smith"):
        output_dir = ROOT / character / "custom-faces"
        output_dir.mkdir(parents=True, exist_ok=True)
        for state, (eyes, mouth) in STATES.items():
            draw_face(character, eyes, mouth).save(output_dir / f"{state}.png")


if __name__ == "__main__":
    main()
