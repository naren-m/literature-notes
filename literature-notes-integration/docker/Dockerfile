# Literature Notes Integration Docker Container
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    sqlite3 \
    curl \
    git \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY scripts/ ./scripts/
COPY config/ ./config/
COPY data/ ./data/

# Create necessary directories
RUN mkdir -p /app/data /app/logs /app/web

# Copy entrypoint script
COPY docker/entrypoint.sh .
RUN chmod +x entrypoint.sh

# Copy markdown viewer for integrated access
COPY web/ ./web/

# Expose ports
EXPOSE 8083 4000

# Set environment variables
ENV PYTHONPATH="/app"
ENV NOTES_DB_PATH="/app/data/zettelkasten.db" 
ENV API_PORT=8083
ENV WEB_PORT=4000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8083/health || exit 1

# Create non-root user
RUN useradd -m -u 1000 notes && chown -R notes:notes /app
USER notes

# Run the application
CMD ["./entrypoint.sh"]