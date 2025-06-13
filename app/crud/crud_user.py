from typing import Any, Dict, Optional, Union, List
from sqlmodel import select
from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.api.deps import SessionDep


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_email(self, db: SessionDep, email: str) -> Optional[User]:
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
        self,
        db: SessionDep,
        *,
        db_obj: User,
        obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        """Actualizar usuario con manejo especial de password"""
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        if "password" in update_data:
            update_data["hashed_password"] = get_password_hash(update_data.pop("password"))

        return super().update(db, db_obj=db_obj, obj_in=update_data)


    def authenticate(self, db: SessionDep, *, email: str, password: str) -> Optional[User]:
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

    def get_active_users(self, db: SessionDep, *, skip: int = 0, limit: int = 100) -> List[User]:
        """Obtener solo usuarios activos"""
        statement = select(User).where(User.is_active == True).offset(skip).limit(limit)
        return list(db.exec(statement).all())

    def search_by_name_or_email(
        self,
        db: SessionDep,
        *,
        search_term: str,
        skip: int = 0,
        limit: int = 100
    ) -> List[User]:
        """Buscar usuarios por nombre o email"""
        statement = (
            select(User)
            .where(
                (User.full_name.contains(search_term)) | (User.email.contains(search_term)) # type: ignore
            )
            .offset(skip)
            .limit(limit)
        )
        return list(db.exec(statement).all())


user = CRUDUser(User)
