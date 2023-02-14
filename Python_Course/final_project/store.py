from typing import List
import requests


#Local function imports
from function_print_menu import *
from function_employees import employee_menu

#Local imports
from model_employee import Employee
from model_member import Member

# Log_in  tar str argument och matchar det med employee ID
# Om input är exit ska programmet stängas av.
def log_in():
    log_input = input("Please enter your employee ID or type exit to close program: ")
    if log_input == "exit":
        print("Closing program")
        exit()

    if log_input !="exit":
        pass


def main():
    log_in()
    
    logged_in = True
    # While loop som körs medan användaren är inloggad. 
    while logged_in:
        print_menu_main()
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
                    print_menu_orders()
                    ch_order = input("What would you like to do?: ")
                    ch_order = ch_order.strip()
                    if not str.isdigit(ch_order):
                        print("")
                        print("Error, wrong input. Try again")
                        print("")
                        return
                
                    match int(ch_order):
                        # Lägger en ny order. Behöver kunna söka medlemmar på personnr. 
                        # Om inget finns ska man kunna spara en ny medlem eller 
                        # bara lägga till guest/non-member.
                        case 1:
                            
                            pass
                        case 2: # tar användaren tillbaka till huvudmenyn
                            print("returning to main menu")
                            order_choice = False
                        case _:
                            print("")
                            print("Error, wrong input. Try again")
                            print("")


            case 2: #Members menu (for everyone)
                member_choice = True
                while member_choice:
                    print_menu_members()
                    ch_members = input("What would you like to do?: ")
                    ch_members = ch_members.strip()
                    if not str.isdigit(ch_members):
                        print("")
                        print("Error, wrong input. Try again")
                        print("")
                        return
                
                    match int(ch_members):
                        case 1: #Add new member
                            pass
                        case 2: #Search members
                            pass
                        case 3: #Update members
                            pass
                        case 4: #Delete member
                            pass
                        case 5: # tar användaren tillbaka till huvudmenyn
                            print("returning to main menu")
                            member_choice = False
                        case _:
                            print("")
                            print("Error, wrong input. Try again")
                            print("")                    

            case 3: # Employee menu (Only for C2 and C3)
                employee_choice = True
                while employee_choice:
                    print_menu_employees()
                    ch_employees = input("What would you like to do?: ")
                    ch_employees = ch_employees.strip()
                    if not str.isdigit(ch_employees):
                        print("")
                        print("Error, wrong input. Try again")
                        print("")
                        return
                
                    match int(ch_employees):
                        case 1: #Add a new Employee
                            employee_menu.create_employee()
                        case 2: #Print Employees
                            employees = employee_menu.get_all_employees()
                            employee_menu.print_all_employees(employees)
                        case 3: #Search Employees
                            employees = employee_menu.get_all_employees()
                            employee_menu.search_employee(employees)
                        case 4: #Update Employee
                            employees = employee_menu.get_all_employees()
                            employee_menu.update_employee(employees)
                        case 5: #Delete Employee Only C3
                            employee_menu.delete_employee()
                            pass
                        case 6: # tar användaren tillbaka till huvudmenyn
                            print("returning to main menu")
                            employee_choice = False
                        case _:
                            print("")
                            print("Error, wrong input. Try again")
                            print("")  

            case 4:
                inventory_choice = True
                while inventory_choice:
                    print_menu_inventory()
                    ch_inventory = input("What would you like to do?: ")
                    ch_inventory = ch_inventory.strip()
                    if not str.isdigit(ch_inventory):
                        print("")
                        print("Error, wrong input. Try again")
                        print("")
                        return
                
                    match int(ch_inventory):
                        # 
                        case 1: # Add Product
                            pass
                        case 2: # Print Inventory (Item name, Item ID, amount, price)
                            pass
                        case 3: # Update Product 
                            pass
                        case 4: # Remove product (enbart C3)
                            pass
                        case 5: # tar användaren tillbaka till huvudmenyn
                            print("returning to main menu")
                            inventory_choice = False
                        case _:
                            print("")
                            print("Error, wrong input. Try again")
                            print("")  
                    
            case 5: #CASE 5 kommer hantera statistik av data. 
                statistics_choice = True
                while statistics_choice:
                    print_menu_statistics()
                    ch_statistics = input("What would you like to do?: ")
                    ch_statistics = ch_statistics.strip()
                    if not str.isdigit(ch_statistics):
                        print("")
                        print("Error, wrong input. Try again")
                        print("")
                        return
                
                    match int(ch_statistics):
                        # 
                        case 1: #SKRIVER UT STATISTIK
                            pass
                        case 2: # tar användaren tillbaka till huvudmenyn
                            print("returning to main menu")
                            statistics_choice = False
                        case _:
                            print("")
                            print("Error, wrong input. Try again")
                            print("")  

            case 6: #loggar ut användaren.
                print("You have been logged out")
                logged_in = False 

            case _: #Hanterar fel input.
                print("")
                print("Error, wrong input. Try again")
                print("")
    pass

while __name__ == "__main__":
    main()