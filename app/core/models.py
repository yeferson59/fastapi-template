from typing import Any

from sqlmodel import Field, SQLModel


class SQLModelWithId(SQLModel):
    id: Any = Field(default=None, primary_key=True)
