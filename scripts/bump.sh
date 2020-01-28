#!/usr/bin/env bash
set -e
poetry version $(gitsemver)
git add pyproject.toml
git commit -m "[skip ci]: bump"
git push
