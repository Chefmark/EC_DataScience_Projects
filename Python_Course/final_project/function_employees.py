from typing import List
import requests

from model_employee import Employee

def url(route:str):
    return f"http://127.0.0.1:8000{route}"
    
# The following class adds functions to work with the employee menu.
class Employee_menu:

    def create_employee():
        print("")
        print("Create a new employee")
        first_name_input = input("First name: ")
        last_name_input = input("Last name: ")
        employee_code_input = input("Add employee code (initials in capital and max 3 digits): ").upper()
        employee_type_input = input("Enter employee's role (employee/shiftleader/owner): ").lower()
        is_owner_input:str
        if employee_type_input == "owner":
            is_owner_input = "YES"
        else:
            is_owner_input = "NO"
        is_shiftleader_input:str
        if employee_type_input == "shiftleader":
            is_shiftleader_input = "YES"
        else:
            is_shiftleader_input = "NO"
        start_date_input = input("Enter startdate (YYYY-MM-DD): ")
        active = "YES"
        new_employee = Employee(employee_code=employee_code_input.upper(), first_name=first_name_input, last_name=last_name_input, emp_type=employee_type_input, is_owner=is_owner_input, is_shiftleader=is_shiftleader_input, start_date=start_date_input, active=active)
        res = requests.post(url("/employee/create_employee"), json=new_employee.dict())
        print(res)

    def get_all_employees():
        employees = []
        res = requests.get(url("/employee/print_employee/all"))
        if not res.status_code == 200:
            print("Error")
            return
        data = res.json()
        for employee in data:
            employee = Employee(**employee)
            employees.append(employee)
        return employees

    def print_all_employees(employees:List[Employee]):
        for employee in employees:
            print("_____________")
            print(f"Employee Code: {employee.employee_code}")
            print(f"First name: {employee.first_name}")
            print(f"Last name: {employee.last_name}")
            print(f"Role: {employee.emp_type}")
            print("For more details search the individuals employee code.")
            print("")
    
    def search_employee(employees: List[Employee]):
        get_employee_input = input("Enter the employee code that you wish to search for: ")
        print("Searching for employee...")
        index = None
        for i, employee in enumerate(employees):
            if employee.employee_code == get_employee_input:
                print("Employee found")
                index = i
                break
        if index == None:
            print("Can not find the employee, try again")
            return
        employee = employees[index]
        res = requests.get(url(f"/employee/search_employee/{get_employee_input}"))
        print("Printing Employee")
        print("_____________")
        print(f"Employee Id: {employee.id}")
        print(f"Employee Code: {employee.employee_code}")
        print(f"First name: {employee.first_name}")
        print(f"Last name: {employee.last_name}")
        print(f"Role: {employee.emp_type}")
        print(f"Start_date: {employee.start_date}")
        print(f"Is active: {employee.active.upper()}")
        return(res.json())

    def update_employee(employees: List[Employee]):
        print("Update employee")
        employee_update = input("Enter the employee code that you wish to update: ")
        index = None
        for i, employee in enumerate(employees):
            if employee.employee_code == employee_update:
                print("Employee found")
                index = i
                break
        if index == None:
            print("Can not find the employee, try again")
            return
        employee = employees[index]
        first_name_update = input("First name (leave blank if there is no update): ")
        last_name_update = input("Last name(leave blank if there is no update): ")
        employee_code_update = input("Add employee code (initials in capital and max 3 digits. Leave blank if there is no update): ").upper()
        employee_type_update = input("Enter employee's role (employee/shiftleader/owner. Leave blank if there is no update): ")
        is_owner_update:str
        if employee_type_update == "owner":
            is_owner_update = "YES"
        else:
            is_owner_update = "NO"
        is_shiftleader_update:str
        if employee_type_update == "shiftleader":
            is_shiftleader_update = "YES"
        else:
            is_shiftleader_update = "NO"
        start_date_update = input("Enter startdate (YYYY-MM-DD. Leave blank if there is no update): ")
        active_update = input("Is the employee still active(yes/no. Leave blank if there is no update): ").upper()
        
        if not first_name_update:
            first_name_update = employee.first_name
        if not last_name_update:
            last_name_update = employee.last_name
        if not employee_code_update:
            employee_code_update = employee.employee_code
        if not employee_type_update:
            employee_type_update = employee.emp_type
        if not is_owner_update:
            is_owner_update = employee.is_owner
        if not is_shiftleader_update:
            is_shiftleader_update = employee.is_shiftleader
        if not start_date_update:
            start_date_update = employee.start_date
        if not active_update:
            active_update = employee.active
        new_employee = Employee(employee_code=employee_code_update, first_name=first_name_update, last_name=last_name_update, emp_type=employee_type_update, is_owner=is_owner_update, is_shiftleader=is_shiftleader_update, start_date=start_date_update, active=active_update)
        res = requests.put(url(f"/employee/update_employee/{employee_update}"), json=new_employee.dict())
        print(res.json())

    def delete_employee():
        print("Delete employee")
        employee_delete_input = input("Enter the employee's id in order to delete an employee: ").strip()
        if not str.isdigit(employee_delete_input):
            print("IDs need to be integers.")
            return
        res = requests.delete(url(f"/employee/delete_employee/{employee_delete_input}"))
        print(res.json())


