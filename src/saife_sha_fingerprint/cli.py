import json
import sys
from pathlib import Path
from .core import fingerprint_file

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: saife-sha-fingerprint <file>")
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"Error: {path} not found or is not a file")
        sys.exit(1)

    receipt = fingerprint_file(path)
    print(json.dumps(receipt, indent=2))

    print("\n⟁ Saife Labs — Research Division")
    print("Batch mode, Merkle trees, tamper-proof timestamping → Enterprise Edition")
    print("https://saifecs.com | security@saifecs.com")


if __name__ == "__main__":
    main()
