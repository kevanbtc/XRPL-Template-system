# Daily Proof-of-Reserves & Oracle Runbook (Template)

Objective: Ensure reserve data is fresh, signed, and on-chain.

## Sources of Truth
- Banker/appraiser statements (PDF/email signed/PGP)
- Proof Server API: /latestProof (freshness window < [HOURS])
- Oracle job: [CRON_SPEC]

## Daily Checklist
- [ ] Banker/appraiser doc received and ingested
- [ ] Proof Server verification passed; hash committed
- [ ] Oracle job executed; on-chain timestamp < [HOURS]
- [ ] IPFS bundle CID updated and pinned
- [ ] Dashboard reflects latest capacity and caps

## Alerts
- Stale data (> [HOURS])
- Oracle failure/exception
- Hash mismatch between Proof Server and on-chain feed

## Remediation
- Re-run adapter; rotate API key if 4xx; failover node if 5xx
- Manual update via multisig (only within emergency policy)
- Notify stakeholders; attach incident CID to daily report
