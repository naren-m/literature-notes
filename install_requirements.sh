#!/bin/bash

# Install Requirements for Literature Notes Integration
echo "📦 Installing Python packages for Literature Notes Integration..."

# Check if pip is available
if ! command -v pip &> /dev/null; then
    echo "❌ pip not found. Trying pip3..."
    if ! command -v pip3 &> /dev/null; then
        echo "❌ Neither pip nor pip3 found. Please install Python pip first."
        exit 1
    else
        PIP_CMD="pip3"
    fi
else
    PIP_CMD="pip"
fi

echo "✅ Using $PIP_CMD for installation"

# Install core packages
echo "🔧 Installing core packages..."
$PIP_CMD install flask flask-cors requests python-dateutil schedule

# Install optional packages for better functionality
echo "🔧 Installing optional packages..."
$PIP_CMD install fastapi uvicorn pandas numpy

echo "✅ Package installation completed!"

# Test imports
echo "🧪 Testing package imports..."
python3 -c "
try:
    import flask
    print('✅ Flask imported successfully')
except ImportError as e:
    print(f'❌ Flask import failed: {e}')

try:
    import flask_cors
    print('✅ Flask-CORS imported successfully')
except ImportError as e:
    print(f'❌ Flask-CORS import failed: {e}')

try:
    import requests
    print('✅ Requests imported successfully')
except ImportError as e:
    print(f'❌ Requests import failed: {e}')

try:
    import sqlite3
    print('✅ SQLite3 imported successfully')
except ImportError as e:
    print(f'❌ SQLite3 import failed: {e}')
"

echo ""
echo "🎉 Ready to run the API server!"
echo "📍 Next step: python simple_api_start.py"