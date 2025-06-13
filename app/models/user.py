from sqlmodel import Field, SQLModel

from app.core.models import SQLModelWithId


class User(SQLModelWithId, SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)
    full_name: str | None = None
    password: str = Field()
