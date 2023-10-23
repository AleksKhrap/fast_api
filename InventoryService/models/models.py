from sqlalchemy import Column, String, Float
from .database import Base


class Inventory(Base):
    __tablename__ = "inventory"

    product_id = Column(String)
    product_name = Column(String)
    quantity_on_inventory = Column(Float)
    current_price = Column(String)
