from sqlmodel import (create_engine, SQLModel)
from app.core.config import get_settings

settings = get_settings()

connect_args = {"check_same_thread": False}

engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,
    echo=settings.debug,
    connect_args=connect_args,
)

def init_db():
    """Inicializa la base de datos creando todas las tablas"""
    SQLModel.metadata.create_all(bind=engine)
