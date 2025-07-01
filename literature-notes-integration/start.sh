#!/bin/bash

# Literature Notes Integration - Docker Startup Script

echo "🚀 Starting Literature Notes Integration Docker Container"
echo "========================================================"

# Set script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Check if Docker is running
if ! docker info >/dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker and try again."
    exit 1
fi

# Check if database exists
if [ ! -f "../zettelkasten.db" ]; then
    echo "⚠️ Warning: zettelkasten.db not found in parent directory"
    echo "   The container will create a new database"
fi

# Create data directory if it doesn't exist
mkdir -p ../data

echo "📦 Building Docker container..."
cd docker

# Build and start the container
docker-compose up --build -d

# Wait for services to start
echo "⏳ Waiting for services to start..."
sleep 10

# Check health
echo "🔍 Checking service health..."

# Check API health
if curl -f http://localhost:8083/health >/dev/null 2>&1; then
    echo "✅ API Server: http://localhost:8083"
else
    echo "❌ API Server: Not responding"
fi

# Check web interface
if curl -f http://localhost:4000 >/dev/null 2>&1; then
    echo "✅ Web Interface: http://localhost:4000"
else
    echo "❌ Web Interface: Not responding"
fi

echo ""
echo "🎉 Literature Notes Integration Started!"
echo "========================================"
echo "📍 Smart Search:    http://localhost:4000/smart-search.html"
echo "📍 Markdown Viewer: http://localhost:4000/markdown-viewer.html"
echo "📍 API Health:      http://localhost:8083/health"
echo "📍 API Stats:       http://localhost:8083/stats"
echo ""
echo "🔧 Management Commands:"
echo "   docker-compose logs -f    # View logs"
echo "   docker-compose stop       # Stop services"
echo "   docker-compose down       # Stop and remove"
echo ""
echo "🧪 Test API:"
echo "   curl http://localhost:8083/health"
echo "   curl http://localhost:8083/stats"
echo ""

# Show running containers
echo "📊 Container Status:"
docker-compose ps