from fastapi import APIRouter, Depends
from typing import Annotated
from sqlmodel import Session
from app.api.deps import session_local
from app.models.user import User
from sqlmodel import select

router = APIRouter()

SessionDep = Annotated[Session, Depends(session_local)]

@router.get("/")
def read_users(db: SessionDep):
    user = db.exec(select(User)).all()
    return {"users": user}
