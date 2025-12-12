#!/usr/bin/env python3
"""
Debug script for API server issues
Checks what's happening with port 8081 and provides solutions
"""

import subprocess
import requests
import socket
import time
import json

def check_port_usage(port):
    """Check what's using a specific port"""
    print(f"🔍 Checking what's using port {port}...")
    
    try:
        # Check if port is in use
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            result = s.connect_ex(('localhost', port))
            if result == 0:
                print(f"✅ Port {port} is in use")
            else:
                print(f"❌ Port {port} is NOT in use")
                return False
    except Exception as e:
        print(f"❌ Error checking port {port}: {e}")
        return False
    
    try:
        # Use lsof to find what's using the port
        result = subprocess.run(['lsof', '-i', f':{port}'], 
                              capture_output=True, text=True)
        if result.stdout:
            print(f"📋 Process using port {port}:")
            print(result.stdout)
        else:
            print(f"⚠️ No process found using port {port} (lsof)")
    except Exception as e:
        print(f"⚠️ Could not run lsof: {e}")
    
    return True

def check_docker_container():
    """Check Docker container status"""
    print("\n🐳 Checking Docker container status...")
    
    try:
        # Check if container is running
        result = subprocess.run(['docker', 'ps'], capture_output=True, text=True)
        if 'literature-notes-integration' in result.stdout:
            print("✅ Docker container is running")
            
            # Get container details
            container_result = subprocess.run([
                'docker', 'inspect', 'literature-notes-integration'
            ], capture_output=True, text=True)
            
            if container_result.returncode == 0:
                container_info = json.loads(container_result.stdout)[0]
                ports = container_info.get('NetworkSettings', {}).get('Ports', {})
                print(f"📋 Container port mappings: {ports}")
            
            return True
        else:
            print("❌ Docker container 'literature-notes-integration' is not running")
            
            # Check if it exists but is stopped
            all_containers = subprocess.run(['docker', 'ps', '-a'], 
                                          capture_output=True, text=True)
            if 'literature-notes-integration' in all_containers.stdout:
                print("⚠️ Container exists but is stopped")
            else:
                print("⚠️ Container does not exist")
            
            return False
            
    except Exception as e:
        print(f"❌ Error checking Docker: {e}")
        return False

def check_container_logs():
    """Check container logs for errors"""
    print("\n📜 Checking container logs...")
    
    try:
        result = subprocess.run([
            'docker', 'logs', '--tail', '50', 'literature-notes-integration'
        ], capture_output=True, text=True)
        
        if result.stdout:
            print("📋 Recent container logs:")
            print(result.stdout[-1000:])  # Last 1000 characters
        
        if result.stderr:
            print("🚨 Container errors:")
            print(result.stderr[-1000:])
            
    except Exception as e:
        print(f"❌ Could not get container logs: {e}")

def test_api_endpoints():
    """Test different API endpoints"""
    print("\n🧪 Testing API endpoints...")
    
    endpoints = [
        ("http://localhost:8081/", "Root endpoint"),
        ("http://localhost:8081/health", "Health check"),
        ("http://localhost:8081/docs", "API documentation"),
        ("http://localhost:8081/stats", "Statistics")
    ]
    
    for url, description in endpoints:
        try:
            response = requests.get(url, timeout=5)
            print(f"✅ {description}: {response.status_code}")
            if response.status_code != 200:
                print(f"   Response: {response.text[:200]}")
        except requests.exceptions.RequestException as e:
            print(f"❌ {description}: {e}")

def check_internal_container_process():
    """Check if API process is running inside container"""
    print("\n🔍 Checking internal container processes...")
    
    try:
        result = subprocess.run([
            'docker', 'exec', 'literature-notes-integration', 
            'ps', 'aux'
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("📋 Processes running in container:")
            print(result.stdout)
        else:
            print(f"❌ Could not check container processes: {result.stderr}")
            
    except Exception as e:
        print(f"❌ Error checking container processes: {e}")

def suggest_fixes():
    """Suggest potential fixes"""
    print("\n🔧 Potential Solutions:")
    print("\n1. **Restart the container:**")
    print("   docker restart literature-notes-integration")
    
    print("\n2. **Check if API server started correctly:**")
    print("   docker logs literature-notes-integration | grep -i api")
    
    print("\n3. **Try starting API manually inside container:**")
    print("   docker exec -it literature-notes-integration python scripts/api_server.py")
    
    print("\n4. **Use different port:**")
    print("   docker run -p 8082:8081 ... (change host port)")
    
    print("\n5. **Rebuild container with fixes:**")
    print("   docker stop literature-notes-integration")
    print("   docker rm literature-notes-integration")
    print("   ./start_integration.sh")
    
    print("\n6. **Test web server only (port 8080):**")
    print("   If 8080 works, use that for now: http://localhost:8080")

def create_simple_api_test():
    """Create a simple standalone API server for testing"""
    print("\n🚀 Creating standalone API test server...")
    
    test_server_code = '''#!/usr/bin/env python3
"""Simple test API server"""
from flask import Flask, jsonify
import sys
import os

app = Flask(__name__)

@app.route('/')
def root():
    return jsonify({"message": "Test API server running", "status": "ok"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "port": 8082})

@app.route('/test')
def test():
    return jsonify({"test": "successful", "note": "This is a test API server"})

if __name__ == '__main__':
    print("🧪 Starting test API server on port 8082...")
    app.run(host='0.0.0.0', port=8082, debug=True)
'''
    
    with open('test_api_server.py', 'w') as f:
        f.write(test_server_code)
    
    print("✅ Created test_api_server.py")
    print("   Run with: python test_api_server.py")
    print("   Test with: curl http://localhost:8082/health")

def main():
    """Main debug function"""
    print("🔧 Literature Notes API Debug Tool")
    print("=" * 50)
    
    # Check port 8081
    port_in_use = check_port_usage(8081)
    
    # Check Docker
    docker_running = check_docker_container()
    
    if docker_running:
        check_container_logs()
        check_internal_container_process()
    
    # Test API if port is in use
    if port_in_use:
        test_api_endpoints()
    
    # Always suggest fixes
    suggest_fixes()
    
    # Create test server
    create_simple_api_test()
    
    print("\n" + "=" * 50)
    print("🎯 Debug Summary:")
    print(f"   Port 8081 in use: {'✅' if port_in_use else '❌'}")
    print(f"   Docker running: {'✅' if docker_running else '❌'}")
    
    if not port_in_use:
        print("\n🚨 API server (port 8081) is not responding!")
        print("   Most likely cause: API process failed to start inside container")
        print("   Check container logs and try the suggested solutions above")

if __name__ == "__main__":
    main()
'''