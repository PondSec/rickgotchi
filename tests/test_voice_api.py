#!/usr/bin/env python3
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Peer:
    def __init__(self, first=True):
        self._first = first

    def first_encounter(self):
        return self._first

    def name(self):
        return "unit-test-peer"


class LastSession:
    duration_human = "12 minutes"
    deauthed = 3
    associated = 4
    handshakes = 2
    peers = 1


def load_voice(path):
    spec = importlib.util.spec_from_file_location("voice_under_test", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.Voice


def assert_line(value, context):
    assert isinstance(value, str), context
    assert value.strip(), context
    assert "{" not in value and "}" not in value, f"{context}: unresolved placeholder in {value!r}"


def exercise_voice(voice):
    callbacks = [
        ("custom", lambda: voice.custom("custom line")),
        ("default", voice.default),
        ("on_starting", voice.on_starting),
        ("on_ai_ready", voice.on_ai_ready),
        ("on_keys_generation", voice.on_keys_generation),
        ("on_normal", voice.on_normal),
        ("on_free_channel", lambda: voice.on_free_channel(6)),
        ("on_reading_logs_start", lambda: voice.on_reading_logs(0)),
        ("on_reading_logs_progress", lambda: voice.on_reading_logs(42)),
        ("on_bored", voice.on_bored),
        ("on_motivated", lambda: voice.on_motivated(1.5)),
        ("on_demotivated", lambda: voice.on_demotivated(-1.0)),
        ("on_sad", voice.on_sad),
        ("on_angry", voice.on_angry),
        ("on_excited", voice.on_excited),
        ("on_new_peer_first", lambda: voice.on_new_peer(Peer(True))),
        ("on_new_peer_known", lambda: voice.on_new_peer(Peer(False))),
        ("on_lost_peer", lambda: voice.on_lost_peer(Peer(False))),
        ("on_miss", lambda: voice.on_miss("target-ap")),
        ("on_grateful", voice.on_grateful),
        ("on_lonely", voice.on_lonely),
        ("on_napping", lambda: voice.on_napping(10)),
        ("on_shutdown", voice.on_shutdown),
        ("on_awakening", voice.on_awakening),
        ("on_waiting", lambda: voice.on_waiting(5)),
        ("on_assoc", lambda: voice.on_assoc({"hostname": "test-ap", "mac": "00:11:22:33:44:55"})),
        ("on_assoc_hidden", lambda: voice.on_assoc({"hostname": "<hidden>", "mac": "00:11:22:33:44:55"})),
        ("on_deauth", lambda: voice.on_deauth({"mac": "aa:bb:cc:dd:ee:ff"})),
        ("on_handshakes", lambda: voice.on_handshakes(2)),
        ("on_unread_messages", lambda: voice.on_unread_messages(2, 5)),
        ("on_rebooting", voice.on_rebooting),
        ("on_uploading", lambda: voice.on_uploading("grid")),
        ("on_downloading", lambda: voice.on_downloading("payload")),
        ("on_last_session_data", lambda: voice.on_last_session_data(LastSession())),
        ("on_last_session_tweet", lambda: voice.on_last_session_tweet(LastSession())),
        ("hhmmss_h", lambda: voice.hhmmss(2, "h")),
        ("hhmmss_m", lambda: voice.hhmmss(1, "m")),
        ("hhmmss_s", lambda: voice.hhmmss(2, "s")),
    ]

    for name, callback in callbacks:
        assert_line(callback(), name)


def main():
    manifest = json.loads((ROOT / "characters.json").read_text())
    for character in manifest["characters"]:
        voice_cls = load_voice(ROOT / character["voice"])
        for lang in character["voice_languages"]:
            for _ in range(10):
                exercise_voice(voice_cls(lang))


if __name__ == "__main__":
    main()

