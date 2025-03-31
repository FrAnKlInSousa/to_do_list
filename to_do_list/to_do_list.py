from http import HTTPStatus

from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse

from to_do_list.routers import auth, users
from to_do_list.schemas import Message

app = FastAPI()
app.include_router(users.router)
app.include_router(auth.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá, mundo!'}


@app.get('/hello', status_code=status.HTTP_200_OK, response_class=HTMLResponse)
def hello():
    return """
    <html>
        <head>
        <title>Nosso olá mundo!</title>
        </head>
        <body>
        <h1> Olá Mundo! </h1>
        </body>
        </html>"""
