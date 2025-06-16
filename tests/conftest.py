import os
import sys

import pytest

from app.db.base import init_db

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture(scope="session", autouse=True)
def initialize_database():
    """Inicializa la base de datos antes de correr los tests."""
    init_db()
