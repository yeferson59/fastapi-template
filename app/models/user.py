from typing import Optional
from sqlmodel import Field, SQLModel
from app.crud.base import SQLModelWithId


class User(SQLModelWithId, SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)
    full_name: Optional[str] = None
    password: str = Field()
