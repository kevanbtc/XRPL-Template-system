# Santander Facility — Technical Implementation (Template)

## Architecture Rings
1. Bank World: banker statements/letters (PDF/PGP)
2. Verification: Proof Server (FastAPI/Express), S3 encryption, Postgres
3. Oracle: Chainlink EA + job (cron), freshness checks
4. On-chain: Oracle feed + FacilityRegistry + Pool (mint caps)

## Proof Server
- Endpoints: POST /uploadStatement, GET /latestProof
- Security: API key, IP allowlist, PGP verification, AES-256 S3
- Tables: statements, verifications, audit_logs

## External Adapter (Node.js)
- Flow: fetch proof → validate freshness → scale → return
- Security: API key, rate limit, IP allowlist

## Contracts
- Oracle: facilityAvailable (1e18 scaled), lastUpdated, onlyOracle update()
- FacilityRegistry: cap, minCollateralRatio, oracleFeed, getUsableCapacity()
- Pool: mint() checks capacityUSD * safety margin

## Ops
- Daily: banker upload → proof ingest → oracle update → auto caps
- Weekly: proof bundle + IPFS; alarms review
- Monthly: compliance review; RM check-in
- Emergencies: oracle failover; mint freeze; wind-down
