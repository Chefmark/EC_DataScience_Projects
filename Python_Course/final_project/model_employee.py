from pydantic import BaseModel


#class used for creation of employees.

class Employee(BaseModel):
    id:int = None
    employee_code: str
    first_name: str
    last_name: str
    emp_type: str
    is_owner: str
    is_shiftleader: str
    start_date: str
    active: str
