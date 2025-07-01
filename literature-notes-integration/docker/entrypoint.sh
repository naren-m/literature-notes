#!/bin/bash

# Literature Notes Integration Entrypoint
echo "🚀 Starting Literature Notes Integration Container..."

# Set default values
API_PORT=${API_PORT:-8083}
WEB_PORT=${WEB_PORT:-4000}
NOTES_DB_PATH=${NOTES_DB_PATH:-/app/data/zettelkasten.db}

# Create necessary directories
mkdir -p /app/data /app/logs

# Copy database if it exists in mounted volume
if [ -f "/app/data/zettelkasten.db" ]; then
    echo "✅ Found existing database at /app/data/zettelkasten.db"
else
    echo "⚠️ No database found, will create new one"
fi

# Function to start API server
start_api() {
    echo "🔧 Starting API Server on port $API_PORT..."
    cd /app && python3 scripts/minimal_api.py &
    API_PID=$!
    echo "✅ API Server started (PID: $API_PID)"
}

# Function to start web server
start_web() {
    echo "🌐 Starting Web Server on port $WEB_PORT..."
    
    # Simple HTTP server for markdown viewer
    cd /app/web && python3 -m http.server $WEB_PORT &
    WEB_PID=$!
    echo "✅ Web Server started (PID: $WEB_PID)"
}

# Function to handle shutdown
shutdown() {
    echo ""
    echo "🛑 Shutting down services..."
    
    if [ ! -z "$API_PID" ]; then
        echo "Stopping API Server (PID: $API_PID)..."
        kill $API_PID 2>/dev/null
    fi
    
    if [ ! -z "$WEB_PID" ]; then
        echo "Stopping Web Server (PID: $WEB_PID)..."
        kill $WEB_PID 2>/dev/null
    fi
    
    echo "✅ All services stopped"
    exit 0
}

# Trap signals for graceful shutdown
trap shutdown SIGTERM SIGINT

# Start services
start_api
sleep 2
start_web

echo ""
echo "🎉 Literature Notes Integration Ready!"
echo "=================================================="
echo "📍 API Server:        http://localhost:$API_PORT"
echo "📍 Web Interface:     http://localhost:$WEB_PORT"
echo "📍 Health Check:      http://localhost:$API_PORT/health"
echo "📍 Smart Search:      http://localhost:$WEB_PORT/smart-search.html"
echo ""
echo "🗃️ Database: $NOTES_DB_PATH"
echo "📁 Data Directory: /app/data"
echo ""
echo "🧪 Test API:"
echo "   curl http://localhost:$API_PORT/health"
echo "   curl http://localhost:$API_PORT/stats"
echo ""
echo "🛑 Press Ctrl+C to stop"

# Wait for both processes
wait