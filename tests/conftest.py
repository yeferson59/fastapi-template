import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest

from app.db.base import init_db


@pytest.fixture(scope="session", autouse=True)
def initialize_database():
    """Inicializa la base de datos antes de correr los tests."""
    init_db()
