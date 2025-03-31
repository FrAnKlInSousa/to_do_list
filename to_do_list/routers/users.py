from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from to_do_list.database import get_session
from to_do_list.models import User
from to_do_list.schemas import Message, UserList, UserPublic, UserSchema
from to_do_list.security import (
    get_current_user,
    get_password_hash,
)

router = APIRouter(prefix='/users', tags=['users'])


@router.post('/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema, session: Session = Depends(get_session)):
    db_user = session.scalar(
        select(User).where(
            (User.username == user.username) | (User.email == user.email)
        )
    )
    if db_user:
        if db_user.username == user.username:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Username already exists',
            )
        elif db_user.email == user.email:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Email already exists',
            )

    db_user = User(
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password),
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@router.get('/', response_model=UserList)
def read_users(
    session: Session = Depends(get_session),
    limit=10,
    skip=0,
):
    users_db = session.scalars(select(User).limit(limit).offset(skip))
    return {'users': users_db}


@router.get('/{user_id}', response_model=UserPublic)
def read_user(user_id: int, session: Session = Depends(get_session)):
    user = session.scalar(select(User).where(User.id == user_id))
    if not user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    return user


@router.put('/{user_id}', response_model=UserPublic)
def update_user(
    user_id: int,
    user: UserSchema,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    if current_user.id != user_id:
        raise HTTPException(
            HTTPStatus.UNAUTHORIZED, detail='Not enough permissions'
        )
    current_user.username = user.username
    current_user.email = str(user.email)
    current_user.password = get_password_hash(user.password)
    session.add(current_user)
    session.commit()
    session.refresh(current_user)
    return current_user


@router.delete('/{user_id}', response_model=Message)
def delete_user(
    user_id: int,
    session: Session = Depends(get_session),
    current_user=Depends(get_current_user),
):
    if user_id != current_user.id:
        raise HTTPException(
            HTTPStatus.UNAUTHORIZED, detail='Not enough permissions'
        )
    session.delete(current_user)
    session.commit()
    return {'message': 'User deleted'}
