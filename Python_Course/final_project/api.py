from typing import List
from fastapi import FastAPI

from db import DB
from model_employee import Employee
from model_member import Member

# http://127.0.0.1:8000

app = FastAPI()
db = DB("store_api.db")

@app.get("/")
def root():
    return "Store api"

# -- Code to add orders

@app.put("/order/new_order")
def add_new_order():
    pass


# -- Code for members menu -- 

@app.post("/member/create_member")
def create_member(member:Member):
    pass

@app.get("/member/search_member/{last_name}")
def search_member(last_name:str):
    pass

@app.put("/member/update_member/{id}")
def update_member(id:int):
    pass

@app.delete("/member/delete_member/{id}")
def delete_member(id:int):
    pass

# -- code for employee menu --

@app.post("/employee/create_employee")
def create_employee(employee: Employee):
    insert_query = """
    INSERT INTO employees (employee_code, first_name, last_name, emp_type, is_owner, is_shiftleader, start_date, active)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    db.call_db(insert_query, employee.employee_code.upper(), employee.first_name, employee.last_name, employee.emp_type, employee.is_owner, employee.is_shiftleader, employee.start_date, employee.active)
    return "creating new employee"

@app.get("/employee/print_employee/all")
def get_employee_all():
    get_employee_all_query = """
    SELECT * 
    FROM employees
    """
    data = db.call_db(get_employee_all_query)
    employees = []
    for i in data:
        id, employee_code, first_name, last_name, emp_type, is_owner, is_shiftleader, start_date, active = i
        employees.append(Employee(id=id, employee_code=employee_code, first_name=first_name, last_name=last_name, emp_type=emp_type, is_owner=is_owner, is_shiftleader=is_shiftleader, start_date=start_date, active=active))
    return employees

@app.get("/employee/search_employee/{employee_code}")
def get_employee_one(employee_code:str):
    get_employee_query = """
    SELECT * 
    FROM employees
    WHERE employee_code = ?
    """
    db.call_db(get_employee_query, employee_code)
    return True

@app.put("/employee/update_employee/{employee_code}")
def update_employee(employee_code:str, new_employee: Employee):
    update_employee_query= """
    UPDATE employees
    SET employee_code = ?, first_name = ?, last_name =?, emp_type = ?, is_owner = ?, is_shiftleader = ?, start_date = ?, active = ?
    WHERE employee_code = ?
    """
    db.call_db(update_employee_query, new_employee.employee_code, new_employee.first_name, new_employee.last_name, new_employee.emp_type, new_employee.is_owner, new_employee.is_shiftleader, new_employee.start_date, new_employee.active, employee_code)
    return True

@app.delete("/employee/delete_employee/{id}")
def delete_employee(id:int):
    delete_query = """
    DELETE FROM employees WHERE id = ?
    """
    db.call_db(delete_query, id)
    return True
    

# -- Code for inventory

@app.post("/inventory/add_product")
def add_product():
    pass

@app.get("/inventory/print_inventory/")
def print_product():
    pass

@app.put("/inventory/update_product/{id}")
def update_product(id:int):
    pass

@app.delete("/inventory/delete_product/{id}")
def delete_product(id:int):
    pass

# -- Code for Statistics --

@app.get("/statistics/print_stats")
def print_stats():
    pass
