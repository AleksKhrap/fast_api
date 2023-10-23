from pydantic import BaseModel


class InventoryBase(BaseModel):
    product_name: str
    quantity_on_inventory: float
    current_price: str


class InventoryCreate(InventoryBase):
    pass


class Inventory(InventoryBase):
    product_id: str

    class Config:
        orm_mode = True
