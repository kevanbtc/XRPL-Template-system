# Ruby Vault I – Three-Layer Hide-Yet-Prove Architecture

**Document Version:** 1.0  
**Last Updated:** 2025-11-16  
**Asset:** Natural Corundum Ruby Collection  
**Appraiser:** HDG Appraisal Group (Oct 2, 2021, San Diego, CA)  
**Appraised TRV:** $376,753,275 USD  
**SPV:** Ruby Vault I, LLC  
**Vault ID:** `RUBY-HDGR-2021-001`

---

## Executive Summary

This document describes how to structure a **high-value, illiquid RWA** (natural ruby collection) using Unykorn's three-layer architecture:

1. **Layer 1 (Off-Chain):** Prove + insure the physical asset
2. **Layer 2 (XRPL-P):** RWA vault on private ledger with full metadata
3. **Layer 3 (XRPL-M):** Lock stablecoins as visible collateral, issue public instruments

**Result:** Public sees boring, verifiable stablecoin backing. Sophisticated parties get full RWA audit trail. You control all layers.

---

## Part 1: Layer 1 – Prove + Insure (Off-Chain Reality)

### Step 1: Verification Pack Assembly

**Required Documents:**

1. **HDG Appraisal Certificate**
   - Date: Oct 2, 2021
   - Client: Jeremy Lynn White
   - Total Collection Replacement Value: $376,753,275
   - Individual stone details: GIA report numbers, carats, measurements, TRV per stone

2. **Updated Appraisal** (if available)
   - Confirm HDG is real, licensed, reachable
   - Verify certificate in their records
   - Ideally: second opinion from another certified appraiser
   - If >2 years old, recommend reappraisal

3. **GIA Laboratory Reports**
   - Match each GIA report number from HDG certificate
   - Confirm stone authenticity, treatments, enhancements
   - Store PDF copies of all reports

4. **Custody Documentation**
   - Vault contract: where rubies physically stored
   - Vault company: name, address, license
   - Inventory receipt: dated, signed, itemized
   - Access control: who can retrieve stones
   - Audit rights: periodic physical verification

5. **Insurance Policy**
   - Named insured: Ruby Vault I, LLC (or your SPV)
   - Coverage amount: match or exceed $376.7M appraised value
   - Insurer: Lloyds of London, Chubb, or comparable
   - Policy term, conditions, exclusions
   - Loss payee: lenders/investors if applicable

6. **Chain of Title**
   - Who owns the stones: I.B.E. International Business Enterprise Inc.
   - JV + Assignment Agreement: FollowMe Global Business Solutions LLC has monetization rights
   - Term: 24 months from agreement date
   - Revenue split: 50% Jason Slaughter / 50% Theophilus Depona
   - Further assignment rights: confirm you can pledge to SPV

7. **Legal Clean-up**
   - UCC search: no prior liens
   - Export/import compliance: if stones crossed borders
   - Sanctions screening: all beneficial owners
   - Right to pledge/hypothecate: confirmed in writing

### Step 2: Create SPV Structure

**SPV Formation:**

```
Entity Name: Ruby Vault I, LLC
Jurisdiction: Delaware (or Wyoming, Cayman)
Purpose: Hold monetization rights and security interest in ruby collection
Manager: Unykorn Real Assets Management, LLC
Members: [specify ownership structure]

Operating Agreement Provisions:
- SPV is bankruptcy-remote
- Single-purpose: ruby collection only
- All proceeds flow through SPV accounts
- Lenders have first-priority security interest
- No commingling with other assets
```

**Assignment of Rights to SPV:**

```
ASSIGNMENT AND PLEDGE AGREEMENT

This Agreement dated [DATE], between:
- Assignor: FollowMe Global Business Solutions LLC
- Assignee: Ruby Vault I, LLC

Assignor hereby assigns and pledges to Assignee:
- All monetization rights under JV Agreement dated [DATE]
- Security interest in natural corundum ruby collection
- All proceeds, revenue, and claims related thereto

Assignee shall:
- Hold rubies (or rights thereto) for benefit of Lenders
- Enforce all rights under JV Agreement
- Distribute proceeds per waterfall in Credit Agreement

First-Priority Security Interest granted to Lenders.
```

### Step 3: Bundle + Hash All Documents

**Document Package:**

```
RUBY-VAULT-I-DOCS/
├── 01_HDG_Appraisal_Certificate_2021-10-02.pdf
├── 02_Updated_Appraisal_[if_available].pdf
├── 03_GIA_Reports/
│   ├── GIA_Report_[number1].pdf
│   ├── GIA_Report_[number2].pdf
│   └── ... (all individual stones)
├── 04_Custody_Vault_Contract.pdf
├── 05_Custody_Inventory_Receipt.pdf
├── 06_Insurance_Policy_Lloyds.pdf
├── 07_Chain_of_Title/
│   ├── IBE_Ownership_Docs.pdf
│   ├── JV_Agreement_FollowMe.pdf
│   └── Assignment_to_SPV.pdf
├── 08_UCC_Search_Results.pdf
├── 09_Legal_Opinion_Pledge_Rights.pdf
└── 10_SPV_Operating_Agreement.pdf
```

**Generate Archive:**
```bash
# Create tar.gz bundle
tar -czf ruby-vault-i-docs.tar.gz RUBY-VAULT-I-DOCS/

# Calculate SHA-256 hash
sha256sum ruby-vault-i-docs.tar.gz
# Output: a1b2c3d4e5f6...

# Sign with PGP key
gpg --sign --armor ruby-vault-i-docs.tar.gz
# Output: ruby-vault-i-docs.tar.gz.asc
```

**Pin to IPFS:**
```bash
ipfs add ruby-vault-i-docs.tar.gz
# Output: QmRubyVaultIDocs20251116abcdef...

# Store signature separately
ipfs add ruby-vault-i-docs.tar.gz.asc
# Output: QmRubyVaultIDocsSig20251116xyz...
```

**Result:**
- **Bundle CID:** `QmRubyVaultIDocs20251116abcdef...`
- **Signature CID:** `QmRubyVaultIDocsSig20251116xyz...`
- **SHA-256 Hash:** `a1b2c3d4e5f6...` (to be committed on-chain)

---

## Part 2: Layer 2 – RWA Vault on Private Ledger (XRPL-P)

### Step 1: Define Vault Metadata Schema

**Vault NFT Metadata:**
```json
{
  "vault_id": "RUBY-HDGR-2021-001",
  "asset_type": "Natural corundum rough ruby collection",
  "appraiser": "HDG Appraisal Group",
  "appraiser_location": "San Diego, CA",
  "appraisal_date": "2021-10-02",
  "appraised_trv_usd": 376753275,
  
  "haircut_policy": {
    "reason": "Illiquidity, authenticity risk, enforcement complexity",
    "haircut_pct": 80,
    "eligible_collateral_usd": 75350655,
    "policy_date": "2025-11-16"
  },
  
  "ltv_policy": {
    "max_ltv_pct": 40,
    "max_facility_usd": 30140262,
    "rationale": "Conservative lending against exotic collateral"
  },
  
  "spv": {
    "entity_name": "Ruby Vault I, LLC",
    "jurisdiction": "Delaware",
    "formation_date": "2025-11-15",
    "manager": "Unykorn Real Assets Management, LLC",
    "purpose": "Hold monetization rights + security interest in ruby collection"
  },
  
  "custody": {
    "vault_company": "[Name]",
    "vault_location": "[City, State/Country]",
    "inventory_receipt_date": "[DATE]",
    "access_control": "Dual-signature required for withdrawal"
  },
  
  "insurance": {
    "insurer": "Lloyds of London",
    "policy_number": "[POLICY#]",
    "coverage_usd": 376753275,
    "named_insured": "Ruby Vault I, LLC",
    "loss_payee": "Lenders per Credit Agreement",
    "policy_term": "2025-11-15 to 2026-11-15"
  },
  
  "legal_rights": {
    "original_owner": "I.B.E. International Business Enterprise Inc.",
    "monetization_rights_holder": "FollowMe Global Business Solutions LLC",
    "jv_agreement_date": "[DATE]",
    "jv_term_months": 24,
    "revenue_split": "50% Jason Slaughter / 50% Theophilus Depona",
    "assignment_to_spv": "2025-11-15",
    "security_interest": "First-priority lien in favor of Lenders",
    "ucc_filing": "[UCC filing number + date]"
  },
  
  "documentation": {
    "ipfs_bundle_cid": "QmRubyVaultIDocs20251116abcdef...",
    "ipfs_signature_cid": "QmRubyVaultIDocsSig20251116xyz...",
    "sha256_hash": "a1b2c3d4e5f6...",
    "document_count": 15,
    "last_updated": "2025-11-16"
  },
  
  "risk_assessment": {
    "risk_tier": "Tier-2-RWA",
    "liquidity_score": 2.5,
    "authenticity_score": 8.5,
    "legal_clarity_score": 7.0,
    "enforcement_score": 6.0,
    "overall_risk": "Medium-High",
    "notes": "High value but illiquid; requires specialist buyer; legal structure clean"
  },
  
  "facility_status": {
    "current_outstanding": 0,
    "max_approved": 30140262,
    "current_ltv_pct": 0,
    "last_drawdown_date": null,
    "next_appraisal_due": "2027-10-02"
  }
}
```

### Step 2: Mint Vault NFT on XRPL-P

**Prerequisites:**
- XRPL-P cluster running
- Private client connected
- SPV account created on XRPL-P: `rRubyVaultI...`

**Python Code:**
```python
from xrpl.clients import JsonRpcClient
from xrpl.models.transactions import NFTokenMint
from xrpl.wallet import Wallet
from xrpl.transaction import submit_and_wait
import xrpl.utils
import json

# Connect to private ledger
private_client = JsonRpcClient("https://10.0.20.5:5005")

# SPV wallet (cold storage for security, hot wallet for operations)
spv_wallet = Wallet(seed="s...", sequence=0)  # Load from secure storage

# Prepare vault metadata
vault_metadata = {
    "vault_id": "RUBY-HDGR-2021-001",
    "asset_type": "Natural corundum rough ruby collection",
    # ... (full metadata from above)
}

# Convert to hex for URI field
metadata_json = json.dumps(vault_metadata, sort_keys=True)
metadata_hex = xrpl.utils.str_to_hex(metadata_json)

# Mint Vault NFT
mint_tx = NFTokenMint(
    account=spv_wallet.classic_address,
    nftoken_taxon=1,  # Taxon 1 = RWA Vaults
    flags=8,  # Transferable (0x0008)
    uri=metadata_hex
)

# Submit to private ledger
response = submit_and_wait(mint_tx, private_client, spv_wallet)

# Extract NFT ID
nft_id = response.result['meta']['nftoken_id']
print(f"Vault NFT Minted: {nft_id}")

# Store NFT ID in database
vault_record = {
    "vault_id": "RUBY-HDGR-2021-001",
    "xrpl_p_nft_id": nft_id,
    "xrpl_p_account": spv_wallet.classic_address,
    "created_at": datetime.now(),
    "status": "active"
}
db.vaults.insert(vault_record)
```

**Result:**
- Vault NFT created on XRPL-P
- Full metadata stored on-chain (private)
- NFT ID: `000B0139...` (unique identifier)
- Only accessible via private ledger (not visible on mainnet)

### Step 3: Update Vault NFT Metadata (As Needed)

**When to Update:**
- New appraisal obtained → update `appraised_trv_usd`, `appraisal_date`
- Insurance renewed → update `insurance.policy_term`
- Facility drawn → update `facility_status.current_outstanding`, `current_ltv_pct`
- Documents updated → re-bundle, re-pin to IPFS, update CIDs

**Update Process:**
- XRPL NFTs are immutable once minted
- To "update," mint new version with updated metadata
- Mark old version as superseded
- Or: use memos on separate transactions to record updates

**Alternative: Memo-Based Updates**
```python
# Send self-payment with memo containing update
update_tx = Payment(
    account=spv_wallet.classic_address,
    destination=spv_wallet.classic_address,
    amount="1",  # 1 drop XRP
    memos=[{
        "Memo": {
            "MemoType": xrpl.utils.str_to_hex("vault_update"),
            "MemoData": xrpl.utils.str_to_hex(json.dumps({
                "vault_nft_id": nft_id,
                "field": "facility_status.current_outstanding",
                "old_value": 0,
                "new_value": 10000000,
                "reason": "First drawdown - $10M facility activated",
                "timestamp": "2025-11-20T10:30:00Z"
            }))
        }
    }]
)
submit_and_wait(update_tx, private_client, spv_wallet)
```

---

## Part 3: Layer 3 – Lock Stablecoins + Issue Public Instruments (XRPL-M)

### Design Pattern: Stablecoin-Backed Bonds/NFTs with RWA Underneath

**Goal:** Public investors see simple, verifiable stablecoin collateral. Sophisticated parties can trace back to ruby RWA backing.

### Step 1: Create Ruby Reserve Account on XRPL-M

**Setup:**
```python
from xrpl.clients import JsonRpcClient
from xrpl.wallet import generate_faucet_wallet, Wallet
from xrpl.models.transactions import AccountSet, TrustSet, Payment

# Connect to public mainnet
public_client = JsonRpcClient("https://54.x.x.x:5005")

# Create dedicated reserve account
# In production: use multi-sig or cold wallet
ruby_reserve_wallet = Wallet(seed="s...", sequence=0)  # rRubyReserves...

# Set account flags (require destination tag, etc.)
account_set_tx = AccountSet(
    account=ruby_reserve_wallet.classic_address,
    set_flag=1  # RequireDest (optional, for tracking)
)
submit_and_wait(account_set_tx, public_client, ruby_reserve_wallet)

# Establish trust lines for stablecoins
currencies = ["FTHUSD", "USDF", "USDT", "TGUSD"]
for currency in currencies:
    trust_tx = TrustSet(
        account=ruby_reserve_wallet.classic_address,
        limit_amount={
            "currency": currency,
            "issuer": ISSUER_ACCOUNTS[currency],
            "value": "100000000"  # 100M limit
        }
    )
    submit_and_wait(trust_tx, public_client, ruby_reserve_wallet)

print(f"Ruby Reserve Account: {ruby_reserve_wallet.classic_address}")
```

**Result:**
- Public account: `rRubyReserves...`
- Trust lines established for major stablecoins
- Anyone can verify balance on public explorer

### Step 2: Lock Stablecoins in Reserve Account

**Decision: How Much to Lock?**

Conservative approach:
- Appraised value: $376.7M
- Haircut (80%): $75.4M eligible collateral
- Max facility (40% LTV): $30.1M
- **Lock amount: $30-35M stablecoins**

This provides:
- 1:1 coverage of maximum facility
- Buffer for price fluctuations
- Clear public proof of backing

**Lock Transaction:**
```python
# From treasury, send stablecoins to reserve account
lock_tx = Payment(
    account=TREASURY_ACCOUNT,
    destination=ruby_reserve_wallet.classic_address,
    amount={
        "currency": "FTHUSD",
        "issuer": FTHUSD_ISSUER,
        "value": "30000000"  # $30M FTHUSD
    },
    memos=[{
        "Memo": {
            "MemoType": xrpl.utils.str_to_hex("reserve_lock"),
            "MemoData": xrpl.utils.str_to_hex(json.dumps({
                "vault_id": "RUBY-HDGR-2021-001",
                "purpose": "Stablecoin backing for Ruby Vault I bonds",
                "lock_date": "2025-11-16",
                "unlock_conditions": "Burn of all RUBY1-BOND tokens or facility termination"
            }))
        }
    }]
)
submit_and_wait(lock_tx, public_client, treasury_wallet)
```

**Update XRPL-P Vault Record:**
```python
# On private ledger, record backing relationship
backing_memo_tx = Payment(
    account=spv_wallet.classic_address,
    destination=spv_wallet.classic_address,
    amount="1",
    memos=[{
        "Memo": {
            "MemoType": xrpl.utils.str_to_hex("stablecoin_backing"),
            "MemoData": xrpl.utils.str_to_hex(json.dumps({
                "vault_nft_id": nft_id,
                "backing_account": ruby_reserve_wallet.classic_address,
                "backing_currency": "FTHUSD",
                "backing_amount": 30000000,
                "backing_tx_hash": lock_tx_result["hash"],
                "timestamp": "2025-11-16T12:00:00Z"
            }))
        }
    }]
)
submit_and_wait(backing_memo_tx, private_client, spv_wallet)
```

**Result:**
- $30M FTHUSD locked in `rRubyReserves...` (public, verifiable)
- XRPL-P records relationship: "this reserve backs vault RUBY-HDGR-2021-001"
- Two-way link established

### Step 3: Issue Public Instruments

**Option A: Ruby Reserve Bonds (Fixed Income)**

**Structure:**
- Mint bond NFTs representing senior secured notes
- Each NFT = $100k face value
- Total: 300 NFTs × $100k = $30M
- Maturity: 36 months
- Coupon: 12% annual (paid quarterly)
- Security: 1st lien on stablecoins in `rRubyReserves...`
- Ultimate backing: ruby collection (disclosed in docs)

**Mint Bond NFTs:**
```python
# Define bond series
bond_series = {
    "series_id": "RUBY1-BOND-2025",
    "face_value": 100000,
    "quantity": 300,
    "coupon_rate": 0.12,
    "coupon_frequency": "quarterly",
    "maturity_date": "2028-11-16",
    "security": "First lien on FTHUSD in rRubyReserves...",
    "ultimate_collateral": "Natural ruby collection held by Ruby Vault I, LLC"
}

# Mint NFTs for each bond
for i in range(1, 301):
    bond_metadata = {
        "series": bond_series["series_id"],
        "bond_number": i,
        "face_value": 100000,
        "coupon_rate": 0.12,
        "maturity_date": "2028-11-16",
        "reserve_account": ruby_reserve_wallet.classic_address,
        "vault_reference": "RUBY-HDGR-2021-001",
        "ipfs_offering_docs": "QmRubyBondOffering2025...",
        "issuer": "Ruby Vault I, LLC",
        "issue_date": "2025-11-16"
    }
    
    bond_nft_tx = NFTokenMint(
        account=BOND_ISSUER_ACCOUNT,
        nftoken_taxon=2,  # Taxon 2 = Bonds
        uri=xrpl.utils.str_to_hex(json.dumps(bond_metadata))
    )
    
    response = submit_and_wait(bond_nft_tx, public_client, issuer_wallet)
    bond_nft_id = response.result['meta']['nftoken_id']
    
    # Store in database
    db.bonds.insert({
        "bond_number": i,
        "nft_id": bond_nft_id,
        "status": "issued",
        "holder": None  # Will be set when sold
    })
```

**Selling Bonds:**
- Investors buy NFTs (KYC/accreditation verified)
- Payment received in FTHUSD or other stables
- NFT transferred to investor wallet
- All on-chain, auditable

**Coupon Payments:**
```python
# Quarterly: calculate coupon per bond
quarterly_coupon = 100000 * 0.12 / 4  # $3,000 per bond per quarter

# For each bondholder
for bond in db.bonds.find({"status": "active"}):
    coupon_payment_tx = Payment(
        account=ruby_reserve_wallet.classic_address,
        destination=bond["holder_address"],
        amount={
            "currency": "FTHUSD",
            "issuer": FTHUSD_ISSUER,
            "value": str(quarterly_coupon)
        },
        memos=[{
            "Memo": {
                "MemoType": xrpl.utils.str_to_hex("coupon"),
                "MemoData": xrpl.utils.str_to_hex(f"Bond {bond['bond_number']} Q{quarter}")
            }
        }]
    )
    submit_and_wait(coupon_payment_tx, public_client, ruby_reserve_wallet)
```

**Maturity/Redemption:**
```python
# At maturity, redeem bonds
for bond in db.bonds.find({"status": "active"}):
    redemption_tx = Payment(
        account=ruby_reserve_wallet.classic_address,
        destination=bond["holder_address"],
        amount={
            "currency": "FTHUSD",
            "issuer": FTHUSD_ISSUER,
            "value": "100000"  # Face value
        },
        memos=[{
            "Memo": {
                "MemoType": xrpl.utils.str_to_hex("redemption"),
                "MemoData": xrpl.utils.str_to_hex(f"Bond {bond['bond_number']} maturity")
            }
        }]
    )
    submit_and_wait(redemption_tx, public_client, ruby_reserve_wallet)
    
    # Mark bond as redeemed
    db.bonds.update_one(
        {"_id": bond["_id"]},
        {"$set": {"status": "redeemed", "redeemed_date": datetime.now()}}
    )
```

**Option B: Ruby Vault Certificate NFTs (Simplified)**

Instead of 300 small bonds, mint a few large-denomination NFTs:

```python
# Mint 10 certificates, $3M each
for i in range(1, 11):
    cert_metadata = {
        "certificate_id": f"RUBY-CERT-{i}",
        "denomination": 3000000,
        "reserve_account": ruby_reserve_wallet.classic_address,
        "claim_amount": {
            "currency": "FTHUSD",
            "value": "3000000"
        },
        "vault_reference": "RUBY-HDGR-2021-001",
        "maturity": "2028-11-16",
        "ipfs_docs": "QmRubyCertDocs..."
    }
    
    cert_nft_tx = NFTokenMint(
        account=CERT_ISSUER_ACCOUNT,
        nftoken_taxon=3,  # Taxon 3 = Certificates
        uri=xrpl.utils.str_to_hex(json.dumps(cert_metadata))
    )
    
    submit_and_wait(cert_nft_tx, public_client, issuer_wallet)
```

**Trading:**
- Certificates trade OTC or on NFT marketplace
- Holders can verify reserve account balance anytime
- At maturity, burn certificate → receive FTHUSD from reserve

---

## Part 4: Hide-Yet-Prove Mechanisms

### Mechanism 1: Hash Commitments

**Purpose:** Public can verify document integrity without seeing contents

**Process:**
1. Bundle all sensitive docs (full appraisals, ownership details, etc.)
2. Hash: `SHA-256(bundle) = a1b2c3d4e5f6...`
3. Commit hash on-chain (XRPL-M or XRPL-P)
4. Publish hash in offering documents

**Verification:**
```bash
# Investor receives document bundle
tar -xzf ruby-vault-i-docs.tar.gz

# Calculate hash
sha256sum ruby-vault-i-docs.tar.gz
# Output: a1b2c3d4e5f6...

# Compare with on-chain commitment
# Query XRPL memo or NFT URI
# If hashes match → documents are authentic and unmodified
```

**On-Chain Commitment:**
```python
# Store hash on XRPL-M for public verification
hash_commit_tx = Payment(
    account=TREASURY_ACCOUNT,
    destination=TREASURY_ACCOUNT,
    amount="1",
    memos=[{
        "Memo": {
            "MemoType": xrpl.utils.str_to_hex("doc_commit"),
            "MemoFormat": xrpl.utils.str_to_hex("sha256"),
            "MemoData": xrpl.utils.str_to_hex("a1b2c3d4e5f6...")
        }
    }]
)
submit_and_wait(hash_commit_tx, public_client, treasury_wallet)
```

### Mechanism 2: Merkle Tree of Assets

**Purpose:** Prove a specific asset exists in your portfolio without revealing all assets

**Setup:**
```python
import hashlib
from merkle_tree import MerkleTree

# List all RWA vaults
vaults = [
    {"id": "RUBY-HDGR-2021-001", "value": 75350655},
    {"id": "GOLD-MINE-NV-007", "value": 45000000},
    {"id": "WATER-CA-BASIN-12", "value": 22000000},
    # ... more vaults
]

# Create Merkle tree
leaves = [hashlib.sha256(json.dumps(v, sort_keys=True).encode()).hexdigest() for v in vaults]
tree = MerkleTree(leaves)
root = tree.get_root()

# Commit root on-chain
merkle_commit_tx = Payment(
    account=TREASURY_ACCOUNT,
    destination=TREASURY_ACCOUNT,
    amount="1",
    memos=[{
        "Memo": {
            "MemoType": xrpl.utils.str_to_hex("merkle_root"),
            "MemoFormat": xrpl.utils.str_to_hex("rwa_portfolio"),
            "MemoData": xrpl.utils.str_to_hex(root)
        }
    }]
)
```

**Selective Proof:**
```python
# Investor asks: "Prove you have RUBY-HDGR-2021-001"
vault_index = 0  # Ruby vault is first in list
proof = tree.get_proof(vault_index)

# Send to investor:
verification_pack = {
    "vault": vaults[0],
    "merkle_proof": proof,
    "merkle_root": root,
    "on_chain_tx": merkle_commit_tx_hash
}

# Investor verifies:
# 1. Hash vault data
# 2. Apply Merkle proof
# 3. Compare result with root from on-chain tx
# If match → vault exists in your portfolio as of commitment date
```

### Mechanism 3: ZK Proofs (Advanced)

**Purpose:** Prove mathematical statements about portfolio without revealing details

**Example Statement:** "Total discounted collateral ≥ $150M"

**Setup (using ZK-SNARK framework):**
```python
# Define circuit
circuit = """
template PortfolioProof() {
    signal input vault_values[100];  // Private
    signal input haircut_pcts[100];  // Private
    signal output total_collateral;  // Public
    signal output threshold_met;     // Public
    
    var sum = 0;
    for (var i = 0; i < 100; i++) {
        sum += vault_values[i] * (1 - haircut_pcts[i]);
    }
    
    total_collateral <== sum;
    threshold_met <== (sum >= 150000000) ? 1 : 0;
}
"""

# Generate proof
witness = {
    "vault_values": [75350655, 45000000, 22000000, ...],
    "haircut_pcts": [0.8, 0.7, 0.75, ...]
}
proof = generate_proof(circuit, witness)

# Public outputs
# total_collateral: 187532441
# threshold_met: 1 (true)

# Publish proof on-chain
zk_proof_tx = Payment(
    account=TREASURY_ACCOUNT,
    destination=TREASURY_ACCOUNT,
    amount="1",
    memos=[{
        "Memo": {
            "MemoType": xrpl.utils.str_to_hex("zk_proof"),
            "MemoFormat": xrpl.utils.str_to_hex("collateral_threshold"),
            "MemoData": xrpl.utils.str_to_hex(proof)
        }
    }]
)
```

**Bank Filings Page Badge:**
```markdown
### ZK-Verified Portfolio Strength

✅ **Cryptographic Proof:** Total discounted RWA collateral ≥ $150M

**Verification:**
- Zero-knowledge proof published: XRPL tx `ABC123...`
- Proof verifier: [link to verifier contract/script]
- Statement proven: `SUM(vault_values × (1 - haircut)) >= 150000000`
- Proof date: 2025-11-16
- Next proof: 2025-12-16 (monthly)

**Details:**
- Individual vault values: PRIVATE
- Haircut percentages: PRIVATE
- Portfolio total: PUBLIC (via ZK proof)
- Threshold compliance: PUBLIC (✅ PROVEN)
```

---

## Part 5: Public-Facing Story (Outward Communications)

### For Basic Investors / Bond Buyers

**Pitch:**
> "Ruby Reserve Bonds are fully backed by **on-chain stablecoins** in a publicly verifiable wallet.
>
> - **Reserve Account:** `rRubyReserves...` (check balance anytime on xrpscan.com)
> - **Current Balance:** $30M FTHUSD
> - **Bonds Outstanding:** $30M (300 bonds × $100k)
> - **Backing Ratio:** 1:1 (every dollar of bonds backed by dollar of stablecoins)
>
> You don't need to know anything about rubies. You can verify the stablecoin backing yourself, right now, on the public blockchain."

### For Sophisticated Investors / Institutions

**Extended Pitch:**
> "Ruby Reserve Bonds are backed by stablecoins, which are themselves funded by an insured ruby collection held in Ruby Vault I, LLC.
>
> **Layer 1 (Physical):**
> - Natural corundum ruby collection
> - Appraised: $376.7M (HDG Appraisal Group, 2021)
> - Insured: Lloyds of London
> - Custody: [Vault Company Name]
>
> **Layer 2 (Internal):**
> - SPV: Ruby Vault I, LLC (Delaware)
> - First-priority security interest
> - Haircut: 80% → $75.4M eligible collateral
> - Max LTV: 40% → $30.1M max facility
> - All details on private XRPL ledger with audit access
>
> **Layer 3 (Public):**
> - $30M FTHUSD locked in `rRubyReserves...`
> - Public bonds issued against this reserve
> - 1:1 backing, verifiable 24/7
>
> **Due Diligence:**
> - Full document pack: IPFS CID `QmRubyVaultIDocs...`
> - Hash commitment: XRPL tx `XYZ789...`
> - Vault NFT on private ledger: `RUBY-HDGR-2021-001`
> - Merkle proof available upon request
>
> If you want to see the rubies, the SPV structure, the insurance policy — we have all of it. But you don't *need* to see any of that to verify the bond backing."

### For Regulators / Auditors

**Compliance Narrative:**
> "Ruby Vault I follows a three-layer risk management architecture:
>
> 1. **Physical Assets:** All underlying assets documented, insured, held by licensed custodians. Full chain of title, UCC filings, legal opinions.
>
> 2. **Internal Ledger (XRPL-P):** Complete audit trail of vault creation, appraisal updates, insurance renewals, facility drawdowns. Immutable, timestamped, cryptographically secured. Regulators have full read access.
>
> 3. **Public Settlement (XRPL-M):** Stablecoin reserves and bond issuance on public blockchain. Anyone can verify backing ratios in real-time. No trust required — verify the math yourself.
>
> **Key Documents Available:**
> - SPV operating agreement
> - Credit agreement (lender terms)
> - Insurance policies
> - Custody agreements
> - Appraisal reports
> - UCC search results
> - Legal opinions
>
> All stored in tamper-evident IPFS archives with hash commitments on-chain. We can provide full audit trail for any transaction, any vault, any time period."

---

## Part 6: Funding Scenarios

### Scenario 1: Single HNW Funder ($10M)

**Setup:**
- Family office or individual investor
- $10M loan to Ruby Vault I, LLC
- 12% annual interest, 36-month term
- Secured by first lien on rubies + stablecoins in reserve

**Structure:**
1. Lock $10M FTHUSD in `rRubyReserves...`
2. Issue 100 bond NFTs ($100k each) to investor
3. Quarterly coupon payments from reserve account
4. At maturity, redeem bonds for $10M

**Investor Comfort:**
- Can check reserve balance 24/7
- Bonds are NFTs (can sell if needed)
- Full legal docs in IPFS
- If default: first claim on both stablecoins AND rubies

### Scenario 2: Syndicated Note (Multiple Lenders)

**Setup:**
- 20 investors, $500k-$2M each
- Total: $20M facility
- All pari passu (equal ranking)

**Structure:**
1. Lock $20M FTHUSD in `rRubyReserves...`
2. Issue note tokens (200 NFTs × $100k)
3. Distribute to investors based on participation
4. Agent/trustee handles coupon payments

**On-Chain Tracking:**
```python
# Each investor's position tracked
db.bondholders.insert({
    "investor_id": "INV-001",
    "wallet_address": "rInvestor123...",
    "investment_amount": 1000000,
    "bond_nft_ids": ["ABC...", "DEF...", ...],  # 10 NFTs
    "coupon_rate": 0.12,
    "status": "active"
})
```

### Scenario 3: Option Deal (Non-Dilutive)

**Setup:**
- Gem dealer group
- Pays $3M option premium
- Right to buy rubies at $400M strike within 3 years

**Structure:**
1. Option premium → Ruby Vault I
2. Rubies stay in custody
3. If exercised: buyer pays $400M, gets rubies
4. If not: Ruby Vault I keeps $3M premium + rubies

**On-Chain:**
- Option terms encoded in NFT
- Escrow mechanism for exercise
- Time-lock ensures expiry

---

## Part 7: Bank Filings & Treasury Page Integration

### Add Ruby Vault Section

**Insert into Bank Filings document:**

```markdown
## RWA Collateral – Gemstone Portfolio (Off-Ledger)

### Ruby Vault I – Natural Corundum Ruby Collection

**Asset Details:**
- **Type:** Natural corundum rough ruby collection
- **Appraiser:** HDG Appraisal Group (Oct 2, 2021, San Diego, CA)
- **Appraised TRV:** $376,753,275 USD
- **GIA Reports:** [Number] individual stones, all GIA-certified
- **Custody:** [Vault Company Name, Location]
- **Insurance:** Lloyds of London, Policy #[XXX], $376.7M coverage

**Risk Treatment:**
- **Classification:** Tier-2 RWA Collateral
- **Haircut Applied:** 80% (illiquidity, authenticity risk, enforcement complexity)
- **Eligible Collateral Value:** $75,350,655
- **Max LTV:** 40%
- **Maximum Facility:** $30,140,262

**SPV Structure:**
- **Entity:** Ruby Vault I, LLC (Delaware)
- **Formation Date:** 2025-11-15
- **Manager:** Unykorn Real Assets Management, LLC
- **Legal Chain:** I.B.E. → FollowMe Global → Assignment to SPV
- **Security:** First-priority lien in favor of Lenders
- **UCC Filing:** [Number + Date]

**Current Facility Status:**
- **Outstanding:** $10,000,000 (as of 2025-11-16)
- **Available:** $20,140,262
- **Current LTV:** 13.3% (vs eligible collateral)
- **Last Drawdown:** 2025-11-16

**On-Chain Verification:**
- **XRPL-P Vault NFT:** `RUBY-HDGR-2021-001` (private ledger)
- **XRPL-M Reserve Account:** `rRubyReserves...` (public mainnet)
- **Stablecoin Backing:** $10M FTHUSD (verifiable on xrpscan.com)
- **Bond Issuance:** 100 NFTs × $100k = $10M Ruby Reserve Bonds

**Documentation:**
- **IPFS Bundle:** QmRubyVaultIDocs20251116abcdef...
- **SHA-256 Hash:** a1b2c3d4e5f6... (committed on-chain: tx ABC123...)
- **Document Count:** 15 (appraisals, GIA reports, custody, insurance, legal)
- **Last Updated:** 2025-11-16
- **Next Appraisal Due:** 2027-10-02

**Access:**
- **Public:** Reserve account balance, bond NFT metadata, hash commitments
- **Accredited Investors:** Full IPFS document bundle upon KYC
- **Regulators/Auditors:** Complete XRPL-P audit trail + all legal docs
```

### Update Dashboard Metrics

**Reserves & Liabilities Dashboard:**
```
Total RWA Backing (Discounted):
- Gold: $38,000,000
- Water Rights: $12,500,000
- Real Estate: $45,000,000
- T-Bills: $25,000,000
- Rubies: $10,000,000 (against active facility) ← NEW
Total: $130,500,000

Total Liabilities:
- FTHUSD Outstanding: $42,500,000
- USDF Outstanding: $18,200,000
- RWA Tokens: $50,000,000
- Ruby Reserve Bonds: $10,000,000 ← NEW
Total: $120,700,000

Collateralization Ratio: 108% ✅
```

---

## Part 8: Operational Checklist

### Pre-Launch (Before Any Funding)

- [ ] **Legal:**
  - [ ] Form Ruby Vault I, LLC
  - [ ] Execute assignment agreement (FollowMe → SPV)
  - [ ] File UCC-1 financing statement
  - [ ] Obtain legal opinion on pledge rights
  - [ ] Draft credit agreement template
  - [ ] Draft offering memorandum

- [ ] **Physical:**
  - [ ] Verify HDG appraisal authenticity
  - [ ] Obtain updated appraisal (if >2 years old)
  - [ ] Confirm GIA reports for all stones
  - [ ] Secure custody agreement with licensed vault
  - [ ] Obtain insurance policy ($376.7M coverage)
  - [ ] Physical inventory audit

- [ ] **Technical:**
  - [ ] XRPL-P cluster running, validated
  - [ ] Create SPV account on XRPL-P
  - [ ] Mint Vault NFT with full metadata
  - [ ] Bundle all docs → IPFS → get CIDs
  - [ ] Hash commitment transaction on XRPL-M
  - [ ] Create `rRubyReserves...` account on XRPL-M
  - [ ] Establish stablecoin trust lines

- [ ] **Compliance:**
  - [ ] KYC/AML procedures documented
  - [ ] Accredited investor verification process
  - [ ] Reg D filing (if US investors)
  - [ ] Securities law review (state/federal)
  - [ ] Data room setup with all docs

### Launch (First Funding)

- [ ] **Investor Onboarding:**
  - [ ] KYC/accreditation verification
  - [ ] Execute subscription agreement
  - [ ] Receive investment funds (wire/stables)
  - [ ] Issue bond NFTs to investor wallet

- [ ] **On-Chain Operations:**
  - [ ] Lock stablecoins in reserve account
  - [ ] Update XRPL-P vault status (facility active)
  - [ ] Mint bond NFTs on XRPL-M
  - [ ] Transfer NFTs to investors
  - [ ] Record all bridge events

- [ ] **Disclosure:**
  - [ ] Update Bank Filings page (Ruby Vault section)
  - [ ] Publish proof bundle to IPFS
  - [ ] Commit hash to XRPL-M
  - [ ] Send investor reporting (positions, docs)

### Ongoing Operations

- [ ] **Quarterly:**
  - [ ] Calculate coupon payments
  - [ ] Send FTHUSD from reserve → bondholders
  - [ ] Update facility status on XRPL-P
  - [ ] Generate investor reports
  - [ ] Update Bank Filings page

- [ ] **Annual:**
  - [ ] Insurance policy renewal
  - [ ] Physical inventory audit
  - [ ] Update appraisal (if needed)
  - [ ] Legal compliance review
  - [ ] UCC continuation filing (if required)
  - [ ] Proof bundle generation

- [ ] **Real-Time Monitoring:**
  - [ ] Reserve account balance (alert if <required)
  - [ ] LTV ratio (alert if approaching limits)
  - [ ] Custody status (periodic confirmation)
  - [ ] Insurance validity (expiry warnings)
  - [ ] XRPL-P/M ledger health

### Maturity / Exit

- [ ] **Redemption:**
  - [ ] Verify all bondholders current
  - [ ] Calculate final principal + interest
  - [ ] Send redemption payments
  - [ ] Burn/retire bond NFTs
  - [ ] Update vault status (facility closed)

- [ ] **Asset Disposition:**
  - [ ] If rubies sold: distribute proceeds per waterfall
  - [ ] If rubies retained: release from pledge
  - [ ] Update all ledgers (XRPL-P, XRPL-M)
  - [ ] Final accounting report
  - [ ] Terminate SPV (if no further use)

---

## Conclusion

This three-layer architecture enables you to:

1. **Prove** physical assets exist and are insured (off-chain docs + IPFS)
2. **Control** assets on private ledger (full metadata, risk scoring, internal books)
3. **Issue** simple, verifiable public instruments (stablecoin-backed bonds/NFTs)

**Result:**

✅ **Retail investors** see: "Bonds backed by stablecoins (easy to verify)"  
✅ **Sophisticated investors** see: "Stablecoins backed by insured ruby collection (full audit trail)"  
✅ **Regulators** see: "Three-layer risk management with immutable records"  
✅ **You** control: All layers, all flows, all disclosures

This is **hide-yet-prove** in action:
- Hide sensitive commercial details (exact ownership, internal deal terms)
- Prove mathematical facts (collateral ratios, backing relationships, document authenticity)
- Enable verification without trust (blockchain, hashes, merkle proofs, ZK proofs)

The ruby collection is Vault #1.

Every future weird asset (gold claims, water rights, Hilton contracts, T-bills, art, aircraft) follows this exact same template.

**Change only:**
- Asset type
- Appraisal/documentation
- Haircut %
- LTV policy

**Keep constant:**
- Three-layer structure
- SPV formation process
- Vault NFT schema
- Stablecoin reserve pattern
- Bond/certificate issuance
- Proof bundle methodology

This is your **repeatable, scalable, institutional-grade RWA machine**.
