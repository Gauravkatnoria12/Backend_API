from sqlalchemy import Boolean, Column, Integer, String, Float
from .database import Base

class Products(Base):
    __tablename__ = 'data'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String(50), index=True, nullable=False)
    in_stock = Column(Boolean, default=True, nullable=False)
    rating = Column(Float, default=0.0, nullable=False)
    image = Column(String(255), default="default.jpg", nullable=False)
    sku = Column(String(50), unique=True, index=True, nullable=False)
    description = Column(String(1000), nullable=False)
    stock_count = Column(Integer, default=0, nullable=False)
    brand = Column(String(50), index=True, nullable=False)
    discount_price = Column(Float, default=0.0, nullable=False)
