from pydantic import BaseModel

#class used to create members
class Member(BaseModel):
    id: int = None 
    first_name: str
    last_name: str
    phone_number: str
    email: str