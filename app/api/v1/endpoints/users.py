from fastapi import APIRouter, HTTPException

from app.api.deps import SessionDep
from app.crud import crud_user
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

router = APIRouter()

user_crud = crud_user.CRUDUser(User)


@router.get("/", response_model=list[User])
def read_users(
    db: SessionDep,
    skip: int = 0,
    limit: int = 100,
) -> list[User]:
    """
    Retrieve users.
    """
    return user_crud.get_multi(db=db, skip=skip, limit=limit)


@router.post("/", response_model=User)
def create_user(
    *,
    db: SessionDep,
    user_in: UserCreate,
) -> User:
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
    return user_crud.create(db, obj_in=user_in)


@router.get("/search/{search_term}", response_model=list[User])
def search_users(
    search_term: str,
    db: SessionDep,
    skip: int = 0,
    limit: int = 100,
) -> list[User]:
    """
    Search users by name or email.
    """
    return user_crud.search_by_name_or_email(
        db, search_term=search_term, skip=skip, limit=limit
    )


@router.get("/{user_id}", response_model=User)
def read_user_by_id(
    user_id: int,
    db: SessionDep,
) -> User:
    """
    Get a specific user by id.
    """
    user = user_crud.get(db, obj_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=User)
def update_user(
    *,
    db: SessionDep,
    user_id: int,
    user_in: UserUpdate,
) -> User:
    """
    Update an user.
    """
    db_user = user_crud.get(db, obj_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return user_crud.update(db, db_obj=db_user, obj_in=user_in)


@router.delete("/{user_id}", response_model=User)
def delete_user(
    *,
    db: SessionDep,
    user_id: int,
) -> User | None:
    """
    Delete an user.
    """
    db_user = user_crud.get(db, obj_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return user_crud.remove(db, obj_id=user_id)
