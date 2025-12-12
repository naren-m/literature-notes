#!/usr/bin/env python3
"""
CLI entry point for build_forest.py
"""
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from knowledge_graph.forest_builder import main

if __name__ == "__main__":
    main()
