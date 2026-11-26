#!/usr/bin/env python3
"""news-image-20261125: emit the front-page PNG for Wednesday 25 November 2026.

Deterministic, stdlib-only, no network. Copies the bundled entry.png to
$MAKEFUN_OUTPUT_DIR (default /output) after validating it is a real PNG
with a 1024x1024 IHDR and a size of at most 1 MiB.
"""
import hashlib
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
MAX_BYTES = 1 * 1024 * 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def fail(msg):
    print("error:", msg, file=sys.stderr)
    return 1


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not os.path.isfile(SRC):
        return fail("entry.png not found next to main.py")
    with open(SRC, "rb") as f:
        data = f.read()
    if len(data) > MAX_BYTES:
        return fail("entry.png is %d bytes (> 1 MiB)" % len(data))
    if data[:8] != PNG_MAGIC:
        return fail("entry.png is not a PNG (bad signature)")
    if len(data) < 33 or data[12:16] != b"IHDR":
        return fail("entry.png has no IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (1024, 1024):
        return fail("entry.png is %dx%d, expected 1024x1024" % (width, height))
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dest)
    with open(dest, "rb") as f:
        written = f.read()
    if hashlib.sha256(written).hexdigest() != hashlib.sha256(data).hexdigest():
        return fail("wrote %s but its bytes differ from entry.png" % dest)
    print("wrote %s (%d bytes, 1024x1024, sha256 %s)"
          % (dest, len(data), hashlib.sha256(data).hexdigest()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
