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


@route.get("/", response_model=list[ProductBase], status_code=status.HTTP_200_OK)
async def get_all_prod(db: db_dependency):
    products = db.query(models.Products).all()
    if products:
        return products
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Products Not Found")

@route.post("/product", status_code=status.HTTP_201_CREATED)
async def add_prod(product : ProductBase, db: db_dependency):
  db_product = models.Products(**product.model_dump())
  db.add(db_product)
  db.commit()