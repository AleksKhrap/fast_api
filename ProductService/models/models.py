from sqlalchemy import Column, Integer, String, Float
from .database import Base


class Products(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    weight = Column(Float)
    description = Column(String, default=None)
