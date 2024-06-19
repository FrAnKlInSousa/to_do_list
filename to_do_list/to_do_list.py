from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse

from to_do_list.schemas import Message

app = FastAPI()


@app.get('/', status_code=status.HTTP_200_OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/hello', status_code=status.HTTP_200_OK, response_class=HTMLResponse)
def hello():
    return """
<html>
<head>
<title>Olá mundo!</title>
</head>
<body>
<h1> Olá Mundo </h1>
</body>
</html>"""
