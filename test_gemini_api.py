#!/usr/bin/env python3
"""
Test script to verify Gemini API key is working
"""

import os
import asyncio
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

async def test_gemini_api():
    """Test if the Gemini API key is working."""
    
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    
    if not gemini_api_key:
        print("❌ No Gemini API key found in environment")
        print("💡 Please add GEMINI_API_KEY to your .env file")
        return False
    
    print(f"🔑 Found Gemini API key: {gemini_api_key[:10]}...")
    
    try:
        import google.generativeai as genai
        
        # Configure Gemini
        genai.configure(api_key=gemini_api_key)
        
        # Test with a simple prompt
        model = genai.GenerativeModel('gemini-pro')
        
        print("🧪 Testing Gemini API with simple prompt...")
        
        response = await asyncio.to_thread(
            model.generate_content,
            "Say 'Hello from Gemini AI!' in exactly 5 words."
        )
        
        if response and response.text:
            print(f"✅ Gemini API is working!")
            print(f"📝 Response: {response.text.strip()}")
            return True
        else:
            print("❌ Gemini API returned empty response")
            return False
            
    except ImportError:
        print("❌ google-generativeai package not installed")
        print("💡 Run: pip install google-generativeai")
        return False
    except Exception as e:
        print(f"❌ Gemini API error: {str(e)}")
        
        if "API_KEY_INVALID" in str(e):
            print("💡 Your API key appears to be invalid")
            print("💡 Get a new key at: https://aistudio.google.com/")
        elif "quota" in str(e).lower():
            print("💡 You may have exceeded your API quota")
            print("💡 Check your usage at: https://aistudio.google.com/")
        elif "PERMISSION_DENIED" in str(e):
            print("💡 API key doesn't have permission for this model")
            print("💡 Make sure your key has access to Gemini models")
        
        return False

if __name__ == "__main__":
    print("🚀 Testing Gemini AI API Key...")
    print("=" * 50)
    
    success = asyncio.run(test_gemini_api())
    
    print("=" * 50)
    if success:
        print("🎉 Gemini API is ready to use!")
        print("💎 Your premium demo should work with AI features")
    else:
        print("⚠️  Gemini API test failed")
        print("🔧 Please check your API key and try again")
    
    exit(0 if success else 1)