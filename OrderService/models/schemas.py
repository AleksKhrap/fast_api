from typing import Union
from pydantic import BaseModel


class OrderItemBase(BaseModel):
    name: str
    quantity: int
    cost: float


class OrderItemCreate(OrderItemBase):
    pass


class OrderItem(OrderItemBase):
    id: Union[int, None]
    order_item_id: int


class OrderBase(BaseModel):
    order_date: str


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: Union[int, None]
    items: list[OrderItem] = []

    class Config:
        orm_mode = True
