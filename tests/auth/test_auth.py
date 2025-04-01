from datetime import datetime, timedelta
from http import HTTPStatus

from freezegun import freeze_time


def test_get_token(client, user):
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    test_token = response.json()
    assert response.status_code == HTTPStatus.CREATED
    assert test_token['token_type'] == 'Bearer'
    assert 'access_token' in test_token


def test_get_token_incorrect_email(client, user):
    data = {'username': 'wrong_email@test.com', 'password': user.password}
    response = client.post('/auth/token', data=data)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Incorrect email or password'}


def test_get_token_incorrect_password(client, user):
    data = {'username': user.email, 'password': 'wrong_pass'}
    response = client.post('/auth/token', data=data)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Incorrect email or password'}


def test_token_expire_after_time(client, user):
    with freeze_time('2025-03-30 12:00:00'):
        data = {'username': user.email, 'password': user.clean_password}
        response = client.post('/auth/token', data=data)
        assert response.status_code == HTTPStatus.CREATED
        my_token = response.json().get('access_token')

    with freeze_time('2025-03-30 12:31:00'):
        response = client.put(
            f'/users/{user.id}',
            headers={'Authorization': f'Bearer {my_token}'},
            json={
                'username': 'wrong',
                'email': 'wrong@wrong.com',
                'password': 'wrong',
            },
        )
        assert response.status_code == HTTPStatus.UNAUTHORIZED
        assert response.json() == {'detail': 'Could not validate credentials'}


def test_refresh_token(client, token):
    response = client.post(
        'auth/refresh_token', headers={'Authorization': f'Bearer {token}'}
    )
    data = response.json()
    assert response.status_code == HTTPStatus.CREATED
    assert 'access_token' in data
    assert data['token_type'] == 'Bearer'


def test_token_expired_dont_refresh(client, user):
    now = datetime.now()
    with freeze_time(now):
        data = {'username': user.email, 'password': user.clean_password}
        response = client.post('/auth/token', data=data)
        assert response.status_code == HTTPStatus.CREATED
        my_token = response.json()['access_token']
    with freeze_time(now + timedelta(minutes=30)):
        response = client.post(
            'auth/refresh_token',
            headers={'Authorization': f'Bearer {my_token}'},
        )
        assert response.status_code == HTTPStatus.UNAUTHORIZED
        assert response.json() == {'detail': 'Could not validate credentials'}
