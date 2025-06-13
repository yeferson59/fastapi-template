from typing import Any

from sqlmodel import String, cast, or_, select

from app.api.deps import SessionDep
from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_email(self, db: SessionDep, email: str) -> User | None:
        """Obtener usuario por email"""
        statement = select(User).where(User.email == email)
        return db.exec(statement).first()

    def create(self, db: SessionDep, *, obj_in: UserCreate) -> User:
        """Crear nuevo usuario con password hasheado"""
        obj_in_data = obj_in.dict(exclude_unset=True)
        obj_in_data["password"] = get_password_hash(obj_in_data.pop("password"))
        db_obj = User(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: SessionDep, *, db_obj: User, obj_in: UserUpdate | dict[str, Any]
    ) -> User:
        """Actualizar usuario con manejo especial de password"""
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        if "password" in update_data:
            update_data["hashed_password"] = get_password_hash(
                update_data.pop("password")
            )

        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate(self, db: SessionDep, *, email: str, password: str) -> User | None:
        """Autenticar usuario con email y password"""
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user

    def is_active(self, user: User) -> bool:
        """Verificar si el usuario está activo"""
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        """Verificar si el usuario es superusuario"""
        return user.is_superuser

    def activate(self, db: SessionDep, *, db_obj: User) -> User:
        """Activar usuario"""
        db_obj.is_active = True
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def deactivate(self, db: SessionDep, *, db_obj: User) -> User:
        """Desactivar usuario"""
        db_obj.is_active = False
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_active_users(
        self, db: SessionDep, *, skip: int = 0, limit: int = 100
    ) -> list[User]:
        """Obtener solo usuarios activos"""
        statement = select(User).where(User.is_active).offset(skip).limit(limit)
        return list(db.exec(statement).all())

    def search_by_name_or_email(
        self, db: SessionDep, *, search_term: str, skip: int = 0, limit: int = 100
    ) -> list[User]:
        """Buscar usuarios por nombre o email"""
        pattern = f"%{search_term}%"
        statement = (
            select(User)
            .where(
                or_(
                    cast(User.full_name, String).like(pattern),
                    cast(User.email, String).like(pattern),
                )
            )
            .offset(skip)
            .limit(limit)
        )
        return list(db.exec(statement).all())

    # Update all calls to get(..., id=...) to get(..., obj_id=...)
    def get_user_by_id(self, db: SessionDep, user_id: int) -> User | None:
        """Get a specific user by id using obj_id argument."""
        return self.get(db, obj_id=user_id)


user = CRUDUser(User)
