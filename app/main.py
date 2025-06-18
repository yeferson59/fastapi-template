from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.api.v1.api import api_router
from app.core.config import get_full_api_prefix
from app.db.base import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa: ARG001
    init_db()
    yield


app = FastAPI(lifespan=lifespan)
prefix = get_full_api_prefix()


@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Service is running smoothly"}


app.include_router(api_router, prefix=prefix)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
