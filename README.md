# Git-to-Docs Platform

A zero-friction Git-to-docs platform that automatically generates beautiful documentation websites from any public Git repository. Think "Vercel for documentation" - paste any Git URL and get instant, beautiful docs.

## Features

- 🚀 **Zero-friction setup**: Paste any Git URL, get docs in 30 seconds
- 🎨 **Beautiful three-column layout**: Folder tree, API reference, and backlinks
- 🤖 **AI-enhanced summaries**: 60-word conversational explanations for every class
- 🔍 **Offline-capable search**: FlexSearch with instant results
- 🔄 **Auto-sync**: One-click GitHub Actions for continuous updates
- 📊 **Privacy-focused analytics**: Plausible integration with usage insights
- 🎯 **Predictable URLs**: `https://<user>-<repo>.docify.dev`
- ⚡ **Performance optimized**: <8s cold starts, <512MB memory usage

## Quick Start

### Web Interface
1. Visit [docify.dev](https://docify.dev)
2. Paste your Git repository URL
3. Get beautiful documentation in seconds

### CLI (for private repos)
```bash
npx docify@latest https://github.com/your/private-repo
```

## Development

### Prerequisites
- Python 3.11+
- Poetry for dependency management
- Node.js 20+ (for Docusaurus generation)

### Setup
```bash
# Clone the repository
git clone https://github.com/docify/git-to-docs-platform
cd git-to-docs-platform

# Install dependencies
poetry install

# Set up pre-commit hooks
poetry run pre-commit install

# Run the development server
poetry run uvicorn docify.main:app --reload
```

### Testing
```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=docify

# Run property-based tests
poetry run pytest -m property
```

## Architecture

The platform consists of several key components:

- **Repository Processing Engine**: Clones repos and analyzes code structure using tree-sitter
- **Documentation Generator**: Creates Docusaurus sites with AI-enhanced content
- **Hosting Infrastructure**: Serves docs with global CDN and analytics
- **Automation System**: GitHub Actions for continuous synchronization

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## License

MIT License - see [LICENSE](LICENSE) for details.