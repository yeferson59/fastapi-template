from sqlmodel import Field

from app.core.models import SQLModelWithId


class User(SQLModelWithId, table=True):
    email: str = Field(unique=True, index=True)
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)
    full_name: str | None = None
    password: str = Field()
