# Bank Filings — Master Page Template

> Purpose: Publish a regulator-safe snapshot of reserves, facilities, and collateral candidates. Only count verified, enforceable assets in headline totals.

## On-Ledger XRPL Reserves

These on-ledger balances represent only assets that have cleared our RWA intake and verification pipeline. More complex or speculative assets are disclosed separately and are not counted in this total.

- Issuer: [XRPL_ADDRESS_ISSUER]
- Treasury: [XRPL_ADDRESS_TREASURY]
- External Reserve Portfolio: [XRPL_ADDRESS_RESERVES]
- Multi-currency IOUs: [CURRENCIES_LIST]

Status: [TOTAL_RESERVES_USD] verified on-ledger reserves.

Evidence:
- Tranche hashes: [IPFS_CID_TRANCHES]
- Statements & capacity letters (if any): [IPFS_CID_BANK_DOCS]

## Off-Ledger Banking & Facilities

### [BANK_NAME] Account & Instruments (PoF Layer)
- Account ownership certificates: [DOC_REF] confirming [IBAN] for [ACCOUNT_HOLDER]
- Instruments: [COUNT] × [TYPE] of [NOMINAL] each; nature/blocked status under verification
- Treatment: classified as pledged collateral — bank confirmation pending; excluded from headline reserves

If/when confirmed — “[BANK_NAME] Facility I”
- Facility size: [AMOUNT]
- Instrument: [Loan/SBLC/BG]
- LTV vs instrument batch: [PCT]
- Utilization: [stablecoin/notes/credit]
- Daily Proof-of-Reserves (oracle feed) and docs to IPFS

## RWA Collateral Candidates (not counted yet)

### [ASSET_NAME] — Vault [VAULT_ID]
- Appraiser/source: [APPRAISER] ([DATE])
- Reported value: [VALUATION_CCY_AMOUNT]
- Documentation: [DOC_LIST] (IPFS CID: [CID])
- Status: [VERIFICATION_STATUS]
- Treatment: excluded from reserve totals until [CONDITION]; expected conservative LTV [LTV_RANGE]

## Legacy / Speculative Inventory (0% LTV)

### [ASSET_NAME] — Vault [VAULT_ID]
- Evidence: [EVIDENCE_SUMMARY]
- Status: [STATUS_SUMMARY]
- Treatment: speculative/collectible inventory; zero collateral value in reserve calculations

## Corporate Treasury Layer (IP)

Unykorn operates a multi-chain financial OS (L1/L2 networks; TLD registries; ERC-6551 vaults; token suites; compliance/escrow engines), documented via Genesis certificates and IPFS.

- Summary of IP scope: [SCOPE]
- Appraisal posture: base valuation in tens of millions; strategic upside higher; independent memo: [LINK/ETA]
- Use: licensable, pledgeable, or partially securitizable. Unless otherwise stated, IP value is not included in "Total Reserves".

## Disclosures
- Only Tier-1 verified assets and confirmed facilities back reserves
- Tier-2/3 assets are disclosed but assigned 0% LTV until verified
- All filings time-stamped and CID-linked for audit
