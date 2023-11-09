from sqlalchemy import Column, Integer, String, Float
from ProductService.app.db.database import Base


class Products(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    weight = Column(Float)
    description = Column(String)
