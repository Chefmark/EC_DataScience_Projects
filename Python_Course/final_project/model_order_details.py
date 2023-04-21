from pydantic import BaseModel

class Order_detail(BaseModel):
    id: int = None
    product_id:int
    product_name:str 
    product_price:float
    product_tax:float
    amount: int
    order_id: int
    subtax:float
    subtotal:float