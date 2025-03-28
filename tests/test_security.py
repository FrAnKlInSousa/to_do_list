from jwt import decode

from to_do_list.security import ALGORITHM, SECRET_KEY, create_access_token


def test_jwt():
    data = {'sub': 'test@test.com'}
    token = create_access_token(data)

    result = decode(token, SECRET_KEY, [ALGORITHM])
    assert result['sub'] == data['sub']
    assert result['exp']
