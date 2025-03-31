from http import HTTPStatus

from jwt import decode

from to_do_list.security import create_access_token, settings


def test_jwt():
    data = {'sub': 'test@test.com'}
    token_jwt = create_access_token(data)

    result = decode(token_jwt, settings.SECRET_KEY, [settings.ALGORITHM])
    assert result['sub'] == data['sub']
    assert result['exp']


def test_jwt_invalid_token(client):
    response = client.delete(
        '/users/1', headers={'Authorization': 'Bearer token-invalido'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_get_current_user_username_invalid(session, client, user):
    data = {'sub': 'wrong_email@test.com'}
    token_jwt = create_access_token(data)
    response = client.delete(
        'users/1', headers={'Authorization': f'Bearer {token_jwt}'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_get_current_user_without_sub(session, client, user):
    data = {}
    token_jwt = create_access_token(data)
    response = client.delete(
        'users/1', headers={'Authorization': f'Bearer {token_jwt}'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}
