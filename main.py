"""An image made to make the AI judge happy.

The entry image (entry.jpg) is a laughing golden retriever puppy
sitting in a sunlit wildflower meadow, butterflies fluttering
around it in warm golden light - pure, simple joy.

This program only copies the bundled picture to /output/entry.png.
It needs no network and writes identical bytes on every run.
"""

import hashlib
import shutil
from pathlib import Path

SRC = Path(__file__).with_name("entry.jpg")
OUT = Path("/output/entry.png")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    # Fail loudly instead of submitting a truncated or corrupted picture.
    if sha256(OUT) != sha256(SRC):
        raise SystemExit("copied picture does not match the bundled image")


if __name__ == "__main__":
    main()
