.PHONY: install install-dev format lint lint-format test run check pre-commit init-db clean help

UV=uv run

install:
	uv sync --group prod

install-dev:
	uv sync --group dev

format:
	$(UV) black .
	$(UV) isort .

lint:
	$(UV) ruff check . --fix

lint-format:
	$(UV) ruff check . --fix
	$(UV) black --check .
	$(UV) isort --check-only .
	$(UV) zuban mypy --warn-unreachable

test:
	$(UV) pytest

run:
	$(UV) fastapi dev app/main.py

check: lint-format test

pre-commit:
	$(UV) pre-commit run --all-files

init-db:
	$(UV) python -c "from app.db.init_db import initialize; initialize()"

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +

help:
	@echo "Comandos disponibles:"
	@echo "  install        Instala dependencias de producción"
	@echo "  install-dev    Instala dependencias de desarrollo"
	@echo "  format         Formatea el código con black e isort"
	@echo "  lint           Linting automático con ruff"
	@echo "  lint-format    Lint + chequeo de formato y tipos"
	@echo "  test           Ejecuta los tests"
	@echo "  run            Ejecuta la app en modo desarrollo"
	@echo "  check          Lint + test"
	@echo "  pre-commit     Ejecuta todos los hooks de pre-commit"
	@echo "  init-db        Inicializa la base de datos"
	@echo "  clean          Limpia archivos temporales y cachés"
