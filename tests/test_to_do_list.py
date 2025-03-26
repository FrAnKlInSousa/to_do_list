from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá, mundo!'}


def test_hello_deve_retornar_ola_mundo_em_html(client):
    response = client.get('/hello')
    assert response.status_code == HTTPStatus.OK
    assert 'Olá Mundo!' in response.text


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'string',
            'email': 'user@example.com',
            'password': 'string',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'string',
        'email': 'user@example.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'string',
                'email': 'user@example.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'frank',
            'email': 'frank@example.com',
            'id': 1,
            'password': '1233',
        },
    )
    assert response.json() == {
        'username': 'frank',
        'email': 'frank@example.com',
        'id': 1,
    }


def test_user_not_found(client):
    response = client.put(
        '/users/5',
        json={
            'username': 'frank',
            'email': 'frank@example.com',
            'id': 1,
            'password': '1234',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/user/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_not_found_user(client):
    response = client.delete('/user/5')
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_read_user_with_id(client):
    response_created = client.post(
        '/users/',
        json={
            'username': 'string',
            'email': 'user@example.com',
            'password': 'string',
        },
    )
    assert response_created.status_code == HTTPStatus.CREATED
    response = client.get('/users/1')
    assert response.json() == {
        'username': 'string',
        'email': 'user@example.com',
        'id': 1,
    }


def test_read_user_with_id_not_found(client):
    response = client.get('/users/3')
    assert response.status_code == HTTPStatus.NOT_FOUND
