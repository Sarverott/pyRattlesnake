#!/bin/sh

uv sync
uv lock
uv export --no-dev --format requirements.txt -o ./requirements.txt
uv export --no-dev --format pylock.toml -o ./pylock.toml