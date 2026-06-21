.PHONY: build-voices test

build-voices:
	python3 scripts/build_voices.py

test:
	python3 tests/test_assets.py
	python3 tests/test_voice_api.py
	python3 -m py_compile rick-sanchez/voice.py morty-smith/voice.py pickle-rick/voice.py scripts/build_voices.py
