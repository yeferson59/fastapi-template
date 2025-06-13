from sqlmodel import Session
from app.db.base import engine

def get_db():
  with Session(engine) as session:
      yield session
