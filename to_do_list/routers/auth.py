from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session

from to_do_list.database import get_session
from to_do_list.models import User
from to_do_list.schemas import Token
from to_do_list.security import (
    create_access_token,
    verify_password,
)

router = APIRouter(prefix='/auth', tags=['auth'])
T_OAuthForm = Annotated[OAuth2PasswordRequestForm, Depends()]
T_Session = Annotated[Session, Depends(get_session)]


@router.post('/token', status_code=HTTPStatus.CREATED, response_model=Token)
def login_for_access_token(
    form_data: T_OAuthForm,
    session: T_Session,
):
    user = session.scalar(select(User).where(User.email == form_data.username))
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            HTTPStatus.BAD_REQUEST, detail='Incorrect email or password'
        )
    access_token = create_access_token(data={'sub': user.email})
    return {'access_token': access_token, 'token_type': 'Bearer'}
