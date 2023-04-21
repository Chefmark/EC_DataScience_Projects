from pydantic import BaseModel

class Product(BaseModel):
    id: int = None
    name:str
    description:str = None
    stock: int
    price: float
    tax: float

