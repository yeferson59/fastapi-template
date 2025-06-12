from sqlmodel import SQLModel, Field, String
from typing_extensions import Optional

class User(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True, index=True)
    name: str = Field(String, index=True)
    email: str = Field(String, unique=True, index=True)
