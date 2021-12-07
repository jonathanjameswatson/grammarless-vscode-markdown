import json
import argparse

parser = argparse.ArgumentParser(
    description="Remove grammars from a package.json file."
)
parser.add_argument(
    "--file", default="package.json", help="The package.json file to modify."
)
args = parser.parse_args()

with open(args.file, "r") as f:
    data = json.load(f)

del data["contributes"]["grammars"]

with open(args.file, "w") as f:
    json.dump(data, f, indent=4)
