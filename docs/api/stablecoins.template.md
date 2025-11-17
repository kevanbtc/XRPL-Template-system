# Stablecoins API — Template

Purpose: Define how stablecoin issuance/redemption respects facility caps and PoR.

## Concepts
- Facility-backed capacity from FacilityRegistry (oracle-fed)
- Safety margin (e.g., 90%) over capacity for mint caps
- Freshness checks on oracle data (e.g., < 36h)

## Endpoints (example)
- GET /capacity — returns usableCapacityUSD, lastUpdated
- POST /mint — amount, checks caps/freshness; emits tx hash on XRPL/EVM
- POST /redeem — amount, processes burn/redemption path

## Errors
- STALE_ORACLE: data older than threshold
- CAP_EXCEEDED: requested mint exceeds cap
- FACILITY_INACTIVE: paused/terminated facility

## Events
- CapacityUpdated(capacityUSD, timestamp)
- Minted(amount, account)
- Redeemed(amount, account)

## Security
- Auth: [JWT/API key]
- Rate limits by IP and account
- Audit log: request id, actor, result, proof hash
