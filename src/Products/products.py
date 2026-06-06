from fastapi import APIRouter, HTTPException, Depends, status
from typing import Annotated

from .schema import ProductBase, ProductCreate, ProductResponse
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


@route.get("/", response_model=list[ProductResponse], status_code=status.HTTP_200_OK)
async def get_all_prod(db: db_dependency):
    products = db.query(models.Products).all()
    if products:
        return products
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Products Not Found")

@route.post("/product", status_code=status.HTTP_201_CREATED, response_model=ProductResponse)
async def add_prod(product : ProductCreate, db: db_dependency):
    products = db.query(models.Products).all()
    new_id = max(item.id for item in products) + 1 if products else 1
    new_prod = {
        "id" : new_id,
        **product.model_dump()
    }
    db_product = models.Products(**new_prod)
    db.add(db_product)
    db.commit()
    return new_prod