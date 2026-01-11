import sys
import os
import pytest
from fastapi.testclient import TestClient

# Permet d'importer le dossier app/
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)

from app.main import app


@pytest.fixture(scope="session")
def client():
    """
    Client de test FastAPI partagé pour tous les tests.
    """
    with TestClient(app) as test_client:
        yield test_client
