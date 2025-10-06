from typing import Any, TypeVar

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlmodel import select

from app.api.deps import SessionDep
from app.core.models import SQLModelWithId

ModelType = TypeVar("ModelType", bound=SQLModelWithId)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase[ModelType, CreateSchemaType, UpdateSchemaType]:
    def __init__(self, model: type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLModel model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, db: SessionDep, obj_id: Any) -> ModelType | None:
        """Obtener un registro por ID"""
        statement = select(self.model).where(self.model.id == obj_id)  # type: ignore[attr-defined]
        return db.exec(statement).first()

    def get_multi(
        self, db: SessionDep, skip: int = 0, limit: int = 100
    ) -> list[ModelType]:
        """Obtener múltiples registros con paginación"""
        statement = select(self.model).offset(skip).limit(limit)
        return list(db.exec(statement).all())

    def create(self, db: SessionDep, *, obj_in: CreateSchemaType) -> ModelType:
        """Crear un nuevo registro"""
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: SessionDep,
        *,
        db_obj: ModelType,
        obj_in: UpdateSchemaType | dict[str, Any],
    ) -> ModelType:
        """Actualizar un registro existente"""
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        # Handle both Pydantic v1 (dict) and v2 (model_dump)
        elif hasattr(obj_in, "model_dump"):
            update_data = obj_in.model_dump(exclude_unset=True)
        else:
            update_data = obj_in.dict(exclude_unset=True)  # type: ignore[attr-defined]

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: SessionDep, *, obj_id: int) -> ModelType | None:
        """Eliminar un registro por ID"""
        statement = select(self.model).where(self.model.id == obj_id)  # type: ignore[attr-defined]
        obj = db.exec(statement).first()
        if obj:
            db.delete(obj)
            db.commit()
        return obj

    def count(self, db: SessionDep) -> int:
        """Contar total de registros"""
        statement = select(self.model)
        return len(list(db.exec(statement).all()))

    def exists(self, db: SessionDep, obj_id: Any) -> bool:
        """Verificar si existe un registro por ID"""
        statement = select(self.model).where(self.model.id == obj_id)  # type: ignore[attr-defined]
        return db.exec(statement).first() is not None
