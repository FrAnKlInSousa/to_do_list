from http import HTTPStatus

from to_do_list.schemas import UserPublic


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


def test_create_user_same_username(client, user):
    response = client.post(
        '/users/',
        json={
            'username': user.username,
            'email': 'testnew@test.com',
            'password': '1233',
        },
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_user_same_user_email(client, user):
    print(user.email)
    response = client.post(
        '/users/',
        json={
            'username': 'Test2',
            'email': user.email,
            'password': '1233',
        },
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_user_with_user(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user, token):
    response = client.put(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'frank',
            'email': 'frank@example.com',
            'id': user.id,
            'password': '1233',
        },
    )
    assert response.json() == {
        'username': 'frank',
        'email': 'frank@example.com',
        'id': user.id,
    }


def test_update_another_user(client, user, token):
    response = client.put(
        f'/users/{user.id + 1}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'frank',
            'email': 'frank@example.com',
            'id': user.id,
            'password': '1233',
        },
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permissions'}


def test_delete_user(client, user, token):
    response = client.delete(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_another_user(client, user, token):
    response = client.delete(
        f'/users/{user.id + 1}',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permissions'}


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
