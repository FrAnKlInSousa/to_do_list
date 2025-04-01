from http import HTTPStatus


def test_create_todo(client, token):
    response = client.post(
        '/todos/',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'title': 'title test',
            'description': 'description test',
            'state': 'draft',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    data = {
        'id': 1,
        'title': 'title test',
        'description': 'description test',
        'state': 'draft',
    }
    assert data == response.json()
