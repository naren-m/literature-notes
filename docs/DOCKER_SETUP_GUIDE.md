# Docker Setup Guide - Literature Notes Integration

## 🚀 Quick Start Commands

Since the automated script isn't running through the interface, here are the manual steps to start your Docker integration:

### 1. Open Terminal and Navigate
```bash
cd /Users/narenmudivarthy/Projects/literature-notes
```

### 2. Make Scripts Executable
```bash
chmod +x start_integration.sh stop_integration.sh run_docker.sh
```

### 3. Start the Integration (Choose one method)

#### Method A: Full Docker Compose (Recommended)
```bash
./start_integration.sh
```

#### Method B: Simple Docker Run
```bash
./run_docker.sh
```

#### Method C: Manual Docker Commands
```bash
# Navigate to integration directory
cd literature-notes-integration

# Build the image
docker build -t literature-notes-integration -f docker/Dockerfile .

# Run the container
docker run -d \
  --name literature-notes-integration \
  -p 8080:8080 \
  -p 8081:8081 \
  -v "$(pwd)/../zettelkasten.db:/app/data/zettelkasten.db:ro" \
  -v "$(pwd)/../logseq:/app/data/logseq" \
  literature-notes-integration
```

## 🔍 Verify Installation

### Check if Services are Running
```bash
# Check container status
docker ps

# Check web service health
curl http://localhost:8080/health

# Check API service
curl http://localhost:8081/health
```

### Access the Services
- **Web Interface**: http://localhost:8080
- **API Documentation**: http://localhost:8081/docs
- **Health Check**: http://localhost:8080/health

## 🧠 Test Smart Search

### Via Web Interface
1. Open http://localhost:8080
2. Try these example queries:
   - "connections between programming and philosophy"
   - "recent notes about learning"
   - "similar to productivity"

### Via API (using curl)
```bash
# Test smart query
curl -X POST "http://localhost:8081/smart-query" \
  -H "Content-Type: application/json" \
  -d '{"query": "connections between programming and philosophy"}'

# Test daily synthesis
curl -X POST "http://localhost:8081/synthesis" \
  -H "Content-Type: application/json" \
  -d '{"type": "daily"}'

# Get system stats
curl "http://localhost:8081/stats"
```

## 🔧 Management Commands

### View Logs
```bash
# Container logs
docker logs literature-notes-integration

# Follow logs in real-time
docker logs -f literature-notes-integration
```

### Stop Services
```bash
# Stop container
docker stop literature-notes-integration

# Remove container
docker rm literature-notes-integration

# Or use the stop script
./stop_integration.sh
```

### Restart Services
```bash
# Stop and restart
docker restart literature-notes-integration

# Or rebuild and restart
./start_integration.sh
```

## 🐛 Troubleshooting

### Common Issues

#### 1. Docker Not Running
```bash
# Check Docker status
docker info

# Start Docker Desktop (macOS)
open -a Docker
```

#### 2. Port Already in Use
```bash
# Find what's using the port
lsof -i :8080
lsof -i :8081

# Kill the process or use different ports
docker run -p 8090:8080 -p 8091:8081 ...
```

#### 3. Database Not Found
The script will automatically create a sample database if your `zettelkasten.db` doesn't exist.

#### 4. Permission Issues
```bash
# Fix script permissions
chmod +x *.sh

# Check file ownership
ls -la zettelkasten.db
```

### View Container Details
```bash
# Inspect running container
docker inspect literature-notes-integration

# Get container IP
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' literature-notes-integration
```

## 📊 What You'll See

### Web Interface Features
- **Smart Search Box** with natural language processing
- **Real-time Statistics** showing your knowledge metrics
- **Search Results** with relevance scoring and connection analysis
- **Responsive Design** that works on mobile and desktop

### API Capabilities
- **Natural Language Queries** with concept expansion
- **Knowledge Synthesis** with automatic insight generation
- **Cross-Domain Analysis** finding unexpected connections
- **Graph Data** for visualization tools

## 🎯 Next Steps

Once the Docker container is running:

1. **Explore Smart Search**: Try different natural language queries
2. **Generate Synthesis**: Use the API to create knowledge insights
3. **Integrate with LogSeq**: The system can sync with your LogSeq setup
4. **Automate Daily Insights**: Set up scheduled synthesis generation
5. **Customize Configuration**: Modify settings in the config files

## 💡 Tips

- **Use the browser**: The web interface at http://localhost:8080 is the easiest way to start
- **Check the API docs**: Visit http://localhost:8081/docs for interactive API documentation
- **Monitor logs**: Use `docker logs -f literature-notes-integration` to see what's happening
- **Backup your data**: Your original database and notes remain untouched

---

Your literature notes are now powered by an intelligent search and synthesis system running in Docker! 🎉