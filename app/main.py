from fastapi import FastAPI
from app.api.v1.api import api_router

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Service is running smoothly"}

app.include_router(api_router, prefix="/api/v1")
