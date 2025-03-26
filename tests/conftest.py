import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from to_do_list.models import table_registry
from to_do_list.to_do_list import app


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture()
def session():
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session  # live 43 e 151 (gerenciamento de contexto)
    table_registry.metadata.drop_all(engine)
