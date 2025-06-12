from sqlmodel import Session
from app.db.base import engine

def session_local():
    with Session(engine) as session:
        yield session
