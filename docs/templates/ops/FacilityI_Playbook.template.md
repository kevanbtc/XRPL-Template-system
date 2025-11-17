# Facility I — Program Playbook (Template)

Objective: Stand up the first confirmed facility (e.g., Santander or Rubies) and wire it into PoR, reserves, and programs.

## Prerequisites
- Executed facility agreement / term sheet
- Dossier CID (legal, bank/appraisal/insurance)
- Parameters: cap [AMOUNT], LTV [PCT], oracle endpoint [URL]

## Contracts & Params
- FacilityRegistry: [ADDRESS] (cap, minCollateralRatio, oracle)
- Oracle feed (e.g., SantanderFacilityFeed): [ADDRESS]
- Stablecoin/Lending pool using facility: [ADDRESS]

## Daily Operations
- Proof Server ingests banker/appraiser confirmations
- Oracle cron updates feed; check freshness < [HOURS]
- Auto-adjust mint caps / redemption windows

## Reporting
- Daily: oracle snapshot + CID bundle
- Weekly: utilization, collateralization, incidents
- Monthly: legal/regulatory attestations

## Emergency Procedures
- Oracle failure → manual override/runbook; switch to backup feed
- Collateralization drop → freeze mint; enable priority redemptions
- Facility termination → orderly wind-down; investor notifications
