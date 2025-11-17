# Reject Log (Dogshit Filter)

Only log assets that we intentionally stop working on. Be blunt. If facts change, create a new intake and reference this log.

## Auto-Reject Triggers

- TTC == 0 (no credible path to cash)
- VF <= 1 (no verification)
- CC <= 1 (counterparty/compliance unacceptable)
- LD <= 1 and LTV <= 1 (no demand and no value)

## Log

| Date       | Asset                | Trigger(s)                         | One-line reason                          | Owner | Notes/Link |
|------------|----------------------|------------------------------------|------------------------------------------|-------|------------|
| YYYY-MM-DD | [Asset name]         | [e.g., VF<=1, TTC==0]              | [e.g., unverifiable title]               | [me]  | [link]     |
| YYYY-MM-DD | [Asset name]         | [e.g., LD<=1 and LTV<=1]           | [e.g., no buyers + poor economics]       | [me]  | [link]     |

## Rescue Checklist (only if facts change)

- [ ] New evidence lifts VF/CC over threshold (documented)
- [ ] New counterparty path with credible buyer/lender
- [ ] Structure changed to address blocker (collateral, terms)
- [ ] Re-scored and passes gates; approved for re-intake
