#!/bin/bash

# Literature Notes API Integration Startup Script
echo "🚀 Starting Literature Notes with Smart Search API..."

# Check if API is already running
if curl -s http://localhost:8083/health > /dev/null 2>&1; then
    echo "✅ API already running at http://localhost:8083"
else
    echo "🔧 Starting API server..."
    # Try python3 first, then python
    if command -v python3 &> /dev/null; then
        python3 minimal_api.py &
        API_PID=$!
    elif command -v python &> /dev/null; then
        python minimal_api.py &
        API_PID=$!
    else
        echo "❌ Neither python nor python3 found"
        exit 1
    fi
    
    # Wait for API to start
    sleep 3
    
    if curl -s http://localhost:8083/health > /dev/null 2>&1; then
        echo "✅ API started successfully (PID: $API_PID)"
    else
        echo "❌ API failed to start"
        exit 1
    fi
fi

# Start Jekyll if not running
if ! curl -s http://localhost:4000 > /dev/null 2>&1; then
    echo "🌐 Starting Jekyll documentation server..."
    
    # Check if we have Jekyll/Bundler
    if command -v bundle &> /dev/null; then
        bundle exec jekyll serve --host 0.0.0.0 --port 4000 &
        JEKYLL_PID=$!
    elif command -v jekyll &> /dev/null; then
        jekyll serve --host 0.0.0.0 --port 4000 &
        JEKYLL_PID=$!
    else
        echo "⚠️ Jekyll not found. Starting simple HTTP server instead..."
        if command -v python3 &> /dev/null; then
            python3 -m http.server 4000 &
            JEKYLL_PID=$!
        elif command -v python &> /dev/null; then
            python -m http.server 4000 &
            JEKYLL_PID=$!
        else
            echo "❌ No Python found for HTTP server"
        fi
    fi
    
    echo "⏳ Waiting for web server to start..."
    sleep 5
    
    if curl -s http://localhost:4000 > /dev/null 2>&1; then
        echo "✅ Documentation server started successfully (PID: $JEKYLL_PID)"
    else
        echo "❌ Documentation server failed to start"
    fi
else
    echo "✅ Documentation server already running at http://localhost:4000"
fi

echo ""
echo "🎉 Literature Notes Integration Ready!"
echo "=================================================="
echo "📍 Documentation Site: http://localhost:4000"
echo "📍 Smart Search Page:  http://localhost:4000/api-search"
echo "📍 Direct API Access:  http://localhost:8083"
echo ""
echo "🧪 Test API directly:"
echo "   curl http://localhost:8083/health"
echo "   curl http://localhost:8083/stats"
echo ""
echo "🛑 To stop all services:"
echo "   pkill -f 'python minimal_api.py'"
echo "   pkill -f jekyll"
echo "   # or press Ctrl+C"
echo ""

# Optional: Open browser
if command -v open >/dev/null 2>&1; then
    echo "🌐 Opening documentation in browser..."
    sleep 2
    open http://localhost:4000/api-search
elif command -v xdg-open >/dev/null 2>&1; then
    echo "🌐 Opening documentation in browser..."
    sleep 2
    xdg-open http://localhost:4000/api-search
fi

echo "✨ Your literature notes now have intelligent search!"