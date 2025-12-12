#!/usr/bin/env python3
"""
CLI entry point for smart query search
"""
import sys
import os
from pathlib import Path

# Add src to path and change to correct directory
src_path = str(Path(__file__).parent.parent / "src")
sys.path.insert(0, src_path)

# Change to literature-notes root for database access
os.chdir(Path(__file__).parent.parent.parent)

# Import and run the search module
if __name__ == "__main__":
    import runpy
    runpy.run_module("zettelkasten.search", run_name="__main__")
