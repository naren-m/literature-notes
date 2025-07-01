#!/bin/bash

# Literature Notes Integration Stop Script
# Gracefully stops all Docker services

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INTEGRATION_DIR="$SCRIPT_DIR/literature-notes-integration"

echo "🛑 Stopping Literature Notes Integration..."
echo "=========================================="

cd "$INTEGRATION_DIR"

# Stop and remove containers
echo "📦 Stopping Docker containers..."
docker-compose -f docker/docker-compose.yml down --remove-orphans

# Optional: Remove volumes (uncomment to clean all data)
# echo "🗑️  Removing volumes..."
# docker-compose -f docker/docker-compose.yml down -v

# Show status
echo ""
echo "✅ Literature Notes Integration stopped!"
echo ""
echo "🔧 Other commands:"
echo "   Start again:     ./start_integration.sh"
echo "   View logs:       docker-compose -f literature-notes-integration/docker/docker-compose.yml logs"
echo "   Clean volumes:   docker-compose -f literature-notes-integration/docker/docker-compose.yml down -v"
echo ""