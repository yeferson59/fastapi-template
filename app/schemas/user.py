from typing import Optional
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    full_name: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    model_config = {
        "from_attributes": True
    }


class User(UserInDBBase):
    pass


class UserInDB(UserInDBBase):
    hashed_password: str
