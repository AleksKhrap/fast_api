from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from OrderService.app.db.database import Base


class Order(Base):
    __tablename__ = "order"

    order_id = Column(Integer, primary_key=True, index=True)
    order_date = Column(Date)

    items = relationship("Item", back_populates="order_items")


class Item(Base):
    __tablename__ = "item"

    order_id = Column(Integer, ForeignKey("order.id"), index=True)
    item_id = Column(Integer, index=True)
    name = Column(String)
    quantity = Column(Integer)
    cost = Column(Float)

    order_items = relationship("Order", back_populates="items")
