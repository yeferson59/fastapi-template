# FastAPI Professional Starter Template

[![CI](https://github.com/yeferson59/fastapi-template/actions/workflows/ci.yml/badge.svg)](https://github.com/yeferson59/fastapi-template/actions/workflows/ci.yml)

A modern, production-ready template for building robust APIs with [FastAPI](https://fastapi.tiangolo.com/), SQLModel, and Docker. This project provides a clean, scalable structure, best practices, and batteries-included features to help you start your next Python web project quickly and efficiently.

---

## Features

- **Modern FastAPI Stack**: Async support, type hints, and modular design.
- **SQLModel ORM**: Simple, powerful database models and queries.
- **User Authentication**: Secure password hashing, user CRUD, and authentication utilities.
- **Environment-based Configuration**: Managed via `.env` and Pydantic settings.
- **API Versioning**: Easily extendable versioned endpoints.
- **Extensible CRUD**: Generic CRUD base for rapid model development.
- **Health Check Endpoint**: Built-in `/health` route for monitoring.
- **Testing Ready**: Structure supports adding tests easily.
- **Docker-Ready**: Multi-stage, production-optimized Dockerfile.
- **MIT Licensed**: Free for personal and commercial use.

---

## Directory Structure

```
simple-api/
├── app/
│   ├── api/           # API routes, versioning, dependencies
│   │   └── v1/
│   │       ├── api.py
│   │       └── endpoints/
│   │           └── users.py
│   ├── core/          # Settings, security utilities
│   ├── crud/          # Base and user CRUD logic
│   ├── db/            # Database engine, session, init
│   ├── models/        # SQLModel database models
│   ├── schemas/       # Pydantic schemas for requests/responses
│   ├── utils/         # Helper utilities
│   └── main.py        # FastAPI application entrypoint
├── tests/             # (Add your tests here)
├── .env.example       # Example environment variables
├── Dockerfile         # Multi-stage, production-ready Dockerfile
├── pyproject.toml     # Project metadata and dependencies
├── uv.lock            # Dependency lock file
├── LICENSE            # MIT License
└── README.md          # Project documentation
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-fastapi-template.git
cd your-fastapi-template/simple-api
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

This template uses [uv](https://github.com/astral-sh/uv) for fast dependency management, but you can use pip as well.

```bash
# With uv (recommended)
uv sync --dev
# Or with pip (if you prefer)
pip install -U pip
pip install .[dev]
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and adjust settings as needed:

```bash
cp .env.example .env
```

### 5. Run the application

```bash
# With uv development (recommended)
uv run fastapi dev app/main.py

# Or with uvicorn directly
# uvicorn app.main:app --reload

# With uv for production
uv run fastapi run app/main.py
```

The API will be available at [http://localhost:8000](http://localhost:8000).

### 6. Explore the API docs

Visit [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive Swagger UI.

---

## Development Workflow

### Linting & Formatting

- **Lint:**
  ```bash
  ruff check . --fix
  ```
- **Format:**
  ```bash
  black .
  ```
- **Sort imports:**
  ```bash
  isort .
  ```

### Pre-commit Hooks

This template includes a `.pre-commit-config.yaml` for automatic linting and formatting before every commit.
To enable:

```bash
pre-commit install
```

### Running Tests

Tests are located in the `tests/` directory and use `pytest` and FastAPI's `TestClient`.

```bash
pytest
```

You can also run all pre-commit hooks manually:

```bash
pre-commit run --all-files
```

---

## API Overview

- **Health Check:** `GET /health`
- **User Endpoints:**
  - `GET /api/v1/users/` — List users
  - `POST /api/v1/users/` — Create user
  - `GET /api/v1/users/search/{search_term}` — Search users by name or email
  - `GET /api/v1/users/{user_id}` — Get user by ID
  - `PUT /api/v1/users/{user_id}` — Update user
  - `DELETE /api/v1/users/{user_id}` — Delete user

---

## Continuous Integration (CI)

This template includes a GitHub Actions workflow for CI/CD:

- Runs on every push and pull request to `main` or `master`
- Installs dependencies (including dev tools)
- Runs linting (ruff), formatting checks (black), import sorting (isort)
- Runs all tests with pytest

You can find the workflow at `.github/workflows/ci.yml`.

> **Important:**
> The CI/CD and all development commands assume you have installed the dev dependencies group (`.[dev]`).

---
## Configuration

All configuration is managed via environment variables. See `.env.example` for available options:

```
PORT=8000
ENVIRONMENT=development
DATABASE_URL=sqlite:///test.sqlite3
SECRET_KEY=your-secret-key-here
API_VERSION=v1
```

---

## Database

- **Default:** SQLite (file-based, easy for development)
- **ORM:** SQLModel (built on SQLAlchemy)
- **Initialization:** Tables are auto-created on startup. You can add seed logic in `app/db/init_db.py`.

---

## Docker

This template includes a multi-stage, production-ready Dockerfile.

### Build the Docker image

```bash
docker build -t fastapi-template .
```

### Run the container

```bash
docker run --env-file .env -p 8000:8000 fastapi-template
```

The application will be available at [http://localhost:8000](http://localhost:8000).

---

## Deployment

You can deploy this template to any cloud provider or platform that supports Docker containers, such as:

- **AWS ECS / Fargate**
- **Google Cloud Run**
- **Azure Container Apps**
- **DigitalOcean App Platform**
- **Heroku (with Docker support)**
- **Any VPS or server with Docker installed**

**Production tips:**
- Set secure values in your `.env`
- Use a production-grade ASGI server (e.g., Uvicorn with Gunicorn)
- Configure HTTPS and a reverse proxy (e.g., Nginx, Traefik)
- Set up persistent storage for your database

---

## Customization

- Add your own models in `app/models/` and schemas in `app/schemas/`
- Implement new CRUD logic in `app/crud/`
- Define new API endpoints in `app/api/v1/endpoints/`
- Adjust settings in `.env` and `app/core/config.py`

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

**Start your next FastAPI project with a solid foundation!**
