#!/usr/bin/env python3
"""Copy the news-image entry PNG to the make.fun output directory.

Reads ``entry.png`` sitting next to this script, validates that it is a
real 1024x1024 PNG no larger than 1 MiB, copies it into the directory
given by ``MAKEFUN_OUTPUT_DIR`` (``/output`` when unset), and then
re-checks the copy byte-for-byte so a bad write can never slip through.

Standard library only; no network access; deterministic.
"""

import hashlib
import os
import shutil
import struct
import sys

MAX_BYTES = 1_048_576          # 1 MiB
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
ENTRY_NAME = "entry.png"


def die(message: str) -> "SystemExit":
    """Print an error to stderr and exit non-zero."""
    print(f"main.py: error: {message}", file=sys.stderr)
    return SystemExit(1)


def sha256_hex(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(1 << 16), b""):
            digest.update(block)
    return digest.hexdigest()


def check_png(path: str) -> None:
    """Validate size, signature, and the IHDR width/height of *path*."""
    size = os.path.getsize(path)
    if size > MAX_BYTES:
        raise SystemExit(
            f"{path}: file is {size} bytes, over the {MAX_BYTES} byte limit"
        )
    with open(path, "rb") as handle:
        header = handle.read(8)
        if header != PNG_MAGIC:
            raise SystemExit(f"{path}: not a PNG file (bad signature)")
        chunk = handle.read(25)
    if len(chunk) < 25 or chunk[4:8] != b"IHDR":
        raise SystemExit(f"{path}: missing IHDR chunk")
    width, height = struct.unpack(">II", chunk[8:16])
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise SystemExit(
            f"{path}: expected {EXPECTED_WIDTH}x{EXPECTED_HEIGHT}, "
            f"got {width}x{height}"
        )


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, ENTRY_NAME)
    if not os.path.isfile(source):
        print(f"main.py: error: {source} not found", file=sys.stderr)
        return 1

    try:
        check_png(source)
    except SystemExit as failure:
        print(f"main.py: error: {failure}", file=sys.stderr)
        return 1

    destination_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    destination = os.path.join(destination_dir, ENTRY_NAME)
    try:
        os.makedirs(destination_dir, exist_ok=True)
    except OSError as exc:
        print(
            f"main.py: error: cannot create output directory "
            f"{destination_dir}: {exc}",
            file=sys.stderr,
        )
        return 1
    try:
        shutil.copyfile(source, destination)
    except OSError as exc:
        print(
            f"main.py: error: cannot write {destination}: {exc}",
            file=sys.stderr,
        )
        return 1

    expected = sha256_hex(source)
    actual = sha256_hex(destination)
    if actual != expected:
        print(
            "main.py: error: sha256 mismatch after copy\n"
            f"  source: {expected}\n"
            f"  copy:   {actual}",
            file=sys.stderr,
        )
        return 1

    copied_size = os.path.getsize(destination)
    print(
        f"verified {ENTRY_NAME}: {copied_size} bytes, sha256 {actual}",
        file=sys.stderr,
    )
    print(f"copied {ENTRY_NAME} to {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
