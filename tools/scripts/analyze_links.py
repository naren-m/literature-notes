#!/usr/bin/env python3
"""
CLI entry point for analyze_links.py
"""
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from knowledge_graph.link_analyzer import main

if __name__ == "__main__":
    main()
