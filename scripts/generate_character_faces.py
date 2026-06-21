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


def ellipse(draw, box, width=1):
    draw.ellipse(coords(box), outline=LINE, width=s(width))


def arc(draw, box, start, end, width=1):
    draw.arc(coords(box), start, end, fill=LINE, width=s(width))


def text(draw, xy, value):
    draw.text((s(xy[0]), s(xy[1])), value, fill=LINE)


def draw_character_base(draw, character):
    if character == "jerry-smith":
        ellipse(draw, (22, 14, 53, 61))
        arc(draw, (22, 12, 53, 32), 190, 350)
        line(draw, [(25, 20), (30, 15), (35, 18), (40, 15), (48, 21)])
        ellipse(draw, (18, 34, 24, 43))
        ellipse(draw, (51, 34, 57, 43))
        line(draw, [(30, 61), (29, 67), (45, 67), (44, 61)])
        line(draw, [(26, 67), (49, 67)])
    elif character == "beth-smith":
        ellipse(draw, (22, 16, 53, 62))
        arc(draw, (17, 10, 58, 56), 200, 340)
        line(draw, [(24, 18), (31, 11), (42, 13), (52, 23)])
        line(draw, [(21, 22), (17, 38), (22, 54)])
        line(draw, [(53, 24), (58, 39), (53, 56)])
        ellipse(draw, (18, 35, 24, 43))
        ellipse(draw, (51, 35, 57, 43))
        line(draw, [(31, 62), (29, 68), (46, 68), (44, 62)])
        line(draw, [(25, 68), (50, 68)])
    elif character == "summer-smith":
        ellipse(draw, (23, 17, 53, 62))
        arc(draw, (18, 11, 58, 55), 195, 345)
        line(draw, [(24, 20), (33, 13), (45, 16), (54, 25)])
        line(draw, [(22, 23), (18, 40), (23, 57)])
        line(draw, [(52, 25), (58, 38), (53, 55)])
        ellipse(draw, (52, 24, 64, 43))
        ellipse(draw, (19, 35, 25, 43))
        ellipse(draw, (50, 35, 56, 43))
        line(draw, [(31, 62), (30, 68), (46, 68), (45, 62)])
        line(draw, [(26, 68), (50, 68)])


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

    if eyes in {"sleep", "sleep2"}:
        line(draw, [(29, 38), (36, 38)])
        line(draw, [(40, 38), (47, 38)])
        if eyes == "sleep2":
            text(draw, (50, 44), "z")
            text(draw, (56, 39), "z")
        return

    if eyes == "dead":
        line(draw, [(29, 34), (36, 41)])
        line(draw, [(36, 34), (29, 41)])
        line(draw, [(40, 34), (47, 41)])
        line(draw, [(47, 34), (40, 41)])
        return

    if eyes == "cool":
        draw.rectangle(coords((27, 34, 37, 41)), outline=LINE, width=s(1))
        draw.rectangle(coords((39, 34, 49, 41)), outline=LINE, width=s(1))
        line(draw, [(37, 37), (39, 37)])
        return

    if eyes == "happy":
        arc(draw, (28, 34, 37, 42), 200, 340)
        arc(draw, (39, 34, 48, 42), 200, 340)
        return

    if eyes == "soft":
        arc(draw, (28, 34, 37, 42), 190, 350)
        arc(draw, (39, 34, 48, 42), 190, 350)
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
        ellipse(draw, (27, 32, 37, 43))
        ellipse(draw, (39, 32, 49, 43))
        ellipse(draw, (31, 36, 33, 38))
        ellipse(draw, (43, 36, 45, 38))
        return

    ellipse(draw, (28, 34, 37, 43))
    ellipse(draw, (39, 34, 48, 43))

    pupil_offset = 0
    if eyes == "left":
        pupil_offset = -2
    elif eyes == "right":
        pupil_offset = 2
    elif eyes == "half":
        line(draw, [(28, 36), (37, 36)])
        line(draw, [(39, 36), (48, 36)])

    ellipse(draw, (31 + pupil_offset, 38, 33 + pupil_offset, 40))
    ellipse(draw, (42 + pupil_offset, 38, 44 + pupil_offset, 40))

    if character in {"beth-smith", "summer-smith"}:
        line(draw, [(27, 35), (25, 33)])
        line(draw, [(49, 35), (51, 33)])


def draw_mouth(draw, mouth):
    if mouth == "smile":
        arc(draw, (31, 45, 46, 56), 20, 160)
    elif mouth == "smirk":
        line(draw, [(32, 51), (45, 48)])
    elif mouth == "sad":
        arc(draw, (31, 49, 46, 59), 200, 340)
    elif mouth == "frown":
        arc(draw, (31, 48, 46, 59), 200, 340)
        line(draw, [(31, 49), (29, 48)])
        line(draw, [(46, 49), (48, 48)])
    elif mouth == "open":
        ellipse(draw, (34, 48, 42, 56))
    elif mouth == "sleep":
        text(draw, (35, 49), "o")
    else:
        line(draw, [(32, 51), (45, 51)])


def draw_face(character, eyes, mouth):
    canvas = Image.new("RGBA", (SIZE * SCALE, SIZE * SCALE), (255, 255, 255, 0))
    draw = ImageDraw.Draw(canvas)
    draw_character_base(draw, character)
    draw_eye_pair(draw, eyes, character)
    draw_mouth(draw, mouth)
    return canvas.resize((SIZE, SIZE), Image.Resampling.LANCZOS)


def main():
    for character in ("jerry-smith", "beth-smith", "summer-smith"):
        output_dir = ROOT / character / "custom-faces"
        output_dir.mkdir(parents=True, exist_ok=True)
        for state, (eyes, mouth) in STATES.items():
            draw_face(character, eyes, mouth).save(output_dir / f"{state}.png")


if __name__ == "__main__":
    main()
