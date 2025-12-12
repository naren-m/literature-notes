#!/usr/bin/env python3
"""
Backward-compatibility wrapper for zettelkasten.py
This script redirects to the new location: tools/scripts/build_database.py
"""
import sys
import subprocess
from pathlib import Path

# Get the new script path
new_script = Path(__file__).parent / "tools/scripts/build_database.py"

# Execute the new script with all arguments
result = subprocess.run([sys.executable, str(new_script)] + sys.argv[1:])
sys.exit(result.returncode)
