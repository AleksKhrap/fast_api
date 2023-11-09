from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    quantity: int
    cost: float


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    pass


class Item(ItemBase):
    order_id: int
    item_id: int

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    order_date: str


class OrderCreate(OrderBase):
    pass


class OrderUpdate(OrderBase):
    pass


class Order(OrderBase):
    order_id: int
    items: list[Item] = []

    class Config:
        orm_mode = True
