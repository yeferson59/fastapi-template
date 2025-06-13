from typing import Any, List
from fastapi import APIRouter, HTTPException
from app.crud import crud_user
from app.api.deps import SessionDep
from app.models.user import User as user_model
from app.schemas.user import User, UserCreate, UserUpdate

router = APIRouter()

user_crud = crud_user.CRUDUser(user_model)

@router.get("/", response_model=List[User])
def read_users(
    db: SessionDep,
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve users.
    """
    users = user_crud.get_multi(db=db, skip=skip, limit=limit)
    return users

@router.post("/", response_model=User)
def create_user(
    *,
    db: SessionDep,
    user_in: UserCreate,
) -> Any:
    """
    Create new user.
    """
    if user_in.email is None:
        raise HTTPException(
            status_code=400,
            detail="Email must be provided.",
        )
    existing_user = user_crud.get_by_email(db=db, email=str(user_in.email))
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = user_crud.create(db, obj_in=user_in)
    return user

@router.get("/search/{search_term}", response_model=List[User])
def search_users(
    search_term: str,
    db: SessionDep,
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Search users by name or email.
    """
    users = user_crud.search_by_name_or_email(
        db, search_term=search_term, skip=skip, limit=limit
    )
    return users

@router.get("/{user_id}", response_model=User)
def read_user_by_id(
    user_id: int,
    db: SessionDep,
) -> Any:
    """
    Get a specific user by id.
    """
    user = user_crud.get(db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=User)
def update_user(
    *,
    db: SessionDep,
    user_id: int,
    user_in: UserUpdate,
) -> Any:
    """
    Update an user.
    """
    db_user = user_crud.get(db, id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    user = user_crud.update(db, db_obj=db_user, obj_in=user_in)
    return user

@router.delete("/{user_id}", response_model=User)
def delete_user(
    *,
    db: SessionDep,
    user_id: int,
) -> Any:
    """
    Delete an user.
    """
    db_user = user_crud.get(db, id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    user = user_crud.remove(db, id=user_id)
    return user
