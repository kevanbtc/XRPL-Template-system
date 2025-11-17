
from pathlib import Path
import sys
import os

# Ensure ai/src is importable
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / " ai\ / \src\))

from config import Config

def test_policy_loading_from_repo_root_config():
 cfg = Config.from_env()
 # Policy keys from config/ai_policy.yaml
 assert isinstance(cfg.allowed_buckets, tuple)
 assert \Immediate\ in cfg.allowed_buckets
 assert cfg.risk.get(\min_score\) == 70
 assert cfg.min_score == 70
 assert cfg.min_net_bps == 5
 assert cfg.max_trades == 5
 assert cfg.dry_run is True

def test_env_overrides_dry_run_false():
 try:
 os.environ[\AI_DRY_RUN\] = \false\
 cfg = Config.from_env()
 assert cfg.dry_run is False
 finally:
 os.environ.pop(\AI_DRY_RUN\, None)
