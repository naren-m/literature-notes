#!/usr/bin/env python3
"""
CLI entry point for generate_site.py
"""
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from generators.github_pages import main

if __name__ == "__main__":
    main()
