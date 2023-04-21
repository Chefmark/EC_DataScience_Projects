from typing import List
import requests

#Local imports
from function_print_menu import Menu
from function_employees import Employee_menu
from function_members import Member_menu
from function_inventory import Inventory_menu
from function_seed import Seed_data
from function_orders import New_order
from function_statistics import Statistics
from db import DB
from model_employee import Employee

#Log in function that takes employment ID or exit to close program.
#There is a hidden command to seed data.
def log_in():
    access = False
    while not access:
        log_input = input("Please enter your employee ID or type exit to close program: ")
        if log_input == "exit":
            print("Closing program")
            exit()
        #The following if statement is a hidden command to seed an admin user (should only be used once)
        #Allows to seed data for a demo purpose
        if log_input == "seed_admin": 
            Seed_data.seed_admin()
            demo_loop = False
            while not demo_loop:
                demo_choice = input("would you like to seed for demo? (y/n): ")
                match(demo_choice):
                    case "y":
                        print("seeding for demo")
                        Seed_data.seed_demo()
                        demo_loop = True
                    case "n":
                        print("will not seed for demo")
                        demo_loop = True
                    case _:
                        print("Error, incorrect input try again")
        if log_input !="exit" and log_input != "seed_admin":
            employees = Employee_menu.get_all_employees()
            access = check_login(log_input, employees)
            
        
#Function checks that the user exists
def check_login(log_input:str, employees: List[Employee]):
    index = None
    for i, employee in enumerate(employees):
        if employee.employee_code == log_input:
            print(f"Welcome {employee.first_name}")
            index = i
            return True
    if index == None:
        print("You do not have access, try again")
        return False
        
def main():

    log_in()
    
    logged_in = True
    # A while loop when the user is logged in
    while logged_in:
        Menu.print_menu_main()
        choice = input("What would you like to do?: ")
        choice = choice.strip()
        if not str.isdigit(choice):
            print("")
            print("Error, wrong input. Try again")
            print("")
            return
        
        match int(choice):
            case 1: # Order menu (for everyone)
                order_choice = True
                while order_choice:
                    Menu.print_menu_orders()
                    ch_order = input("What would you like to do?: ")
                    ch_order = ch_order.strip()
                    if not str.isdigit(ch_order):
                        print("")
                        print("Error, wrong input. Try again")
                        print("")
                    match int(ch_order):
                        case 1:
                            New_order.display_menu()
                            
                        case 2: 
                            print("returning to main menu")
                            order_choice = False
                        case _:
                            print("")
                            print("Error, wrong input. Try again")
                            print("")

            case 2: # Member menu (for everyone)
                member_choice = True
                while member_choice:
                    Menu.print_menu_members()
                    ch_members = input("What would you like to do?: ")
                    ch_members = ch_members.strip()
                    if not str.isdigit(ch_members):
                        print("")
                        print("Error, wrong input. Try again")
                        print("")
                
                    match int(ch_members):
                        case 1: #Create a new member
                            Member_menu.create_member()
                        case 2: #Search for a member
                            members = Member_menu.get_all_members()
                            print("All members have been found")
                            Member_menu.search_member(members)
                        case 3: #Update a member
                            members = Member_menu.get_all_members()
                            Member_menu.update_member(members)
                        case 4: #Delete a member
                            Member_menu.delete_member()
                        case 5: #Returns to main menu
                            print("returning to main menu")
                            member_choice = False
                        case _:
                            print("")
                            print("Error, wrong input. Try again")
                            print("")                    

            case 3: # Employee menu (Only for C2 and C3)
                employee_choice = True
                while employee_choice:
                    Menu.print_menu_employees()
                    ch_employees = input("What would you like to do?: ")
                    ch_employees = ch_employees.strip()
                    if not str.isdigit(ch_employees):
                        print("")
                        print("Error, wrong input. Try again")
                        print("")
                    match int(ch_employees):
                        case 1: #Add a new Employee
                            Employee_menu.create_employee()
                        case 2: #Print Employees
                            employees = Employee_menu.get_all_employees()
                            Employee_menu.print_all_employees(employees)
                        case 3: #Search Employees
                            employees = Employee_menu.get_all_employees()
                            Employee_menu.search_employee(employees)
                        case 4: #Update Employee
                            employees = Employee_menu.get_all_employees()
                            Employee_menu.update_employee(employees)
                        case 5: #Delete Employee Only C3
                            Employee_menu.delete_employee()
                        case 6: #Returns to main menu
                            print("returning to main menu")
                            employee_choice = False
                        case _:
                            print("")
                            print("Error, wrong input. Try again")
                            print("")  

            case 4: # Inventory menu (C2 and C3)
                inventory_choice = True
                while inventory_choice:
                    Menu.print_menu_inventory()
                    ch_inventory = input("What would you like to do?: ")
                    ch_inventory = ch_inventory.strip()
                    if not str.isdigit(ch_inventory):
                        print("")
                        print("Error, wrong input. Try again")
                        print("")
                
                    match int(ch_inventory):
                        case 1: # Add Product
                            Inventory_menu.create_product()
                        case 2: # Print Inventory (Item name, Item ID, stock, price)
                            products = Inventory_menu.get_all_products()
                            Inventory_menu.print_inventory(products)
                        case 3: # Update Product 
                            products = Inventory_menu.get_all_products()
                            Inventory_menu.update_product(products)
                        case 4: # Remove product (only C3)
                            Inventory_menu.delete_product()
                        case 5: # Return to main menu
                            print("returning to main menu")
                            inventory_choice = False
                        case _:
                            print("")
                            print("Error, wrong input. Try again")
                            print("")  
                    
            case 5: #CASE 5 statistics (Only C3). 
                statistics_choice = True
                while statistics_choice:
                    Menu.print_menu_statistics()
                    ch_statistics = input("What would you like to do?: ")
                    ch_statistics = ch_statistics.strip()
                    if not str.isdigit(ch_statistics):
                        print("")
                        print("Error, wrong input. Try again")
                        print("")
                
                    match int(ch_statistics):
                        # 
                        case 1: #Prints some statistics
                            Statistics.total_sales()
                            Statistics.member_count()
                            Statistics.guest_count()
                        case 2: # Return to main menu
                        case 1: #Prints some statistics
                            Statistics.total_sales()
                            Statistics.member_count()
                            Statistics.guest_count()
                        case 2: # Return to main menu
                            print("returning to main menu")
                            statistics_choice = False
                        case _:
                            print("")
                            print("Error, wrong input. Try again")
                            print("")  

            case 6: #Log out the user
            case 6: #Log out the user
                print("You have been logged out")
                logged_in = False 

            case _:
            case _:
                print("")
                print("Error, wrong input. Try again")
                print("")

while __name__ == "__main__":
    db = DB("store_api.db")
    d_url = "db_url"
    db.__init__(d_url)
    db = DB("store_api.db")
    d_url = "db_url"
    db.__init__(d_url)
    main()
    
    