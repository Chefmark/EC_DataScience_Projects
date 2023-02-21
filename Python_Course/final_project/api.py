from typing import List
from fastapi import FastAPI
import sqlite3

from db import DB
from model_employee import Employee
from model_member import Member
from model_product import Product
from model_order import Order
from model_order_details import Order_detail

# http://127.0.0.1:8000

app = FastAPI()
db = DB("store_api.db")

@app.get("/")
def root():
    return "Store api"

# -- Code to seed environment --

@app.post("/seed/admin")
def seed_admin(employee: Employee):
    insert_query = """
    INSERT INTO employees (employee_code, first_name, last_name, emp_type, is_owner, is_shiftleader, start_date, active)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    db.call_db(insert_query, employee.employee_code.upper(), employee.first_name, employee.last_name, employee.emp_type, employee.is_owner, employee.is_shiftleader, employee.start_date, employee.active)
    return "creating new admin"

# -- Code to for Order menu
@app.post("/order/new_order")
def add_new_order(order: Order):
    insert_query = """
    INSERT INTO orders (employee_code, member_id, total_price, tax_total)
    VALUES (?, ?, ?, ?)
    """
    db.call_db(insert_query,order.employee_code, order.member_id, order.total_price, order.tax_total)
    return "adding order to orders"

@app.get("/order/all_orders")
def get_all_orders():
    get_all_orders_query = """
    SELECT *
    FROM orders
    """
    data = db.call_db(get_all_orders_query)
    orders = []
    for i in data:
        id, employee_code, member_id, total_price, tax_total = i
        orders.append(Order(id=id, employee_code=employee_code, member_id=member_id, total_price=total_price, tax_total=tax_total))
    return orders

@app.get("/order/most_recent_order")
def get_most_recent_order():
    get_most_recent_order_query = """
    SELECT *
    FROM orders
    ORDER BY id DESC
    LIMIT 1
    """
    data_id = db.call_db(get_most_recent_order_query)
    for i in data_id:
        id, employee_code, member_id, total_price, tax_total = i
        most_recent_order = Order(id=id, employee_code=employee_code, member_id=member_id, total_price=total_price, tax_total=tax_total)
        return most_recent_order

@app.post("/order/new_order_detail")
def add_order_detail(order_detail: Order_detail):
    insert_new_order_detail_query = """
    INSERT INTO order_details (product_id, product_name, product_price, 
    product_tax, amount, order_id, subtax, subtotal)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    db.call_db(insert_new_order_detail_query, order_detail.product_id, order_detail.product_name,
     order_detail.product_price, order_detail.product_tax, order_detail.amount, order_detail.order_id,
      order_detail.subtax, order_detail.subtotal)
    return "adding new order_detail"
# -- Code for members menu -- 

@app.post("/member/create_member")
def create_member(member:Member):
    insert_query = """
    INSERT INTO members (first_name, last_name, phone_number, email)
    VALUES (?, ?, ?, ?)
    """
    db.call_db(insert_query, member.first_name, member.last_name, member.phone_number, member.email)
    return "creating new member"

@app.get("/member/all")
def get_all_members():
    get_all_members_query = """
    SELECT *
    FROM members
    """
    data = db.call_db(get_all_members_query)
    members = []
    for i in data:
        id, first_name, last_name, phone_number, email = i
        members.append(Member(id=id, first_name=first_name, last_name=last_name, 
        phone_number=phone_number, email=email))
    return members

@app.get("/member/search_member/{last_name}")
def search_member(last_name:str):
    get_member_query= """
    SELECT * 
    FROM members
    WHERE last_name = ?
    """
    db.call_db(get_member_query, last_name)
    return "searching for member"

@app.put("/member/update_member/{id}")
def update_member(id:int, new_member:Member):
    update_member_query= """
    UPDATE members
    SET first_name = ?, last_name =?, phone_number = ?, email = ?
    WHERE id = ?
    """
    db.call_db(update_member_query, new_member.first_name, 
    new_member.last_name, new_member.phone_number, new_member.email, id)
    return "Updating member"

@app.delete("/member/delete_member/{id}")
def delete_member(id:int):
    delete_query = """
    DELETE FROM members 
    WHERE id = ?
    """
    db.call_db(delete_query, id)
    return "Deleting member"

# -- code for employee menu --

@app.post("/employee/create_employee")
def create_employee(employee: Employee):
    insert_query = """
    INSERT INTO employees (employee_code, first_name, last_name, emp_type, is_owner, is_shiftleader start_date, active)
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
        employees.append(Employee(id=id, employee_code=employee_code, 
        first_name=first_name, last_name=last_name, emp_type=emp_type, 
        is_owner=is_owner, is_shiftleader=is_shiftleader, start_date=start_date,
         active=active))
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
    db.call_db(update_employee_query, new_employee.employee_code,
     new_employee.first_name, new_employee.last_name, new_employee.emp_type, 
     new_employee.is_owner, new_employee.is_shiftleader, new_employee.start_date,
      new_employee.active, employee_code)
    return "Updating employee"

@app.delete("/employee/delete_employee/{id}")
def delete_employee(id:int):
    delete_query = """
    DELETE FROM employees WHERE id = ?
    """
    db.call_db(delete_query, id)
    return "Deleting employee"
    

# -- Code for inventory

@app.post("/inventory/add_product")
def add_product(product: Product):
    insert_query = """
    INSERT INTO products (name, description, stock, price, tax)
    VALUES (?, ?, ?, ?, ?)
    """
    db.call_db(insert_query, product.name, product.description, product.stock, product.price, product.tax)
    return "creating new product"

@app.get("/inventory/print_inventory/")
def print_product():
    get_all_products_query = """
    SELECT *
    FROM products
    """
    data = db.call_db(get_all_products_query)
    products = []
    for i in data:
        id, name, description, stock, price, tax = i
        products.append(Product(id=id, name=name, 
        description=description, stock=stock, price=price, 
        tax=tax))
    return products

@app.put("/inventory/update_product/{id}")
def update_product(id:int, new_product:Product):
    update_product_query = """
    UPDATE products
    SET name = ?, description = ?, stock = ?, price = ?, tax = ?
    WHERE id = ?
    """
    db.call_db(update_product_query, new_product.name, 
    new_product.description, new_product.stock, new_product.price,
     new_product.tax, id)
    return "Updating product"
    

@app.delete("/inventory/delete_product/{id}")
def delete_product(id:int):
    delete_product_query = """
    DELETE FROM products WHERE id = ?
    """
    db.call_db(delete_product_query, id)
    return "Deleting product"

# -- Code for Statistics --

@app.get("/statistics/total_sales")
def print_total_sales():
    conn = sqlite3.connect("store_api.db")
    total_sales_query = """
    SELECT SUM(total_price), SUM(tax_total)
    FROM orders
    """
    cursor = conn.execute(total_sales_query)
    data = cursor.fetchone()
    conn.close()
    sum_total_price, sum_total_tax = data
    return f"The total sales is ${sum_total_price} of which the tax is ${sum_total_tax}"

@app.get("/statistics/member_count")
def print_member_count():
    conn = sqlite3.connect("store_api.db")
    member_count_query = """
    SELECT COUNT(first_name)
    FROM members
    WHERE first_name IS NOT 'Guest'
    """
    cursor = conn.execute(member_count_query)
    data = cursor.fetchone()
    conn.close()
    member_count = data[0]
    return f"The total amount of members (that are not guests) = {member_count}"

@app.get("/statistics/guest_count")
def print_guest_count():
    conn = sqlite3.connect("store_api.db")
    guest_count_query = """
    SELECT COUNT(first_name)
    FROM members
    WHERE first_name = 'Guest'
    """
    cursor = conn.execute(guest_count_query)
    data = cursor.fetchone()
    conn.close()
    guest_count = data[0]
    return f"The total amount of guests = {guest_count}"
