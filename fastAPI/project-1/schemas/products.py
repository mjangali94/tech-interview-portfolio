from typing import Optional

from pydantic import BaseModel


class Category(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class Product(BaseModel):
    id:int
    name:str
    description:str
    price:float
    available:bool
    category_id:Optional[int] =None

    class Config:
        from_attributes = True

