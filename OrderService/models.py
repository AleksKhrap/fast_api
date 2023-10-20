from pydantic import BaseModel


class OrderItem(BaseModel):
    product_id: str
    product_name: str
    quantity: int
    cost: float


class Order(BaseModel):
    order_id: str
    order_date: str
    order_items: list[OrderItem]
