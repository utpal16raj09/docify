# Git-to-Docs Platform Makefile

.PHONY: help install dev test lint format clean run

help: ## Show this help message
	@echo "Git-to-Docs Platform - Development Commands"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	poetry install

dev: ## Install development dependencies
	poetry install --with dev
	poetry run pre-commit install

test: ## Run tests
	poetry run pytest -v

test-cov: ## Run tests with coverage
	poetry run pytest --cov=docify --cov-report=html --cov-report=term

test-property: ## Run property-based tests only
	poetry run pytest -m property -v

lint: ## Run linting
	poetry run flake8 docify tests
	poetry run mypy docify

format: ## Format code
	poetry run black docify tests
	poetry run isort docify tests

clean: ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

run: ## Run the development server
	poetry run uvicorn docify.main:app --reload --host 0.0.0.0 --port 8000

run-prod: ## Run the production server
	poetry run uvicorn docify.main:app --host 0.0.0.0 --port 8000

cli: ## Show CLI help
	poetry run docify --help

docker-build: ## Build Docker image
	docker build -t docify:latest .

docker-run: ## Run Docker container
	docker run -p 8000:8000 docify:latest

setup: install dev ## Complete development setup
	@echo "✅ Development environment setup complete!"
	@echo "🚀 Run 'make run' to start the development server"
	@echo "🧪 Run 'make test' to run the test suite"