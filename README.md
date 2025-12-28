# fastapi-practice-ci

A small FastAPI practice project with 3 CI builds:
- tests (pytest)
- lint/format (ruff)
- security scan (bandit)

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e ".[dev]"
