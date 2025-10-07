from sqlmodel import Field, SQLModel


class SQLModelWithId(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
