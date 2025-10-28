#!/usr/bin/env python3
import json, argparse, hashlib, os, sys
from datetime import date

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def set_attr(attrs, trait_type, value):
    for a in attrs:
        if a.get("trait_type") == trait_type:
            a["value"] = value
            return
    attrs.append({"trait_type": trait_type, "value": value})

def main():
    p = argparse.ArgumentParser(description="Inject checksum + fields into Flame NFT metadata template")
    p.add_argument("--template", required=True, help="Path to metadata template JSON")
    p.add_argument("--asset", help="Path to master asset (for checksum)")
    p.add_argument("--image", help="Image URL/CID (ar:// or ipfs://)")
    p.add_argument("--animation-url", help="Animation/video URL/CID (for clips)")
    p.add_argument("--name")
    p.add_argument("--description")
    p.add_argument("--division")
    p.add_argument("--class")
    p.add_argument("--version")
    p.add_argument("--law")
    p.add_argument("--author", default="Commander Flame")
    p.add_argument("--issued", default=date.today().isoformat())
    p.add_argument("--rights")
    p.add_argument("--royalty-bps", type=int)
    p.add_argument("--external-url")
    p.add_argument("--original-cid")
    p.add_argument("--current-cid")
    p.add_argument("--deprecation-pointer")
    p.add_argument("--out", required=True, help="Output JSON path")
    args = p.parse_args()

    with open(args.template, "r") as f:
        meta = json.load(f)

    # Basic fields
    if args.name: meta["name"] = args.name
    if args.description: meta["description"] = args.description
    if args.image: meta["image"] = args.image
    if args.animation_url: meta["animation_url"] = args.animation_url
    if args.external_url: meta["external_url"] = args.external_url

    # Rights/Royalties
    if args.rights: meta["rights"] = args.rights
    if args.royalty_bps is not None: meta["royalty_bps"] = int(args.royalty_bps)

    # Provenance fields
    if args.original_cid: meta["original_cid"] = args.original_cid
    if args.current_cid: meta["current_cid"] = args.current_cid
    if args.version: meta["version"] = args.version
    if args.deprecation_pointer: meta["deprecation_pointer"] = args.deprecation_pointer

    # Compute checksum if asset provided
    if args.asset:
        if not os.path.exists(args.asset):
            sys.exit(f"[ERR] Asset not found: {args.asset}")
        meta["checksum_sha256"] = "sha256:" + sha256_file(args.asset)

    # Attributes updates
    attrs = meta.get("attributes", [])
    if args.division: set_attr(attrs, "Division", args.division)
    if args.class: set_attr(attrs, "Class", args.class)
    if args.version: set_attr(attrs, "Version", args.version)
    if args.law: set_attr(attrs, "Flame Law", args.law)
    if args.author: set_attr(attrs, "Author", args.author)
    if args.issued: set_attr(attrs, "Issued", args.issued)
    meta["attributes"] = attrs

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)

    print(f"[OK] Wrote {args.out}")

if __name__ == "__main__":
    main()
