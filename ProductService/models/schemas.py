from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    weight: float
    description: str | None


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    product_id: int

    class Config:
        orm_mode = True
