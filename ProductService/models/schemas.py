from typing import Union
from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    weight: float
    description: Union[str, None] = None


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    product_id: Union[int, None]

    class Config:
        orm_mode = True
