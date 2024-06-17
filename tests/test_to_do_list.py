from http import HTTPStatus

from fastapi.testclient import TestClient

from to_do_list.to_do_list import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}
