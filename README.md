# FastAPI Professional Starter Template

This project is a professional, production-ready template for building robust APIs with [FastAPI](https://fastapi.tiangolo.com/). It provides a clean, scalable structure and best practices to help you start your next Python web project quickly and efficiently.

## Features

- **Modern FastAPI Stack**: Uses FastAPI with async support and type hints.
- **Project Structure**: Organized for scalability and maintainability.
- **SQLModel Integration**: Easy-to-use ORM for database models and queries.
- **User Authentication**: Includes user model, password hashing, and authentication utilities.
- **Environment Management**: Uses `.env` files for configuration.
- **Ready for Docker**: Optimized Dockerfile included.
- **API Versioning**: Example of versioned API endpoints.
- **Extensible CRUD**: Base CRUD classes for rapid development.
- **Testing Ready**: Structure supports adding tests easily.

## Directory Structure

```
simple-api/
├── app/
│   ├── api/           # API route definitions
│   ├── core/          # Core settings, security, and utilities
│   ├── crud/          # CRUD logic for database models
│   ├── models/        # SQLModel database models
│   ├── schemas/       # Pydantic schemas for request/response
│   └── main.py        # FastAPI application entrypoint
├── .env               # Environment variables
├── pyproject.toml     # Project dependencies and metadata
└── README.md          # Project documentation
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-fastapi-template.git
cd your-fastapi-template/simple-api
```

### 2. Install dependencies

It is recommended to use a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt  # or use your preferred tool with pyproject.toml
```

### 3. Configure environment variables

Copy `.env.example` to `.env` and adjust settings as needed.

### 4. Run the application

```bash
uvicorn app.main:app --reload
```

The API will be available at [http://localhost:8000](http://localhost:8000).

### 5. Explore the API docs

Visit [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive Swagger UI.

## Customization

- Add your own models and CRUD logic in `app/models/` and `app/crud/`.
- Define new API endpoints in `app/api/`.
- Adjust settings and secrets in `.env`.

## Docker

This template includes a production-ready Dockerfile for containerized deployments.

### Build the Docker image

```bash
docker build -t fastapi-template .
```

### Run the container

```bash
docker run --env-file .env -p 8000:8000 fastapi-template
```

The application will be available at [http://localhost:8000](http://localhost:8000).

## Deployment

You can deploy this template to any cloud provider or platform that supports Docker containers, such as:

- **AWS ECS / Fargate**
- **Google Cloud Run**
- **Azure Container Apps**
- **DigitalOcean App Platform**
- **Heroku (with Docker support)**
- **Any VPS or server with Docker installed**

For production deployments, consider:

- Setting appropriate environment variables in `.env`
- Using a production-ready ASGI server (e.g., Uvicorn with Gunicorn)
- Configuring HTTPS and a reverse proxy (e.g., Nginx, Traefik)
- Setting up persistent storage for your database

## License

This template is open-source and free to use for any purpose.

---

**Start your next FastAPI project with a solid foundation!**