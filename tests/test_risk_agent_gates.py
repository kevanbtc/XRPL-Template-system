import sys
from pathlib import Path

# Add ai/src to path like ai/run.py
ROOT = Path(__file__).resolve().parents[1]
AI_SRC = ROOT / "ai" / "src"
if str(AI_SRC) not in sys.path:
    sys.path.insert(0, str(AI_SRC))

from agents.risk_agent import RiskAgent  # type: ignore

from config import Config  # type: ignore


def _cfg(
    min_score=70.0,
    min_net_bps=5.0,
    allowed_buckets=("Immediate", "Near-Term"),
):
    cfg = Config.from_env()
    cfg.min_score = min_score
    cfg.min_net_bps = min_net_bps
    cfg.allowed_buckets = tuple(allowed_buckets)
    return cfg


def test_risk_agent_accepts_good_opportunity():
    cfg = _cfg()
    agent = RiskAgent(cfg)
    state = {
        "market_opps": [
            {
                "asset": "ASSET_X",
                "score": 80,
                "bucket": "Immediate",
                "net_bps": 6.0,
                "direction": "buy",
            }
        ]
    }
    out = agent.step(state)
    payload = {}
    if hasattr(out, "payload"):
        payload = getattr(out, "payload", {})
    elif isinstance(out, dict):
        payload = out
    approved = payload.get("approved_opps") or state.get("approved_opps", [])
    assert len(approved) == 1
    a0 = approved[0]
    # Dict or object support
    asset = a0.get("asset") if isinstance(a0, dict) else getattr(a0, "asset", None)
    assert asset == "ASSET_X"


def test_risk_agent_rejects_low_score():
    cfg = _cfg(min_score=70.0)
    agent = RiskAgent(cfg)
    state = {
        "market_opps": [
            {
                "asset": "LOW_SCORE",
                "score": 50,
                "bucket": "Immediate",
                "net_bps": 10.0,
                "direction": "buy",
            }
        ]
    }
    out = agent.step(state)
    payload = {}
    if hasattr(out, "payload"):
        payload = getattr(out, "payload", {})
    elif isinstance(out, dict):
        payload = out
    approved = payload.get("approved_opps") or state.get("approved_opps", [])
    assert len(approved) == 0


def test_risk_agent_rejects_wrong_bucket():
    cfg = _cfg()
    agent = RiskAgent(cfg)
    state = {
        "market_opps": [
            {
                "asset": "REJECTED_BUCKET",
                "score": 90,
                "bucket": "Reject",
                "net_bps": 12.0,
                "direction": "buy",
            }
        ]
    }
    out = agent.step(state)
    payload = {}
    if hasattr(out, "payload"):
        payload = getattr(out, "payload", {})
    elif isinstance(out, dict):
        payload = out
    approved = payload.get("approved_opps") or state.get("approved_opps", [])
    assert len(approved) == 0
