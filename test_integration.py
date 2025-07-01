#!/usr/bin/env python3
"""
Test script for Literature Notes Integration
Verifies that all components are working correctly
"""

import requests
import json
import time
import sys
from pathlib import Path

def test_service(url, name, timeout=5):
    """Test if a service is responding"""
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            print(f"✅ {name} is responding")
            return True
        else:
            print(f"⚠️ {name} returned status {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ {name} is not responding: {e}")
        return False

def test_smart_query():
    """Test smart query functionality"""
    print("\n🧠 Testing Smart Query...")
    
    query_data = {"query": "connections between programming and philosophy"}
    
    try:
        response = requests.post(
            "http://localhost:8081/smart-query",
            json=query_data,
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            results_count = data.get('count', 0)
            print(f"✅ Smart query successful - Found {results_count} results")
            
            if results_count > 0:
                # Show first result
                first_result = data['results'][0]
                print(f"   📄 Sample result: {first_result.get('title', 'No title')}")
            
            return True
        else:
            print(f"❌ Smart query failed with status {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Smart query request failed: {e}")
        return False

def test_synthesis():
    """Test knowledge synthesis"""
    print("\n🔗 Testing Knowledge Synthesis...")
    
    synthesis_data = {"type": "daily"}
    
    try:
        response = requests.post(
            "http://localhost:8081/synthesis",
            json=synthesis_data,
            timeout=15
        )
        
        if response.status_code == 200:
            data = response.json()
            result = data.get('result', {})
            groups = result.get('groups', [])
            insights = result.get('insights', [])
            
            print(f"✅ Synthesis successful")
            print(f"   📊 Knowledge clusters: {len(groups)}")
            print(f"   💡 Insights generated: {len(insights)}")
            
            return True
        else:
            print(f"❌ Synthesis failed with status {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Synthesis request failed: {e}")
        return False

def test_stats():
    """Test system statistics"""
    print("\n📊 Testing System Stats...")
    
    try:
        response = requests.get("http://localhost:8081/stats", timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Stats retrieved successfully")
            print(f"   📝 Notes: {data.get('notes', 0)}")
            print(f"   🔗 Links: {data.get('links', 0)}")
            print(f"   🏷️ Tags: {data.get('tags', 0)}")
            print(f"   📖 Total words: {data.get('total_words', 0)}")
            return True
        else:
            print(f"❌ Stats failed with status {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Stats request failed: {e}")
        return False

def check_files():
    """Check if required files exist"""
    print("📁 Checking Integration Files...")
    
    required_files = [
        "literature-notes-integration/docker/Dockerfile",
        "literature-notes-integration/docker/docker-compose.yml",
        "literature-notes-integration/scripts/smart_query.py",
        "literature-notes-integration/scripts/knowledge_synthesis.py",
        "literature-notes-integration/scripts/web_server.py",
        "literature-notes-integration/requirements.txt",
        "zettelkasten.db"
    ]
    
    all_good = True
    for file_path in required_files:
        if Path(file_path).exists():
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - MISSING")
            all_good = False
    
    return all_good

def main():
    """Main test function"""
    print("🧪 Literature Notes Integration Test Suite")
    print("=" * 50)
    
    # Check files first
    files_ok = check_files()
    if not files_ok:
        print("\n❌ Some required files are missing. Please run the setup first.")
        return False
    
    print("\n🔍 Testing Service Connectivity...")
    
    # Test basic connectivity
    web_ok = test_service("http://localhost:8080/health", "Web Service")
    api_ok = test_service("http://localhost:8081/health", "API Service")
    
    if not (web_ok and api_ok):
        print("\n❌ Services are not running. Please start Docker first:")
        print("   ./start_integration.sh")
        print("   or")
        print("   ./run_docker.sh")
        return False
    
    # Test functionality
    query_ok = test_smart_query()
    synthesis_ok = test_synthesis()
    stats_ok = test_stats()
    
    # Summary
    print("\n" + "=" * 50)
    print("🎯 Test Summary:")
    
    tests = [
        ("Files Present", files_ok),
        ("Web Service", web_ok),
        ("API Service", api_ok),
        ("Smart Query", query_ok),
        ("Knowledge Synthesis", synthesis_ok),
        ("System Stats", stats_ok)
    ]
    
    passed = sum(1 for _, result in tests if result)
    total = len(tests)
    
    for test_name, result in tests:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"   {test_name:<20} {status}")
    
    print(f"\n🏆 Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! Your Literature Notes Integration is working perfectly!")
        print("\n🚀 Ready to use:")
        print("   📍 Web Interface: http://localhost:8080")
        print("   📍 API Docs: http://localhost:8081/docs")
        print("   📍 Try a smart query: 'connections between programming and philosophy'")
        return True
    else:
        print(f"\n⚠️ {total - passed} tests failed. Check the output above for details.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)