from http import HTTPStatus


def test_get_token(client, user):
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    test_token = response.json()
    assert response.status_code == HTTPStatus.OK
    assert test_token['token_type'] == 'Bearer'
    assert 'access_token' in test_token


def test_get_token_incorrect_email(client, user):
    data = {'username': 'wrong_email@test.com', 'password': user.password}
    response = client.post('/auth/token', data=data)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Incorrect email or password'}


def test_get_token_incorrect_password(client, user):
    data = {'username': user.email, 'password': 'wrongpass'}
    response = client.post('/auth/token', data=data)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Incorrect email or password'}
