from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=200, response_model=Message)
def read_root():
    return {'message': 'Ola Mundo!'}


@app.get('/exe2', response_class=HTMLResponse)
def exe2():
    return """
    <html>
        <head>
            <title>Exercicio 2</title>
        </head>
        <body>
            <h1>Ola Mundo!</h1>
        </body>
    </html>
    """
