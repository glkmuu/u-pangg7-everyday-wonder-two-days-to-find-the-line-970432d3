"""Write the entry sentence to the output directory.

Reads entry.txt next to this file, validates the gate
(UTF-8, one line, 1-200 characters, not only whitespace),
and writes it byte-for-byte to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).
"""

import os
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    text = text.rstrip("\r\n")
    if not text.strip():
        print("entry is empty or only whitespace", file=sys.stderr)
        return 1
    if text != text.strip():
        print("entry must not have leading or trailing spaces", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 200:
        print(f"entry must be 1-200 characters, got {len(text)}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as f:
        f.write(text.encode("utf-8"))
    print(f"wrote {len(text)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
