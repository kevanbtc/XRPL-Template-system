from pathlib import Path
import sys
import os


# Ensure ai/src is importable like ai/run.py does
ROOT = Path(__file__).resolve().parents[1]
AI_SRC = ROOT / "ai" / "src"
if str(AI_SRC) not in sys.path:
    sys.path.insert(0, str(AI_SRC))

from config import Config  # type: ignore


def test_policy_loading_from_config_dir():
    # Ensure policy loads from repo_root/config/ai_policy.yaml (mirrored)
    cfg = Config.from_env()

    # Dry-run should default to True for safety (unless overridden by env)
    assert cfg.dry_run is True

    # Allowed buckets should include Immediate and Near-Term from policy
    assert isinstance(cfg.allowed_buckets, (list, tuple))
    assert ("Immediate" in cfg.allowed_buckets) or (
        "Immediate" in list(cfg.allowed_buckets)
    )
    assert ("Near-Term" in cfg.allowed_buckets) or (
        "Near-Term" in list(cfg.allowed_buckets)
    )

    # Numeric thresholds mapped from policy
    assert cfg.min_score == 70
    assert cfg.min_net_bps == 5
    assert cfg.max_trades == 5


def test_env_overrides_dry_run_false():
    try:
        os.environ["AI_DRY_RUN"] = "false"
        cfg = Config.from_env()
        assert cfg.dry_run is False
    finally:
        os.environ.pop("AI_DRY_RUN", None)
