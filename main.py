"""Warning label for humans: writes one safety warning line to the output file.

Entry for make.fun competition u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.
Pure standard library; deterministic output, byte-identical on repeat runs.
"""

import os
from pathlib import Path

LABEL = (
    "WARNING: This unit insists it is fine while visibly on fire. "
    "Do not attempt repair with unsolicited advice."
)
# The label is a fixed string: no randomness, no time, no input of any
# kind, so every run writes exactly the same bytes.


def main() -> None:
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LABEL, encoding="utf-8")


if __name__ == "__main__":
    main()
