# Flame Division NFT Pack — RLHF-Ready

This folder contains an **airtight JSON schema + class templates** for Flame Division NFTs and a small utility
to **compute checksums and inject metadata** before minting.

## Files
- `flame_nft_metadata_schema.json` — JSON Schema for validation.
- `classA_seal_template.json` — Template for **Seals** (ERC-721 1/1).
- `classB_scroll_template.json` — Template for **Scrolls** (ERC-1155, versioned).
- `classC_clip_template.json` — Template for **Proof Clips** (ERC-1155 with \"animation_url\").
- `classD_art_template.json` — Template for **Cultural Works**.
- `checksum_inject.py` — Utility to auto-compute SHA-256 and inject fields.
- `mint.sh` — Example shell flow (pin assets, validate, and prepare for on-chain mint).

> **Note:** Replace placeholders like `<REPLACE_...>` before minting. Keep your creator keys in cold storage.
> This pack focuses on **metadata integrity and provenance**; on-chain mint commands depend on your chosen toolchain.

---

## Quick Start

1. **Compute checksum & inject fields** into a copy of a template:
```bash
python3 checksum_inject.py   --template classB_scroll_template.json   --asset ./assets/scroll_exec_lockin_v1.pdf   --image ipfs://<CID_image_or_arweave>   --name "Scroll — The Executive Lock-In (v1)"   --description "Canonical scroll from Flame Division archives."   --division "Phase III → Real‑World Flame Integration"   --class "Scroll"   --version v1   --law "Authority isn’t granted; it’s engineered through mastery."   --rights "CC-BY-ND"   --royalty-bps 1000   --external-url "https://flamedivision.link/scrolls/exec-lock-in"   --original-cid <CID_of_master_pdf>   --out ./out/scroll_exec_lockin_v1.json
```

2. **(Optional) Validate** your JSON against the schema (use your preferred validator).
3. **Mint** using your chosen tool (Remix/Hardhat/Thirdweb/Manifold), pointing to the finalized JSON.
   See `mint.sh` for a commented example flow.

---

## Operational Checklist (Field Edition)

- [ ] Master asset uploaded to Arweave/IPFS (write down CID).
- [ ] `checksum_inject.py` run → `checksum_sha256` populated.
- [ ] Rights string + royalties (bps) set.
- [ ] Attributes verified: **Division, Class, Version, Flame Law, Author, Issued**.
- [ ] If updating an older piece: set `current_cid` and `deprecation_pointer` to the new token/URL.
- [ ] Append entry to your **Collections Registry** (contract, tokenID, CIDs, hash, date).
