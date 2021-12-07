import json
import argparse
import os
import glob

parser = argparse.ArgumentParser(
    description="Remove grammars from a package.json file."
)
parser.add_argument(
    "--dir", default=".", help="The directory containing manifest files to modify."
)
parser.add_argument(
    "--republish",
    action="store_true",
    help="Whether other manifest options should be changed for republishing.",
)
args = parser.parse_args()

path = os.path.join(args.dir, "package.json")

with open(path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

del manifest["contributes"]["grammars"]

if args.republish:
    manifest["name"] = "grammarless-markdown-all-in-one"
    del manifest["icon"]
    manifest["publisher"] = "jonathanjameswatson"
    manifest["bugs"][
        "url"
    ] = "https://github.com/jonathanjameswatson/grammarless-vscode-markdown/issues"
    manifest["repository"][
        "url"
    ] = "https://github.com/jonathanjameswatson/grammarless-vscode-markdown"

with open(path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=4, ensure_ascii=False)

if args.republish:
    for path_end in glob.glob("package.nls.*json", root_dir=args.dir):
        path = os.path.join(args.dir, path_end)

        with open(path, "r", encoding="utf-8") as f:
            manifest = json.load(f)

        manifest["ext.displayName"] = "Grammarless " + manifest["ext.displayName"]
        manifest["ext.description"] = (
            "(No grammar contributions) " + manifest["ext.description"]
        )

        with open(path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=4, ensure_ascii=False)
