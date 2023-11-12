from pydantic import BaseModel
from uuid import UUID


class InventoryBase(BaseModel):
    product_name: str
    quantity_on_inventory: float
    current_price: float


class InventoryCreate(InventoryBase):
    pass


class InventoryUpdate(InventoryBase):
    pass


class Inventory(InventoryBase):
    product_id: UUID

    class Config:
        orm_mode = True
