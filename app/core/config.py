"""Application configuration settings."""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Database configuration: defaults to SQLite located in the project root
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR}/studymanager.db")

APP_TITLE = "StudyManager API"
APP_DESCRIPTION = (
    "API RESTful para gerenciamento de Usuários, Cursos e Matrículas, "
    "desenvolvida seguindo os princípios de Arquitetura Limpa e Clean Code."
)
APP_VERSION = "1.0.0"
