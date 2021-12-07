import json
import argparse

parser = argparse.ArgumentParser(
    description="Remove grammars from a package.json file."
)
parser.add_argument(
    "--file", default="package.json", help="The package.json file to modify."
)
parser.add_argument(
    "--republish",
    action="store_true",
    help="Whether other manifest options should be changed for republishing.",
)
args = parser.parse_args()

with open(args.file, "r") as f:
    data = json.load(f)

del data["contributes"]["grammars"]

if args.republish:
    data["name"] = "grammarless-markdown-all-in-one"
    del data["icon"]
    data["publisher"] = "jonathanjameswatson"
    data["bugs"][
        "url"
    ] = "https://github.com/jonathanjameswatson/grammarless-vscode-markdown/issues"
    data["repository"][
        "url"
    ] = "https://github.com/jonathanjameswatson/grammarless-vscode-markdown"

with open(args.file, "w") as f:
    json.dump(data, f, indent=4)
