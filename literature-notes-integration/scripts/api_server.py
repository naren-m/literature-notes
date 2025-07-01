#!/usr/bin/env python3
"""
FastAPI server for Literature Notes Integration
Provides REST API endpoints for smart queries and knowledge synthesis
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict
import os
import logging
from datetime import datetime

# Import our custom modules
from smart_query import SmartQueryProcessor
from knowledge_synthesis import KnowledgeSynthesizer

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Literature Notes Integration API",
    description="API for smart queries and knowledge synthesis",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize processors
db_path = os.getenv('NOTES_DB_PATH', '/app/data/zettelkasten.db')
query_processor = SmartQueryProcessor(db_path)
synthesizer = KnowledgeSynthesizer(db_path)

# Request/Response models
class QueryRequest(BaseModel):
    query: str

class SynthesisRequest(BaseModel):
    type: str = "daily"  # daily, domain, cross-domain
    domain: Optional[str] = None
    domain1: Optional[str] = None
    domain2: Optional[str] = None

class HealthResponse(BaseModel):
    status: str
    timestamp: str
    service: str
    database_connected: bool

# API Endpoints
@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Literature Notes Integration API",
        "status": "running",
        "timestamp": datetime.now().isoformat(),
        "endpoints": {
            "smart_query": "/smart-query",
            "synthesis": "/synthesis",
            "health": "/health",
            "docs": "/docs"
        }
    }

@app.get("/health", response_model=HealthResponse)
async def health():
    """Health check endpoint"""
    try:
        # Test database connection
        test_results = query_processor.execute_smart_query("test")
        db_connected = True
    except Exception as e:
        logger.warning(f"Database connection test failed: {e}")
        db_connected = False
    
    return HealthResponse(
        status="healthy" if db_connected else "degraded",
        timestamp=datetime.now().isoformat(),
        service="api",
        database_connected=db_connected
    )

@app.post("/smart-query")
async def smart_query(request: QueryRequest):
    """Execute smart query and return results"""
    try:
        logger.info(f"Processing smart query: {request.query}")
        
        results = query_processor.execute_smart_query(request.query)
        
        # Format results for API response
        formatted_results = []
        for result in results:
            formatted_results.append({
                'title': result.get('title', ''),
                'content': result.get('content', '')[:300] + '...' if len(result.get('content', '')) > 300 else result.get('content', ''),
                'tags': result.get('tags', []),
                'word_count': result.get('word_count', 0),
                'relevance_score': result.get('relevance_score', 0),
                'connection_strength': result.get('connection_strength', 0),
                'path': result.get('path', '')
            })
        
        return {
            "query": request.query,
            "results": formatted_results,
            "count": len(formatted_results),
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        logger.error(f"Smart query failed: {e}")
        raise HTTPException(status_code=500, detail=f"Query processing failed: {str(e)}")

@app.post("/synthesis")
async def generate_synthesis(request: SynthesisRequest, background_tasks: BackgroundTasks):
    """Generate knowledge synthesis"""
    try:
        logger.info(f"Generating synthesis: {request.type}")
        
        if request.type == "daily":
            result = synthesizer.generate_daily_synthesis()
            
        elif request.type == "domain":
            if not request.domain:
                raise HTTPException(status_code=400, detail="Domain parameter required for domain synthesis")
            result = synthesizer.generate_domain_summary(request.domain)
            
        elif request.type == "cross-domain":
            if not request.domain1 or not request.domain2:
                raise HTTPException(status_code=400, detail="Both domain1 and domain2 required for cross-domain synthesis")
            result = synthesizer.find_cross_domain_insights(request.domain1, request.domain2)
            
        else:
            raise HTTPException(status_code=400, detail="Invalid synthesis type. Use: daily, domain, or cross-domain")
        
        return {
            "type": request.type,
            "result": result,
            "timestamp": datetime.now().isoformat()
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Synthesis failed: {e}")
        raise HTTPException(status_code=500, detail=f"Synthesis failed: {str(e)}")

@app.get("/domains")
async def get_available_domains():
    """Get list of available domains for analysis"""
    return {
        "domains": [
            "programming", "sanskrit", "ayurveda", "cryptography", 
            "leadership", "philosophy", "wellness", "learning"
        ],
        "description": "Available domains for synthesis analysis"
    }

@app.get("/stats")
async def get_stats():
    """Get system statistics"""
    try:
        import sqlite3
        
        conn = sqlite3.connect(db_path)
        cursor = conn.execute("SELECT COUNT(*) FROM notes")
        note_count = cursor.fetchone()[0]
        
        cursor = conn.execute("SELECT COUNT(*) FROM links")
        link_count = cursor.fetchone()[0]
        
        cursor = conn.execute("SELECT COUNT(DISTINCT tag) FROM tags")
        tag_count = cursor.fetchone()[0]
        
        cursor = conn.execute("SELECT SUM(word_count) FROM notes WHERE word_count IS NOT NULL")
        total_words = cursor.fetchone()[0] or 0
        
        conn.close()
        
        return {
            "notes": note_count,
            "links": link_count,
            "tags": tag_count,
            "total_words": total_words,
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        logger.error(f"Stats query failed: {e}")
        raise HTTPException(status_code=500, detail=f"Stats unavailable: {str(e)}")

# Error handlers
@app.exception_handler(404)
async def not_found_handler(request, exc):
    return {
        "error": "Endpoint not found",
        "message": "The requested endpoint does not exist",
        "available_endpoints": ["/", "/health", "/smart-query", "/synthesis", "/domains", "/stats"]
    }

@app.exception_handler(500)
async def internal_error_handler(request, exc):
    return {
        "error": "Internal server error",
        "message": "An unexpected error occurred",
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    
    port = int(os.getenv('API_PORT', 8081))
    host = os.getenv('HOST', '0.0.0.0')
    
    logger.info(f"🚀 Starting Literature Notes API server on {host}:{port}")
    
    uvicorn.run(
        app, 
        host=host, 
        port=port,
        log_level="info"
    )