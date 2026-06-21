# Rickgotchi

Rickgotchi is a fan-made set of Pwnagotchi character packs inspired by Rick and Morty. Each pack includes custom PNG faces plus a standalone `voice.py` with character-specific lines.

## Character Packs

| Character | Folder | Voice languages |
| --- | --- | --- |
| Rick Sanchez | `rick-sanchez` | `en`, `de`, `es`, `fr`, `it`, `pt`, `pt_BR` |
| Morty Smith | `morty-smith` | `en`, `de`, `es`, `fr`, `it`, `pt`, `pt_BR` |
| Pickle Rick | `pickle-rick` | `en`, `de`, `es`, `fr`, `it`, `pt`, `pt_BR` |
| Jerry Smith | `jerry-smith` | `en`, `de`, `es`, `fr`, `it`, `pt`, `pt_BR` |
| Beth Smith | `beth-smith` | `en`, `de`, `es`, `fr`, `it`, `pt`, `pt_BR` |
| Summer Smith | `summer-smith` | `en`, `de`, `es`, `fr`, `it`, `pt`, `pt_BR` |

## Quick Install

From the repository root, choose one character slug:

```bash
scripts/install-character.sh rick-sanchez
scripts/install-character.sh morty-smith
scripts/install-character.sh pickle-rick
scripts/install-character.sh jerry-smith
scripts/install-character.sh beth-smith
scripts/install-character.sh summer-smith
```

The installer:

- copies the selected face PNGs to `/custom-faces`
- finds the active Pwnagotchi `voice.py`
- creates a timestamped backup of the original voice file
- installs the selected character voice

Then open your Pwnagotchi config:

```bash
sudo nano /etc/pwnagotchi/config.toml
```

Paste or merge the face settings from:

```bash
config/faces.toml
```

Set the language you want:

```toml
main.lang = "de"
```

Supported values are `en`, `de`, `es`, `fr`, `it`, `pt`, and `pt_BR`.

## Manual Install

Copy the selected faces:

```bash
sudo mkdir -p /custom-faces
sudo rm -rf /custom-faces/*
sudo cp -a rick-sanchez/custom-faces/. /custom-faces/
```

Find the real `voice.py` location on your device:

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

Replace `rick-sanchez` with any other character folder.

## Face Config

Rickgotchi uses PNG faces, so your config must enable `ui.faces.png = true`. The complete reusable block lives in:

```bash
config/faces.toml
```

All character packs use the same face filenames, so you do not need to change the config when switching characters. Just reinstall another pack.

## Development

Generated assets are reproducible:

```bash
python3 scripts/generate_character_faces.py
python3 scripts/build_voice_files.py
```

`characters.json` is the source of truth for available packs and voice languages.

## Responsible Use

Use Rickgotchi only on networks and devices you own or are explicitly allowed to test.
