#!/usr/bin/env python3
"""
Premium SaaS Demo Server for Docify
Enhanced with Gemini AI integration and premium features
"""

import asyncio
import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Try to import settings, fallback to mock if not available
try:
    from docify.config import settings
except ImportError:
    print("⚠️  docify.config not found, using mock settings")
    class MockSettings:
        gemini_api_key = os.getenv("GEMINI_API_KEY")
        openai_api_key = os.getenv("OPENAI_API_KEY")
    settings = MockSettings()

# Initialize FastAPI app with premium configuration
app = FastAPI(
    title="Docify Premium - Git-to-Docs Platform",
    description="Premium SaaS platform for generating beautiful documentation from Git repositories with Gemini AI",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def landing_page(request: Request):
    """Premium landing page with enhanced features."""
    
    # Mock premium user data for demo
    context = {
        "request": request,
        "auth_status": "Premium Active",
        "user_tier": "Pro",
        "rate_limits": {
            "requests_per_minute": 100,
            "builds_per_hour": 50
        }
    }
    
    return templates.TemplateResponse("landing.html", context)

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "version": "1.0.0",
        "ai_provider": "gemini",
        "premium_features": True
    }

@app.get("/api/v1/status")
async def api_status():
    """API status with premium features."""
    return {
        "api_version": "v1",
        "status": "operational",
        "features": {
            "gemini_ai": bool(settings.gemini_api_key),
            "premium_hosting": True,
            "advanced_analytics": True,
            "custom_domains": True,
            "priority_support": True
        },
        "limits": {
            "free_tier": {
                "repositories": 5,
                "builds_per_hour": 10,
                "ai_summaries": False
            },
            "pro_tier": {
                "repositories": "unlimited_public",
                "private_repositories": 50,
                "builds_per_hour": 100,
                "ai_summaries": True,
                "custom_domains": True
            },
            "enterprise_tier": {
                "repositories": "unlimited",
                "builds_per_hour": "unlimited",
                "ai_summaries": True,
                "custom_domains": True,
                "sso_integration": True,
                "dedicated_support": True
            }
        }
    }

# Import API routes (if they exist)
try:
    from docify.api.generate import router as generation_router
    from docify.api.status import router as status_router
    
    app.include_router(generation_router, prefix="/api/v1/generate", tags=["generation"])
    app.include_router(status_router, prefix="/api/v1", tags=["status"])
    print("✅ API routes loaded successfully")
except ImportError as e:
    print(f"⚠️  API routes not found ({e}) - running in demo mode only")
    
    # Create mock API endpoints for demo
    @app.post("/api/v1/generate")
    async def mock_generate_docs(request: dict):
        """Mock documentation generation endpoint for demo."""
        import uuid
        import asyncio
        
        # Simulate processing delay
        await asyncio.sleep(1)
        
        job_id = str(uuid.uuid4())[:8]
        repo_url = request.get("repository_url", "")
        
        # Extract repo name for demo URL
        repo_name = "demo-repo"
        if repo_url:
            try:
                parts = repo_url.rstrip("/").split("/")
                if len(parts) >= 2:
                    repo_name = parts[-1].replace(".git", "")
            except:
                pass
        
        return {
            "job_id": job_id,
            "status": "queued",
            "documentation_url": f"https://{repo_name}.docify.dev",
            "estimated_completion_seconds": 30
        }
    
    @app.get("/api/v1/generate/{job_id}")
    async def mock_get_status(job_id: str):
        """Mock job status endpoint for demo."""
        import random
        import asyncio
        
        # Simulate processing delay
        await asyncio.sleep(0.5)
        
        # Simulate different statuses for demo
        statuses = ["queued", "cloning", "analyzing", "generating", "building", "success"]
        status = random.choice(statuses)
        
        return {
            "job_id": job_id,
            "status": status,
            "documentation_url": f"https://demo-repo.docify.dev",
            "progress": random.randint(10, 90) if status != "success" else 100
        }

def main():
    """Run the premium demo server."""
    print("🚀 Starting Docify Premium Demo Server...")
    print(f"📍 Landing page: http://localhost:8000")
    print(f"📚 API docs: http://localhost:8000/api/docs")
    print(f"🔧 Health check: http://localhost:8000/health")
    print(f"🎨 Premium features: Gemini AI, Dark theme, Rose gold accents")
    
    # Check if Gemini API key is configured
    if settings.gemini_api_key:
        print(f"✅ Gemini AI: Configured (Key: {settings.gemini_api_key[:10]}...)")
        print(f"⚠️  Note: API key may need verification - test with /api/v1/generate")
    else:
        print(f"⚠️  Gemini AI: Not configured (set GEMINI_API_KEY in .env)")
        print(f"💡 Get your free API key at: https://aistudio.google.com/")
    
    print("\n" + "="*60)
    print("Premium SaaS Demo Features:")
    print("• Dark theme with rose gold accents")
    print("• Glassmorphism effects and 3D animations")
    print("• Gemini AI integration for smart summaries")
    print("• Premium pricing tiers")
    print("• Advanced particle system")
    print("• Real-time validation and feedback")
    print("="*60 + "\n")
    
    # Run the server
    uvicorn.run(
        "premium_demo:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    main()