from sqlmodel import SQLModel, create_engine

from app.core.config import get_settings

settings = get_settings()

connect_args = {"check_same_thread": False, "auth_token": settings.turso_auth_token}

engine = create_engine(
    f"sqlite+{settings.database_url}?secure=true",
    pool_pre_ping=True,
    echo=settings.debug,
    connect_args=connect_args,
)


def init_db():
    """Inicializa la base de datos creando todas las tablas"""
    SQLModel.metadata.create_all(bind=engine)
