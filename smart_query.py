#!/usr/bin/env python3
"""Search the vault. Wrapper for tools/search_notes.py (kept for old habits)."""
import runpy
import sys
from pathlib import Path

sys.argv[0] = "search_notes.py"
runpy.run_path(str(Path(__file__).parent / "tools" / "search_notes.py"), run_name="__main__")
