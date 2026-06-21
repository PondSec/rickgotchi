#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage:
  scripts/install-character.sh <character-slug>

Examples:
  scripts/install-character.sh rick-sanchez
  scripts/install-character.sh jerry-smith

Optional:
  PWNAGOTCHI_VOICE_PATH=/exact/path/to/pwnagotchi/voice.py scripts/install-character.sh beth-smith
USAGE
}

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
character="${1:-}"

if [[ -z "$character" || "$character" == "-h" || "$character" == "--help" ]]; then
  usage
  exit 0
fi

character_dir="$repo_root/$character"
faces_dir="$character_dir/custom-faces"
voice_file="$character_dir/voice.py"

if [[ ! -d "$faces_dir" || ! -f "$voice_file" ]]; then
  echo "Unknown or incomplete character pack: $character" >&2
  echo "Available packs:" >&2
  find "$repo_root" -maxdepth 2 -type f -name voice.py -print \
    | sed "s#^$repo_root/##; s#/voice.py##" \
    | sort >&2
  exit 1
fi

find_voice_path() {
  if [[ -n "${PWNAGOTCHI_VOICE_PATH:-}" ]]; then
    printf '%s\n' "$PWNAGOTCHI_VOICE_PATH"
    return
  fi

  sudo find / -path '*/pwnagotchi/voice.py' -print -quit 2>/dev/null
}

voice_path="$(find_voice_path)"

if [[ -z "$voice_path" ]]; then
  echo "Could not find pwnagotchi/voice.py." >&2
  echo "Try: sudo find / -name voice.py 2>/dev/null" >&2
  echo "Then rerun with PWNAGOTCHI_VOICE_PATH=/the/path/voice.py" >&2
  exit 1
fi

if [[ ! -f "$voice_path" ]]; then
  echo "Resolved voice.py path does not exist: $voice_path" >&2
  exit 1
fi

timestamp="$(date +%Y%m%d-%H%M%S)"
backup_path="$voice_path.rickgotchi-backup-$timestamp"

echo "Installing character: $character"
echo "Using Pwnagotchi voice path: $voice_path"

sudo mkdir -p /custom-faces
sudo rm -rf /custom-faces/*
sudo cp -a "$faces_dir"/. /custom-faces/

sudo cp "$voice_path" "$backup_path"
sudo cp "$voice_file" "$voice_path"

echo "Faces installed to /custom-faces"
echo "Voice installed to $voice_path"
echo "Backup saved to $backup_path"
echo "Set main.lang to one of: en, de, es, fr, it, pt, pt_BR"
