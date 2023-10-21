from typing import Union
from pydantic import BaseModel


class ProductsBase(BaseModel):
    name: str
    weight: float
    description: Union[str, None] = None


class ProductCreate(ProductsBase):
    pass


class Product(ProductsBase):
    id: Union[int, None]

    class Config:
        orm_mode = True
