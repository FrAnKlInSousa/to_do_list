from sqlalchemy import select

from to_do_list.models import User


def test_create_user(session, mock_db_time):
    user = User(
        username='franklin', email='frank@frank.com', password='mysecret'
    )
    session.add(user)
    session.commit()
    # session.refresh(user)  # atualiza o obj com o que está no db
    result = session.scalar(
        select(User).where(User.email == 'frank@frank.com')
    )
    assert result.id == 1
    assert result.username == 'franklin'


# def test_update_user(session, client):
#     user = User(
#         username='franklin', email='frank@frank.com', password='mysecret'
#     )
#     session.add(user)
#     session.commit()
#
#     user.username = 'frank'
#     session.add(user)
#     session.commit()
#
#     result = session.scalar(select(User).where(User.id == 1))
#     assert result.username == 'frank'
