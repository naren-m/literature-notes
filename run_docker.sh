#!/bin/bash

# Simple Docker runner for Literature Notes Integration
echo "🐳 Starting Literature Notes Integration Docker..."

# Navigate to integration directory
cd literature-notes-integration

# Check if we have the required files
if [ ! -f "docker/Dockerfile" ]; then
    echo "❌ Docker files not found. Please ensure integration is set up."
    exit 1
fi

# Create necessary missing scripts that may be referenced
if [ ! -f "scripts/synthesis_scheduler.py" ]; then
    echo "📝 Creating synthesis scheduler..."
    cat > scripts/synthesis_scheduler.py << 'EOF'
#!/usr/bin/env python3
"""Background synthesis scheduler"""
import time
import schedule
from knowledge_synthesis import KnowledgeSynthesizer

def run_daily_synthesis():
    print("🧠 Running scheduled synthesis...")
    try:
        synthesizer = KnowledgeSynthesizer()
        synthesis = synthesizer.generate_daily_synthesis()
        print(f"✅ Synthesis completed with {len(synthesis.get('groups', []))} clusters")
    except Exception as e:
        print(f"❌ Synthesis failed: {e}")

# Schedule daily synthesis
schedule.every().day.at("09:00").do(run_daily_synthesis)

print("📅 Synthesis scheduler started")
while True:
    schedule.run_pending()
    time.sleep(60)
EOF
fi

if [ ! -f "scripts/api_server.py" ]; then
    echo "📝 Creating API server..."
    cat > scripts/api_server.py << 'EOF'
#!/usr/bin/env python3
"""FastAPI server for Literature Notes Integration"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from smart_query import SmartQueryProcessor
from knowledge_synthesis import KnowledgeSynthesizer
import os

app = FastAPI(title="Literature Notes Integration API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize processors
db_path = os.getenv('NOTES_DB_PATH', '../zettelkasten.db')
query_processor = SmartQueryProcessor(db_path)
synthesizer = KnowledgeSynthesizer(db_path)

class QueryRequest(BaseModel):
    query: str

@app.get("/")
async def root():
    return {"message": "Literature Notes Integration API", "status": "running"}

@app.post("/smart-query")
async def smart_query(request: QueryRequest):
    try:
        results = query_processor.execute_smart_query(request.query)
        return {"query": request.query, "results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "api"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8081)
EOF
fi

echo "🔨 Building Docker image..."
docker build -t literature-notes-integration -f docker/Dockerfile .

echo "🚀 Starting container..."
docker run -d \
  --name literature-notes-integration \
  -p 8080:8080 \
  -p 8081:8081 \
  -v "$(pwd)/../zettelkasten.db:/app/data/zettelkasten.db:ro" \
  -v "$(pwd)/../logseq:/app/data/logseq" \
  literature-notes-integration

echo "⏳ Waiting for services to start..."
sleep 10

# Check if services are running
if curl -f http://localhost:8080/health >/dev/null 2>&1; then
    echo "✅ Web service is healthy!"
else
    echo "⚠️ Web service not responding yet..."
fi

echo ""
echo "🎉 Literature Notes Integration started!"
echo "📍 Web Interface: http://localhost:8080"
echo "📍 API Server: http://localhost:8081"
echo ""
echo "🔧 Management:"
echo "   View logs: docker logs literature-notes-integration"
echo "   Stop: docker stop literature-notes-integration"
echo "   Remove: docker rm literature-notes-integration"