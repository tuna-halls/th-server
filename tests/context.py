import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from tunahalls.api import app
import pytest


@pytest.fixture(scope="session")
def anon_client():
    return TestClient(app)


# TODO: Setup tests database
