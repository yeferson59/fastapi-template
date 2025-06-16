import os
import sys

# Asegura que el directorio raíz esté en sys.path antes de importar app
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_path not in sys.path:
    sys.path.insert(0, root_path)

import pytest

from app.db.base import init_db


@pytest.fixture(scope="session", autouse=True)
def initialize_database():
    """Inicializa la base de datos antes de correr los tests."""
    init_db()
