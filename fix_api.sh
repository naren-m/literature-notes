#!/bin/bash

# Fix API Server Script for Literature Notes Integration
echo "🔧 Fixing API Server Issues..."

# Check if Docker container is running
if ! docker ps | grep -q literature-notes-integration; then
    echo "❌ Container not running. Starting container first..."
    ./start_integration.sh
    sleep 10
fi

# Check container status
echo "📋 Container status:"
docker ps | grep literature-notes-integration

# Check container logs for errors
echo -e "\n📜 Recent container logs:"
docker logs --tail 20 literature-notes-integration

# Check if API process is running inside container
echo -e "\n🔍 Checking processes inside container:"
docker exec literature-notes-integration ps aux | grep -E "(python|api|uvicorn)" || echo "No API processes found"

# Try to start API server manually inside container
echo -e "\n🚀 Attempting to start API server manually..."
docker exec -d literature-notes-integration python scripts/api_server.py

# Wait a moment
sleep 5

# Test API endpoints
echo -e "\n🧪 Testing API endpoints:"
curl -s http://localhost:8081/health | jq . || echo "API not responding"

# If still not working, try alternative approach
if ! curl -s http://localhost:8081/health > /dev/null 2>&1; then
    echo -e "\n⚠️ API still not responding. Trying alternative fixes..."
    
    # Stop and restart container
    echo "🔄 Restarting container..."
    docker restart literature-notes-integration
    
    # Wait for restart
    sleep 15
    
    # Test again
    echo "🧪 Testing after restart..."
    curl -s http://localhost:8081/health | jq . || echo "Still not responding"
    
    # Show detailed container info
    echo -e "\n📊 Container detailed info:"
    docker inspect literature-notes-integration | jq '.[] | {Status: .State.Status, Ports: .NetworkSettings.Ports}'
fi

# Alternative: Use web server API endpoints
echo -e "\n💡 Alternative: Testing web server API endpoints (port 8080):"
curl -s "http://localhost:8080/api/stats" | jq . || echo "Web server API also not available"

# Provide manual steps
echo -e "\n📋 Manual debugging steps:"
echo "1. Check container logs: docker logs literature-notes-integration"
echo "2. Access container shell: docker exec -it literature-notes-integration /bin/bash"
echo "3. Manually start API: docker exec literature-notes-integration python scripts/api_server.py"
echo "4. Check port mapping: docker port literature-notes-integration"
echo "5. Use web interface instead: http://localhost:8080"

echo -e "\n✅ Fix script completed. Check output above for issues."