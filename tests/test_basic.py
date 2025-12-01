from saife_sha_fingerprint.core import sha256_file, fingerprint_file
from pathlib import Path
import tempfile
import json

def test_sha256_known_string():
    """Hash a known string and verify deterministic result."""
    with tempfile.NamedTemporaryFile() as tf:
        tf.write(b"saife")
        tf.seek(0)
        expected = "79cde40927b9aac2a757f7732c9d86fe3c037ba10fbfed43e7ff311691b40f9e"

        assert sha256_file(Path(tf.name)) == expected


def test_fingerprint_structure():
    """Fingerprint should return a dict with required fields."""
    with tempfile.NamedTemporaryFile() as tf:
        tf.write(b"test123")
        tf.seek(0)
        receipt = fingerprint_file(Path(tf.name))

    assert isinstance(receipt, dict)
    assert "engine" in receipt
    assert "version" in receipt
    assert "file" in receipt
    assert "sha256" in receipt
    assert "timestamp_utc" in receipt


def test_timestamp_format():
    """Timestamp must end with Z and be ISO-like."""
    with tempfile.NamedTemporaryFile() as tf:
        tf.write(b"hello world")
        tf.seek(0)
        receipt = fingerprint_file(Path(tf.name))

    ts = receipt["timestamp_utc"]
    # Basic ISO sanity check (we don't validate exact format to avoid time logic issues)
    assert ts.endswith("Z")
    assert "T" in ts
