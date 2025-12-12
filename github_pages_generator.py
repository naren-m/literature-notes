#!/usr/bin/env python3
"""
Backward-compatibility wrapper for github_pages_generator.py
This script redirects to the new location: tools/scripts/generate_site.py
"""
import sys
import subprocess
from pathlib import Path

# Get the new script path
new_script = Path(__file__).parent / "tools/scripts/generate_site.py"

# Execute the new script with all arguments
result = subprocess.run([sys.executable, str(new_script)] + sys.argv[1:])
sys.exit(result.returncode)
