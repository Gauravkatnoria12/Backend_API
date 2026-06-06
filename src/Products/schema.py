from pydantic import BaseModel

class ProductBase(BaseModel):
    id: int
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