from sqlalchemy import Column, String, Float
from ProductService.product_app.db.database import Base


class Products(Base):
    __tablename__ = "products"

    product_id = Column(String, primary_key=True)
    name = Column(String)
    weight = Column(Float)
    description = Column(String)
