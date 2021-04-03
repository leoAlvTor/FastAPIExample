from typing import List

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

import models, schemas
from database import SessionLocal

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True,
)

def get_database():
    global db
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get('/')
def main():
    return RedirectResponse(url='/docs/')


@app.get('/products/', response_model=List[schemas.Product])
def get_products(database: Session = Depends(get_database)):
    productos = database.query(models.Producto).all()
    return productos
