from app.api.deps import session_local

def get_db():
    """
    Dependencia para obtener una sesión de base de datos.
    Cierra la sesión automáticamente al finalizar el request.
    """
    db = session_local()
    try:
        yield db
    finally:
        db.close()
