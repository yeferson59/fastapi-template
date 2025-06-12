# app/db/init_db.py

from app.db.base import init_db
# Importa aquí tus modelos si necesitas crear datos iniciales (seed)
# from app.models.user import User

def initialize():
    """
    Inicializa la base de datos y opcionalmente agrega datos iniciales (seed).
    Llama esta función en el evento de startup o desde un script manual.
    """
    # Crea las tablas según los modelos declarados
    init_db()

    # Ejemplo de seed opcional:
    # db = SessionLocal()
    # try:
    #     if not db.query(User).filter_by(username="admin").first():
    #         user = User(username="admin", email="admin@example.com")
    #         db.add(user)
    #         db.commit()
    # finally:
    #     db.close()
