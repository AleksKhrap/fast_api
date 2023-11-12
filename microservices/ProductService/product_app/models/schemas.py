from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    weight: float
    description: str


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    product_id: str

    class Config:
        orm_mode = True
