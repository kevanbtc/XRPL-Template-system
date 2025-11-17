# AI Swarm (MCP-friendly) – Liquidity & Trading Assist

This module gives you a small, self-contained **multi-agent (swarm)** that knows about your scoring outputs and can propose liquidity/arb actions. It runs locally with no keys by default (dry-run), and is structured so you can plug real connectors later.

- No external dependencies required for the basic demo.
- Reads `output/asset_scores.csv` to prioritize Immediate/Near-Term assets.
- Mock market data agent detects simple price deltas between two venues.
- Risk agent applies reject/gating discipline before proposing actions.
- Trader agent emits dry-run orders (no network).

## Layout

```text
ai/
  README.md
  run.py                  # Run the swarm locally (dry-run)
  src/
    config.py
    swarm.py              # Orchestrator and agent base
    agents/
      scoring_agent.py
      market_agent.py
      risk_agent.py
      trader_agent.py
    tools/
      scoring_reader.py
  tests/
    test_swarm.py
```

## Quickstart (dry-run)

```powershell
# From repo root
python ai/run.py
```

### What you'll see

- The scoring agent loading top assets
- The market agent simulating prices and a potential delta
- The risk agent accepting/rejecting
- The trader agent emitting a dry-run plan

## Extending to real connectors (optional)

- DEX / XRPL: add a real XRPL client in `tools/` using `xrpl-py` and an AMM router.
- CEX: add a connector (e.g., CCXT) for read-only price discovery first.
- Keys: put them in environment variables and load in `config.py` (never commit).

## Notes

- This is a planning tool, not an offering. All actions require legal/compliance review.
- Keep the **Reject/Dogshit** discipline in place — the swarm respects the gates.
