#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_FACES = {
    "ANGRY", "AWAKE", "BORED", "BROKEN", "COOL", "DEBUG", "DEMOTIVATED",
    "EXCITED", "FRIEND", "GRATEFUL", "HAPPY", "INTENSE", "LONELY",
    "LOOK_L", "LOOK_L_HAPPY", "LOOK_R", "LOOK_R_HAPPY", "MOTIVATED",
    "SAD", "SLEEP", "SLEEP2", "SMART", "UPLOAD", "UPLOAD1", "UPLOAD2",
}


def main():
    manifest = json.loads((ROOT / "characters.json").read_text())
    for character in manifest["characters"]:
        faces_dir = ROOT / character["faces"]
        files = {path.stem for path in faces_dir.glob("*.png") if path.name != "template.png"}
        missing = EXPECTED_FACES - files
        extra = files - EXPECTED_FACES
        if missing or extra:
            raise SystemExit(
                f"{character['slug']} face mismatch: missing={sorted(missing)} extra={sorted(extra)}"
            )

        voice_path = ROOT / character["voice"]
        if not voice_path.is_file():
            raise SystemExit(f"Missing voice file: {voice_path}")


if __name__ == "__main__":
    main()

