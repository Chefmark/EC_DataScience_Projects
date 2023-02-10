from pydantic import BaseModel

#class used for creation of employees.

class Employee(BaseModel):
    employee_code: str
    first_name: str
    last_name: str
    emp_type: str
    is_owner: bool
    if emp_type == "owner":
        is_owner = True
    else: 
        is_owner = False
    is_shiftleader: bool
    if emp_type == "shiftleader":
        is_shiftleader = True
    else:
        is_shiftleader = False
    active: str

class Member(BaseModel):
    id: int
    first_name: str
    last_name: str
    phone_number: str
    email: str