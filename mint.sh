#!/usr/bin/env bash
# Flame Division Mint Flow (example skeleton)
# This is a commented template; replace commands with your actual toolchain (e.g., thirdweb, manifold, hardhat).

set -e

## 1) PIN ASSETS (examples - replace with your pinning method)
# ipfs add -r ./assets
# or use web UI / pinning service and paste resulting CIDs below

## 2) GENERATE METADATA FROM TEMPLATE WITH CHECKSUM
# python3 checksum_inject.py #   --template classB_scroll_template.json #   --asset ./assets/scroll_exec_lockin_v1.pdf #   --image ipfs://<CID_image> #   --name "Scroll — The Executive Lock-In (v1)" #   --description "Canonical scroll from Flame Division archives." #   --division "Phase III → Real‑World Flame Integration" #   --class "Scroll" #   --version v1 #   --law "Authority isn’t granted; it’s engineered through mastery." #   --rights "CC-BY-ND" #   --royalty-bps 1000 #   --external-url "https://flamedivision.link/scrolls/exec-lock-in" #   --original-cid <CID_master_pdf> #   --out ./out/scroll_exec_lockin_v1.json

## 3) (Optional) VALIDATE METADATA AGAINST SCHEMA
# npx ajv validate -s flame_nft_metadata_schema.json -d ./out/scroll_exec_lockin_v1.json

## 4) MINT (examples)
# -- Thirdweb CLI example (pseudo) --
# npx thirdweb@latest upload ./out/scroll_exec_lockin_v1.json
# npx thirdweb@latest mint --contract <address> --metadata ./out/scroll_exec_lockin_v1.json --to <your_wallet>

# -- Hardhat/Remix: pass JSON URL (ipfs:// or ar://) to your contract's mint function

echo 'Template ready. Fill values and run your chosen toolchain to mint.'
