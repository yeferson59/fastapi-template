from fastapi import FastAPI

from app.api.v1.api import api_router
from app.core.config import get_full_api_prefix
from app.db.base import init_db

app = FastAPI()
prefix = get_full_api_prefix()


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Service is running smoothly"}


app.include_router(api_router, prefix=prefix)
