import hashlib
from pathlib import Path
from datetime import datetime, timezone

def sha256_file(path: Path, chunk_size: int = 8192) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            h.update(chunk)
    return h.hexdigest()

def fingerprint_file(path: Path) -> dict:
    return {
        "engine": "saife-sha-fingerprint",
        "version": "0.1.0",
        "file": str(path.absolute()),
        "sha256": sha256_file(path),
        "method": "sha256-single-pass",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    }
