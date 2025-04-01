from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from to_do_list.database import get_session
from to_do_list.models import Todo, User
from to_do_list.schemas import TodoPublic, TodoSchema
from to_do_list.security import get_current_user

router = APIRouter(prefix='/todos', tags=['todos'])

CurrentUser = Annotated[User, Depends(get_current_user)]
T_Session = Annotated[Session, Depends(get_session)]


@router.post('/', status_code=HTTPStatus.CREATED, response_model=TodoPublic)
def create_todo(todo: TodoSchema, session: T_Session, user: CurrentUser):
    db_todo = Todo(
        title=todo.title,
        description=todo.description,
        state=todo.state,
        user_id=user.id,
    )
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo
