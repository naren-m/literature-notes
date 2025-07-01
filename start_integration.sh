#!/bin/bash

# Literature Notes Integration Startup Script
# Builds and starts the Docker container with all services

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INTEGRATION_DIR="$SCRIPT_DIR/literature-notes-integration"

echo "🚀 Literature Notes Integration Startup"
echo "========================================"

# Check if Docker is running
if ! docker info >/dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

# Navigate to integration directory
cd "$INTEGRATION_DIR"

# Check if database exists
if [ ! -f "../zettelkasten.db" ]; then
    echo "⚠️  Database not found at ../zettelkasten.db"
    echo "   Creating sample database..."
    
    # Create a minimal database for demo purposes
    mkdir -p ../sample_data
    sqlite3 ../zettelkasten.db << 'EOF'
CREATE TABLE notes (
    id INTEGER PRIMARY KEY,
    path TEXT UNIQUE,
    title TEXT,
    content TEXT,
    tags TEXT,
    wikilinks TEXT,
    backlinks TEXT,
    created TEXT,
    modified TEXT,
    word_count INTEGER
);

CREATE TABLE links (
    source_path TEXT,
    target_path TEXT,
    link_type TEXT
);

CREATE TABLE tags (
    tag TEXT,
    note_path TEXT
);

-- Insert sample data
INSERT INTO notes (path, title, content, tags, created, modified, word_count) VALUES
('sample1.md', 'Getting Started', 'This is a sample note about getting started with the Literature Notes Integration system.', '["productivity", "learning"]', '2025-06-30', '2025-06-30', 20),
('sample2.md', 'Smart Search Demo', 'Demonstrates the smart search capabilities with natural language queries.', '["technology", "search"]', '2025-06-30', '2025-06-30', 15);

INSERT INTO tags (tag, note_path) VALUES
('productivity', 'sample1.md'),
('learning', 'sample1.md'),
('technology', 'sample2.md'),
('search', 'sample2.md');
EOF
    echo "✅ Sample database created"
fi

# Build the Docker image
echo "🔨 Building Docker image..."
docker-compose -f docker/docker-compose.yml build

# Stop any existing containers
echo "🛑 Stopping existing containers..."
docker-compose -f docker/docker-compose.yml down --remove-orphans

# Start the services
echo "🚀 Starting services..."
docker-compose -f docker/docker-compose.yml up -d

# Wait for services to be ready
echo "⏳ Waiting for services to start..."
sleep 10

# Check health
MAX_RETRIES=30
RETRY_COUNT=0

while [ $RETRY_COUNT -lt $MAX_RETRIES ]; do
    if curl -f http://localhost:8080/health >/dev/null 2>&1; then
        echo "✅ Services are healthy!"
        break
    fi
    
    RETRY_COUNT=$((RETRY_COUNT + 1))
    echo "   Attempt $RETRY_COUNT/$MAX_RETRIES - waiting for services..."
    sleep 2
done

if [ $RETRY_COUNT -eq $MAX_RETRIES ]; then
    echo "❌ Services failed to start properly"
    echo "   Check logs with: docker-compose -f literature-notes-integration/docker/docker-compose.yml logs"
    exit 1
fi

# Show status
echo ""
echo "🎉 Literature Notes Integration is ready!"
echo "========================================"
echo ""
echo "📍 Web Interface:  http://localhost:8080"
echo "📍 API Server:     http://localhost:8081"
echo "📍 Health Check:   http://localhost:8080/health"
echo ""
echo "🔧 Management Commands:"
echo "   View logs:       docker-compose -f literature-notes-integration/docker/docker-compose.yml logs -f"
echo "   Stop services:   docker-compose -f literature-notes-integration/docker/docker-compose.yml down"
echo "   Restart:         ./start_integration.sh"
echo ""
echo "🧠 Smart Search Examples:"
echo "   - 'connections between programming and philosophy'"
echo "   - 'recent notes about learning'"
echo "   - 'similar to productivity'"
echo ""

# Optional: Open browser
if command -v open >/dev/null 2>&1; then
    echo "🌐 Opening web interface..."
    sleep 2
    open http://localhost:8080
elif command -v xdg-open >/dev/null 2>&1; then
    echo "🌐 Opening web interface..."
    sleep 2
    xdg-open http://localhost:8080
fi

echo "✨ Ready to explore your knowledge!"