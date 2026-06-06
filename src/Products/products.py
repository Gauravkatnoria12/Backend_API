from fastapi import APIRouter, HTTPException, Depends, status
from typing import Annotated

from .schema import ProductBase
from . import models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

route = APIRouter()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@route.post("/", status_code=status.HTTP_201_CREATED)
async def add_prod(product : ProductBase, db: db_dependency):
  db_product = models.Products(**product.model_dump())
  db.add(db_product)
  db.commit()