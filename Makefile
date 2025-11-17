PYTHON ?= python

.PHONY: install test score index swarm all

install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

test:
	pytest -q

score:
	$(PYTHON) scripts/asset_scoring.py

index:
	$(PYTHON) scripts/generate_assets_index.py --input output/asset_scores.csv --output output/Assets.current.md

swarm:
	$(PYTHON) ai/run.py

all: score index test swarm
