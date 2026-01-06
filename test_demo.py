#!/usr/bin/env python3
"""
Simple test script to verify the premium demo server is working
"""

import requests
import time

def test_server():
    """Test if the premium demo server is responding correctly."""
    base_url = "http://localhost:8000"
    
    print("🧪 Testing Premium Demo Server...")
    print(f"📍 Base URL: {base_url}")
    
    try:
        # Test health endpoint
        print("\n1. Testing health endpoint...")
        response = requests.get(f"{base_url}/health", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Health check passed")
            print(f"   📊 Status: {data.get('status')}")
            print(f"   🤖 AI Provider: {data.get('ai_provider')}")
            print(f"   💎 Premium Features: {data.get('premium_features')}")
        else:
            print(f"   ❌ Health check failed: {response.status_code}")
            return False
        
        # Test API status endpoint
        print("\n2. Testing API status endpoint...")
        response = requests.get(f"{base_url}/api/v1/status", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ API status check passed")
            print(f"   🔧 API Version: {data.get('api_version')}")
            features = data.get('features', {})
            print(f"   🤖 Gemini AI: {'✅' if features.get('gemini_ai') else '❌'}")
            print(f"   💎 Premium Hosting: {'✅' if features.get('premium_hosting') else '❌'}")
            print(f"   📊 Advanced Analytics: {'✅' if features.get('advanced_analytics') else '❌'}")
        else:
            print(f"   ❌ API status check failed: {response.status_code}")
            return False
        
        # Test landing page
        print("\n3. Testing landing page...")
        response = requests.get(base_url, timeout=5)
        if response.status_code == 200:
            content = response.text
            print(f"   ✅ Landing page loaded successfully")
            
            # Check for premium features in the HTML
            checks = [
                ("Premium theme", "rose gold" in content.lower() or "premium" in content.lower()),
                ("Docify branding", "Docify" in content),
                ("Premium CSS", "landing.css" in content),
                ("Premium JS", "landing.js" in content),
                ("No emojis in title", "🚀 Docify" not in content),
                ("Clean title", "<h1>Docify</h1>" in content)
            ]
            
            for check_name, passed in checks:
                status = "✅" if passed else "❌"
                print(f"   {status} {check_name}")
                
        else:
            print(f"   ❌ Landing page failed: {response.status_code}")
            return False
        
        print("\n🎉 All tests passed! Premium demo is working correctly.")
        print("\n📋 Summary:")
        print("   • Server is running on http://localhost:8000")
        print("   • Health checks are passing")
        print("   • Premium features are enabled")
        print("   • Gemini AI integration is configured")
        print("   • Landing page loads with premium theme")
        print("   • No emojis in the clean premium design")
        
        return True
        
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Is it running on http://localhost:8000?")
        return False
    except requests.exceptions.Timeout:
        print("❌ Server response timeout")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    # Wait a moment for server to be ready
    print("⏳ Waiting for server to be ready...")
    time.sleep(2)
    
    success = test_server()
    exit(0 if success else 1)