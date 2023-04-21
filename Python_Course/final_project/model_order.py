from pydantic import BaseModel

class Order(BaseModel):
    id: int = None
    employee_code:str
    member_id: int = None
    total_price: float
    tax_total: float
    
