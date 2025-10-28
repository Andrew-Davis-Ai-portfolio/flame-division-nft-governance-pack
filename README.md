# 🔥 Flame Division NFT Governance Pack

**Author:** Andrew Davis  
**Certifications:** Certified AI Implementation Professional (CAIIP) · Chief AI Officer (CAIO)  
**Division:** Flame Division Command — Phase IV Deployment  

---

### 🧩 Overview
This repository is a verifiable archive demonstrating **AI-powered NFT governance**, schema generation, and automation scripting.  
It integrates blockchain metadata standards with human-in-the-loop RLHF design — ensuring transparency, integrity, and control.

---

### 📁 Contents
| Folder/File | Purpose |
|--------------|----------|
| `classA–D_*_template.json` | Base schema templates for hierarchical NFT classes |
| `example_classA–D_*_filled.json` | Example metadata instances with production values |
| `flame_nft_metadata_schema.json` | Master metadata validation schema |
| `checksum_inject.py` | Python utility for hash integrity verification |
| `mint.sh` | Automated shell script for minting sequence execution |
| `Flame_Division_Minting_Protocol.pdf` | Full governance and deployment documentation |
| `README.md` | Overview and reference guide |

---

### ⚙️ Execution Flow
```bash
# Validate schema
python3 checksum_inject.py

# Run minting sequence
bash mint.sh

What’s inside (built for RLHF + on-chain hygiene)
	•	Schema enforces fields: name, description, image, attributes + governance extras (rights, royalty_bps, version, checksum_sha256, original_cid/current_cid, deprecation_pointer).
	•	Class A – Seal: 1/1 authority artifacts (ERC-721 recommended), royalty_bps: 750 (7.5%) default.
	•	Class B – Scroll: versioned doctrine/milestones (ERC-1155), ideal for v1/v2 updates with deprecation pointers.
	•	Class C – Proof Clip: 15-sec verification/tutorial modules (ERC-1155), includes animation_url for video.
	•	Class D – Cultural Work: covers/banners/posters (721 or 1155).

Quick-use checklist (before mint)
	1.	Replace all <REPLACE_…> fields.
	2.	Upload asset to Arweave/IPFS → paste CID into image (and animation_url if video).
	3.	Compute SHA-256 of the master file → set checksum_sha256.
	4.	Set rights and royalty_bps (e.g., 1000 = 10%).
	5.	For updates, set current_cid and fill deprecation_pointer with the successor token URL/ID.
