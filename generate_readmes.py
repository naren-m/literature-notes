#!/usr/bin/env python3
"""Entry point used by the Auto-Update GitHub Action.

Rebuilds INDEX.md from the notes. The old per-domain README generator wrote
to folders that no longer exist (CSE/, sanskrit-lit/, highlights/), so it is
gone; domain READMEs under content/ are maintained by hand as map pages.
"""

import runpy
from pathlib import Path

if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).parent / "tools" / "build_index.py"), run_name="__main__")
