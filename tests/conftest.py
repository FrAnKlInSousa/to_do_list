import pytest
from fastapi.testclient import TestClient

from to_do_list.to_do_list import app


@pytest.fixture()
def client():
    return TestClient(app)
