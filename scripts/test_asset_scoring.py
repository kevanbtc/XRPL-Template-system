import json
from pathlib import Path

# Import functions from asset_scoring by path manipulation if needed
import importlib.util, sys
SCRIPT_PATH = Path(__file__).parent / 'asset_scoring.py'
spec = importlib.util.spec_from_file_location('asset_scoring', str(SCRIPT_PATH))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)  # type: ignore

ROOT = Path(__file__).resolve().parent.parent

weights_doc = mod.strip_jsonc(ROOT / 'docs' / 'templates' / 'scoring' / 'AssetScoringWeights.jsonc')
assets = json.loads((ROOT / 'data' / 'assets.json').read_text(encoding='utf-8'))

scored = mod.compute_scores(assets, weights_doc)

# Basic assertions
names = {r['name']: r for r in scored}

# Top should include Unykorn and be Immediate
assert 'Unykorn IP Licensing' in names, 'Missing Unykorn asset'
assert names['Unykorn IP Licensing']['bucket'] == 'Immediate', 'Unykorn should be Immediate'

# Rejects should include IQD and Historic Chinese Bonds
assert names['IQD Boxes']['bucket'] == 'Reject', 'IQD Boxes should be Reject'
assert names['Historic Chinese Bonds']['bucket'] == 'Reject', 'Historic Chinese Bonds should be Reject'

print('All tests passed.')
