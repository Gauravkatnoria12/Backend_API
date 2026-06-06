from pydantic import BaseModel, Field, ConfigDict

class ProductBase(BaseModel):
    name: str
    price: float
    category: str
    in_stock: bool
    rating: float
    image: str
    sku: str
    description: str
    stock_count: int
    brand: str
    discount_price: float

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id : int