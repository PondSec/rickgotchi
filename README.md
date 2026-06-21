# Rickgotchi

Rickgotchi is a fan-made set of Pwnagotchi character packs inspired by Rick and Morty. The repository currently ships three complete packs:

| Character | Folder | Voice languages |
| --- | --- | --- |
| Rick Sanchez | `rick-sanchez` | `en`, `de`, `es`, `fr`, `it`, `pt`, `nl`, `pl`, `tr`, `sv` |
| Morty Smith | `morty-smith` | `en`, `de`, `es`, `fr`, `it`, `pt`, `nl`, `pl`, `tr`, `sv` |
| Pickle Rick | `pickle-rick` | `en`, `de`, `es`, `fr`, `it`, `pt`, `nl`, `pl`, `tr`, `sv` |

Each pack includes:

- PNG face assets for the Pwnagotchi face states
- a standalone `voice.py` replacement
- many character-specific line combinations for normal, bored, excited, sad, angry, peer, session, upload/download, handshake, and status callbacks

The supported languages are embedded directly in each `voice.py`, so you do not need to copy separate `.po` or `.mo` files.

## Quick Install

Clone the repository on your Pwnagotchi and run one of:

```bash
scripts/install-character.sh rick-sanchez
scripts/install-character.sh morty-smith
scripts/install-character.sh pickle-rick
```

The installer copies the selected faces to `/custom-faces`, finds the active Pwnagotchi `voice.py`, backs it up, and installs the selected character voice.

Then open your config:

```bash
sudo nano /etc/pwnagotchi/config.toml
```

Paste or merge the face block from:

```bash
config/faces.toml
```

Set the voice language:

```toml
main.lang = "de"
```

Supported values are `en`, `de`, `es`, `fr`, `it`, `pt`, `nl`, `pl`, `tr`, and `sv`.

## Manual Install

Copy one character's faces:

```bash
sudo mkdir -p /custom-faces
sudo rm -rf /custom-faces/*
sudo cp -a rick-sanchez/custom-faces/. /custom-faces/
```

Find the real `voice.py` location:

```bash
sudo find / -name voice.py 2>/dev/null
```

On Jayofelony Pwnagotchi 2.9.5.3 images, the path is commonly inside the hidden `.pwn` virtual environment:

```text
/home/pi/.pwn/lib/python3.11/site-packages/pwnagotchi/voice.py
```

Other images may use a system Python path:

```text
/usr/local/lib/python3.11/dist-packages/pwnagotchi/voice.py
```

Use the path found on your device:

```bash
VOICE_PATH="$(sudo find / -path '*/pwnagotchi/voice.py' -print -quit 2>/dev/null)"
sudo cp "$VOICE_PATH" "$VOICE_PATH.rickgotchi-backup"
sudo cp rick-sanchez/voice.py "$VOICE_PATH"
```

Replace `rick-sanchez` with `morty-smith` or `pickle-rick` if you want another pack.

## Testing

Local test suite:

```bash
make test
```

## Development

Regenerate the voice files after editing the phrase banks:

```bash
make build-voices
```

Project files:

- `characters.json`: character manifest and supported voice languages
- `config/faces.toml`: reusable Pwnagotchi PNG face config
- `scripts/build_voices.py`: source generator for standalone voice files
- `scripts/install-character.sh`: installer for a selected character pack
- `tests/`: local and container-compatible compatibility checks

## Responsible Use

Use Rickgotchi only on networks and devices you own or are explicitly allowed to test.
