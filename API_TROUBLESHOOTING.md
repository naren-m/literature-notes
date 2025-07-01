# API Troubleshooting Guide - Port 8081 Not Working

## 🔧 Quick Fixes

Since port 8081 is not responding, here are several solutions in order of complexity:

### **Solution 1: Use Simple Local API (Recommended)**
```bash
# Start a simple API server on port 8082
python simple_api_start.py
```
This creates a working API server on port 8082 that you can test immediately.

**Test it:**
```bash
curl http://localhost:8082/health
curl http://localhost:8082/stats
```

### **Solution 2: Debug the Docker Container**
```bash
# Run the debug script
python debug_api.py

# Or manually check container
docker logs literature-notes-integration
docker exec -it literature-notes-integration /bin/bash
```

### **Solution 3: Fix Docker Container**
```bash
# Make script executable and run
chmod +x fix_api.sh
./fix_api.sh
```

### **Solution 4: Use Web Server API (Port 8080)**
The web server on port 8080 might have API endpoints:
```bash
curl http://localhost:8080/api/stats
curl http://localhost:8080/health
```

## 🐛 Common Issues & Solutions

### **Issue 1: Container Started But API Process Failed**
```bash
# Check what's running inside container
docker exec literature-notes-integration ps aux

# Manually start API inside container
docker exec -d literature-notes-integration python scripts/api_server.py

# Check if it started
curl http://localhost:8081/health
```

### **Issue 2: Port Mapping Problem**
```bash
# Check port mappings
docker port literature-notes-integration

# If wrong, restart with correct mapping
docker stop literature-notes-integration
docker run -d --name literature-notes-integration -p 8080:8080 -p 8081:8081 ...
```

### **Issue 3: Missing Dependencies**
```bash
# Install dependencies inside container
docker exec literature-notes-integration pip install fastapi uvicorn

# Or rebuild container
docker stop literature-notes-integration
docker rm literature-notes-integration
cd literature-notes-integration
docker build -t literature-notes-integration -f docker/Dockerfile .
```

### **Issue 4: API Server Code Issues**
The entrypoint script might not be starting the API correctly.

**Check entrypoint:**
```bash
docker exec literature-notes-integration cat entrypoint.sh
```

**Manual start:**
```bash
docker exec -it literature-notes-integration /bin/bash
cd /app
python scripts/api_server.py
```

## 🧪 Testing APIs

### **Test Simple API (Port 8082)**
```bash
# Health check
curl http://localhost:8082/health

# Get statistics
curl http://localhost:8082/stats

# Simple search
curl "http://localhost:8082/search?q=programming"

# Smart query
curl -X POST -H "Content-Type: application/json" \
  -d '{"query":"connections between programming and philosophy"}' \
  http://localhost:8082/smart-query
```

### **Test Docker API (Port 8081 - if working)**
```bash
curl http://localhost:8081/health
curl http://localhost:8081/docs
curl -X POST -H "Content-Type: application/json" \
  -d '{"query":"programming"}' \
  http://localhost:8081/smart-query
```

## 🔍 Diagnostic Commands

```bash
# Check what's using port 8081
lsof -i :8081

# Check Docker container status
docker ps
docker inspect literature-notes-integration

# Check container logs
docker logs literature-notes-integration

# Check container processes
docker exec literature-notes-integration ps aux

# Check container networking
docker exec literature-notes-integration netstat -tlnp
```

## 💡 Alternative Approaches

### **1. Use Web Interface Only**
If APIs are problematic, use the web interface at http://localhost:8080

### **2. Run Scripts Directly**
```bash
cd literature-notes-integration/scripts
python smart_query.py "connections between programming and philosophy"
python knowledge_synthesis.py daily
```

### **3. Rebuild from Scratch**
```bash
# Complete reset
docker stop literature-notes-integration
docker rm literature-notes-integration
docker rmi literature-notes-integration

# Rebuild
./start_integration.sh
```

## 🎯 Recommended Steps

1. **First, try the simple API:**
   ```bash
   python simple_api_start.py
   ```

2. **Test the simple API:**
   ```bash
   curl http://localhost:8082/health
   ```

3. **If that works, debug Docker:**
   ```bash
   python debug_api.py
   ```

4. **Fix Docker issues:**
   ```bash
   ./fix_api.sh
   ```

5. **As last resort, rebuild:**
   ```bash
   ./stop_integration.sh
   ./start_integration.sh
   ```

The simple API server (`simple_api_start.py`) should give you immediate functionality while we debug the Docker container issue!