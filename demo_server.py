#!/usr/bin/env python3
"""
Demo server for Git-to-Docs Platform
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from datetime import datetime
import json

app = FastAPI(
    title="Git-to-Docs Platform Demo",
    description="Zero-friction documentation generation from Git repositories",
    version="0.1.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def landing_page():
    """Serve a demo landing page."""
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Git-to-Docs Platform - Demo</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { 
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                color: white;
            }
            .container { max-width: 1200px; margin: 0 auto; padding: 2rem; }
            .hero { text-align: center; padding: 4rem 0; }
            .hero h1 { font-size: 3.5rem; margin-bottom: 1rem; font-weight: 700; }
            .hero p { font-size: 1.25rem; margin-bottom: 2rem; opacity: 0.9; }
            .demo-section { 
                background: rgba(255,255,255,0.1); 
                border-radius: 12px; 
                padding: 2rem; 
                margin: 2rem 0;
                backdrop-filter: blur(10px);
            }
            .input-group { margin: 1rem 0; }
            .input-group label { display: block; margin-bottom: 0.5rem; font-weight: 600; }
            .input-group input { 
                width: 100%; 
                padding: 0.75rem; 
                border: none; 
                border-radius: 6px; 
                font-size: 1rem;
            }
            .btn { 
                background: #4CAF50; 
                color: white; 
                padding: 0.75rem 2rem; 
                border: none; 
                border-radius: 6px; 
                cursor: pointer; 
                font-size: 1rem;
                margin: 0.5rem;
            }
            .btn:hover { background: #45a049; }
            .btn-secondary { background: #2196F3; }
            .btn-secondary:hover { background: #1976D2; }
            .result { 
                background: rgba(0,0,0,0.2); 
                padding: 1rem; 
                border-radius: 6px; 
                margin-top: 1rem;
                font-family: monospace;
            }
            .features { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin: 2rem 0; }
            .feature { background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 8px; }
            .feature h3 { margin-bottom: 1rem; color: #FFD700; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="hero">
                <h1>🚀 Git-to-Docs Platform</h1>
                <p>Zero-friction documentation generation from any Git repository</p>
                <p><em>The "Vercel for Documentation" - Instant, Beautiful, AI-Enhanced</em></p>
            </div>

            <div class="demo-section">
                <h2>🎯 Try the Demo</h2>
                <div class="input-group">
                    <label for="repo-url">Git Repository URL:</label>
                    <input type="text" id="repo-url" placeholder="https://github.com/username/repository" 
                           value="https://github.com/fastapi/fastapi">
                </div>
                <button class="btn" onclick="generateDocs()">Generate Documentation</button>
                <button class="btn btn-secondary" onclick="checkStatus()">Check System Status</button>
                <div id="result" class="result" style="display: none;"></div>
            </div>

            <div class="features">
                <div class="feature">
                    <h3>⚡ Lightning Fast</h3>
                    <p>8-second cold start builds with intelligent caching and optimization</p>
                </div>
                <div class="feature">
                    <h3>🤖 AI-Enhanced</h3>
                    <p>Automatic summaries and explanations for classes and functions</p>
                </div>
                <div class="feature">
                    <h3>🔍 Smart Search</h3>
                    <p>Offline-capable FlexSearch with instant results across all code elements</p>
                </div>
                <div class="feature">
                    <h3>🎨 Beautiful UI</h3>
                    <p>Three-column layout with dark/light themes and responsive design</p>
                </div>
                <div class="feature">
                    <h3>🔄 Auto-Sync</h3>
                    <p>GitHub Actions integration for automatic documentation updates</p>
                </div>
                <div class="feature">
                    <h3>📊 Analytics</h3>
                    <p>Privacy-focused usage analytics and search insights</p>
                </div>
            </div>

            <div class="demo-section">
                <h2>🛠️ API Endpoints</h2>
                <p><strong>POST /api/v1/generate</strong> - Generate documentation from Git URL</p>
                <p><strong>GET /api/v1/generate/{job_id}</strong> - Check generation status</p>
                <p><strong>GET /api/v1/status</strong> - System health and metrics</p>
                <p><strong>GET /health</strong> - Health check</p>
            </div>
        </div>

        <script>
            async function generateDocs() {
                const url = document.getElementById('repo-url').value;
                const resultDiv = document.getElementById('result');
                
                if (!url) {
                    alert('Please enter a Git repository URL');
                    return;
                }
                
                resultDiv.style.display = 'block';
                resultDiv.innerHTML = '🔄 Generating documentation...';
                
                try {
                    const response = await fetch('/api/v1/generate', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({
                            repository_url: url,
                            include_ai_summaries: true,
                            generate_search_index: true
                        })
                    });
                    
                    const data = await response.json();
                    
                    if (response.ok) {
                        resultDiv.innerHTML = `
                            <h3>✅ Documentation Generation Started!</h3>
                            <p><strong>Job ID:</strong> ${data.job_id}</p>
                            <p><strong>Repository:</strong> ${data.repository.owner}/${data.repository.name}</p>
                            <p><strong>Status:</strong> ${data.status}</p>
                            <p><strong>Documentation URL:</strong> <a href="${data.documentation_url}" target="_blank">${data.documentation_url}</a></p>
                            <p><strong>Estimated completion:</strong> ${data.estimated_completion_seconds} seconds</p>
                        `;
                    } else {
                        resultDiv.innerHTML = `<h3>❌ Error:</h3><p>${data.detail}</p>`;
                    }
                } catch (error) {
                    resultDiv.innerHTML = `<h3>❌ Network Error:</h3><p>${error.message}</p>`;
                }
            }
            
            async function checkStatus() {
                const resultDiv = document.getElementById('result');
                resultDiv.style.display = 'block';
                resultDiv.innerHTML = '🔄 Checking system status...';
                
                try {
                    const response = await fetch('/api/v1/status');
                    const data = await response.json();
                    
                    resultDiv.innerHTML = `
                        <h3>📊 System Status</h3>
                        <p><strong>Status:</strong> ${data.status}</p>
                        <p><strong>Active Builds:</strong> ${data.active_builds}</p>
                        <p><strong>Queue Length:</strong> ${data.performance_metrics.queue_length}</p>
                        <p><strong>Average Build Time:</strong> ${data.performance_metrics.average_build_time_seconds}s</p>
                        <p><strong>Success Rate:</strong> ${data.performance_metrics.success_rate}%</p>
                    `;
                } catch (error) {
                    resultDiv.innerHTML = `<h3>❌ Error:</h3><p>${error.message}</p>`;
                }
            }
        </script>
    </body>
    </html>
    """

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "version": "0.1.0",
        "timestamp": datetime.now().isoformat(),
        "performance_constraints": {
            "max_build_time_seconds": 8,
            "max_memory_usage_mb": 512,
            "max_deploy_time_seconds": 30,
        }
    }

@app.post("/api/v1/generate")
async def generate_documentation(request: Request):
    """Demo endpoint for documentation generation."""
    body = await request.json()
    repository_url = body.get("repository_url", "")
    
    if not repository_url:
        raise HTTPException(status_code=400, detail="Repository URL is required")
    
    # Parse repository info
    if "github.com" not in repository_url:
        raise HTTPException(status_code=400, detail="Only GitHub repositories are supported in this demo")
    
    try:
        # Extract owner and repo name from URL
        parts = repository_url.rstrip("/").split("/")
        owner = parts[-2]
        repo_name = parts[-1].replace(".git", "")
        
        job_id = f"demo-{owner}-{repo_name}-{int(datetime.now().timestamp())}"
        
        return {
            "job_id": job_id,
            "repository": {
                "url": repository_url,
                "owner": owner,
                "name": repo_name,
                "branch": "main"
            },
            "status": "pending",
            "documentation_url": f"https://{owner}-{repo_name}.docify.dev",
            "estimated_completion_seconds": 30,
            "options": {
                "include_ai_summaries": body.get("include_ai_summaries", True),
                "generate_search_index": body.get("generate_search_index", True)
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid repository URL: {str(e)}")

@app.get("/api/v1/generate/{job_id}")
async def get_generation_status(job_id: str):
    """Demo endpoint for checking generation status."""
    # Simulate different statuses based on job_id
    if "demo-" in job_id:
        return {
            "job_id": job_id,
            "status": "completed",
            "progress": 100,
            "repository": {
                "owner": "demo",
                "name": "repository"
            },
            "documentation_url": "https://demo-repository.docify.dev",
            "build_time_seconds": 6.2,
            "memory_usage_mb": 384,
            "deploy_time_seconds": 12.5
        }
    else:
        raise HTTPException(status_code=404, detail="Job not found")

@app.get("/api/v1/status")
async def system_status():
    """Demo system status endpoint."""
    return {
        "status": "healthy",
        "active_builds": 2,
        "performance_metrics": {
            "total_builds": 1247,
            "successful_builds": 1198,
            "failed_builds": 49,
            "success_rate": 96.1,
            "average_build_time_seconds": 5.8,
            "queue_length": 0,
            "estimated_wait_time_seconds": 0
        },
        "system_resources": {
            "cpu_usage_percent": 23.5,
            "memory_usage_percent": 67.2,
            "disk_usage_percent": 45.8
        }
    }

if __name__ == "__main__":
    print("🚀 Starting Git-to-Docs Platform Demo...")
    print("📊 Demo server with mock data and real UI")
    print("🌐 Open http://127.0.0.1:8000 in your browser")
    
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")