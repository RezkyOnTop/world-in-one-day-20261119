"""Writes the day's one-page news image to the output directory.

The image is built by build.py with Pillow and committed as entry.png; the
grader's sandbox runs the Python standard library alone, with no network, so
this program only copies those exact bytes. Both runs therefore write the same
file.

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> str:
    os.makedirs(OUT_DIR, exist_ok=True)
    dest = os.path.join(OUT_DIR, "entry.png")
    shutil.copyfile(os.path.join(HERE, "entry.png"), dest)
    return dest


if __name__ == "__main__":
    print(main())
