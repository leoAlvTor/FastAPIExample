from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return 'Hey from FastAPI'


@app.get('/name')
def index():
    return {'Name': 'Leo Alvarado!'}
