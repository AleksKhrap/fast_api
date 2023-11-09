from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Order(Base):
    __tablename__ = "order"

    order_id = Column(Integer, primary_key=True, index=True)
    order_date = Column(Date)

    items = relationship("OrderItem", back_populates="order_item_id")


class OrderItem(Base):
    __tablename__ = "order_item"

    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    quantity = Column(Integer)
    cost = Column(Float)
    order_item_id = Column(Integer, ForeignKey("order.id"))

    order_item = relationship("Order", back_populates="items")
