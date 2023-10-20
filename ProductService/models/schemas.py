from typing import Union
from pydantic import BaseModel


class Products(BaseModel):
    id: Union[int, None]
    name: str
    weight: float
    description: Union[str, None] = None