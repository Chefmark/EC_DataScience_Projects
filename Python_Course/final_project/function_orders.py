import requests

from function_members import Member_menu
from model_product import Product
from model_order_details import Order_detail
from model_order import Order
from model_member import Member

class New_order():
    def display_menu(): #Displays the current cart as well as the menu for orders
        new_order_choice = True
        cart: list = [] 
        while new_order_choice:
            print("")
            print("Currently in cart:")
            total_cost= []
            total_tax = []
            for item in cart:
                print(f"{item['product_name']}: amount {item['amount']} at ${item['subtotal']}")
                subtotal = item['subtotal']
                total_cost.append(subtotal)
                subtax = item['subtax']
                total_tax.append(subtax)
            
            #Following variables round the sum of the totalcost and total tax lists for display purposes.
            sum_total_cost = round(sum(total_cost), 2)
            display_total_cost = str(round(sum(total_cost), 2))
            sum_total_tax = round(sum(total_tax), 2)
            display_total_tax = str(round(sum(total_tax), 2))
            print("")
            print(f"Total cost = ${display_total_cost}")
            print(f"Of which tax = ${display_total_tax}")
        
            print("""
            1. Add item(s) to cart
            2. Clear the cart
            3. Go to payment
            5. Back out
            """)
            order_choice = input("What would you like to do?: ").strip()
            if not str.isdigit(order_choice):
                print("Error, enter an integer")
            match int(order_choice):
                case 1: #ask to add to cart
                   current_inventory = New_order.display_inventory()
                   item_to_cart = New_order.add_to_cart(current_inventory)
                   cart.append(item_to_cart)
                case 2:  #ask to clear cart
                    choice_clear = New_order.clear_cart(cart)
                    print(choice_clear)
                case 3:#ask to pay
                    payment = New_order.check_out(cart, sum_total_cost, display_total_cost, sum_total_tax, display_total_tax)
                    print(payment)
                case 5: #Return
                    new_order_choice = False
                case _: 
                    ("Enter a valid menu choice")

    def display_inventory(): # Gets the current inventory with updated stock
        inventory = requests.get("http://127.0.0.1:8000/inventory/print_inventory/")
        if not inventory.status_code == 200:
            print("Error")
            return
        current_inventory = []
        data = inventory.json()
        for item in data:
            current_inventory.append(item)
        pass 
        print("Current inventory: ")
        for item in current_inventory:
            print(f"{item['id']}.) {item['name']} ${item['price']} Amount in stock {item['stock']}")
        return current_inventory

    def add_to_cart(current_inventory): #Adds an item from the cart and removes the amount added from the stock.
        gate_key1 = False
        while not gate_key1:
            item_add_cart = input("What item would you like to add to cart?(choose the number from the current inventory): ").strip()
            key = "id"
            value = int(item_add_cart)
            for item in current_inventory:
                if (item.get(key) == value) and (item['stock'] != "0"):
                    print("")
                    print(f"{item['name']} exists")
                    if item['stock'] == 0:
                        print("Unfortunately it is out of stock")
                        print("")
                        gate_key1 = False
                        break
                    else:
                        selected_item = item
                        gate_key1 = True
                        break    
            else:
                print("")
                print("The item deos not exist")
                print("")
                gate_key1 = False
            
            gate_key = False
        while not gate_key:
        #takes an amount to be added. checks that the amount is in stock. finally creates a dictionary matching the model order details which will be used later.
            amount_of_item = input(f"How many {selected_item['name']} would you like to add?: ").strip()
            if not str.isdigit(amount_of_item):
                print("Error, enter an integer")
                gate_key = False
            amount_of_item = int(amount_of_item)
            if (selected_item['stock'] - amount_of_item) < 0:
                print("")
                print("Unfortunately we do not have that much stocked")
                print("")
                gate_key = False
            else:
                gate_key = True
                print(f"Adding {amount_of_item} of {selected_item['name']} to your cart.")
                subtax: float
                subtotal: float
                new_stock = selected_item['stock'] - amount_of_item
                subtax = amount_of_item * selected_item['tax']
                subtotal = amount_of_item * selected_item['price']
                item_to_append: dict
                item_to_append = {
                    "product_id": selected_item['id'],
                    "product_name": selected_item['name'],
                    "product_price": selected_item['price'],
                    "product_tax": selected_item['tax'],
                    "amount": amount_of_item,
                    "subtax": subtax,
                    "subtotal": subtotal
                }
                # Remove from stock.
                rs_id = selected_item['id']
                rs_name = selected_item['name']
                rs_description = selected_item['description']
                rs_stock = new_stock
                rs_price = selected_item['price']
                rs_tax = selected_item['tax']
                new_product_stock = Product(id=rs_id, name=rs_name, description=rs_description, stock=rs_stock, price=rs_price, tax=rs_tax)
                res = requests.put((f"http://127.0.0.1:8000/inventory/update_product/{rs_id}"), json=new_product_stock.dict())
                print(res.json())
                return(item_to_append)
    

    def clear_cart(cart): #Clears the cart and adds the cart back to the inventory
        print("")
        loop_key = True
        while loop_key:
            confirm_clear = input("Are you sure you want to clear the cart? (y/n): ").lower().strip()
            if confirm_clear == "y":
                print("Clearing cart")
                loop_key = False
                current_inventory = []
                inventory = requests.get("http://127.0.0.1:8000/inventory/print_inventory/")
                data = inventory.json()
                for i in data:
                    current_inventory.append(i)
                for cart_item in cart:
                    for inventory_item in current_inventory:
                        if cart_item['product_id'] == inventory_item['id']:
                            update_inv_stock = inventory_item['stock'] + cart_item['amount']
                            update_inv_id= inventory_item['id']
                            update_inv_name= inventory_item['name']
                            update_inv_description = inventory_item['description']
                            update_inv_price = inventory_item['price']
                            update_inv_tax = inventory_item['tax']
                            update_inventory_item = Product(name=update_inv_name, description=update_inv_description,stock=update_inv_stock, price=update_inv_price, tax=update_inv_tax)
                            res = requests.put(f"http://127.0.0.1:8000/inventory/update_product/{update_inv_id}", json=update_inventory_item.dict())
                            print(res)
                return (cart.clear())
            elif confirm_clear == "n":
                print("Returning to previous menu")
                loop_key = False
                break
            else:
                print("Error, try again")
                loop_key = True
        pass

        #Adds a new order to the orders table in the store.api database
    def add_new_order(employee_code, member_id, sum_total_cost, sum_total_tax):
        print("Processing order")
        new_order = Order(employee_code=employee_code, member_id= member_id, total_price=sum_total_cost, tax_total=sum_total_tax )
        res = requests.post(f"http://127.0.0.1:8000/order/new_order", json=new_order.dict())
        print(res)

        #selects the most recent order so that its id can be used for creating a new order detail
    def select_most_recent_order():
        res = requests.get(f"http://127.0.0.1:8000/order/most_recent_order")
        data = res.json()
        return data

    #creates a new order detail
    def add_new_order_detail(cart, new_order_id):
        for item in cart:
            product_id = item['product_id']
            product_name = item['product_name']
            product_price = item['product_price']
            product_tax = item['product_tax']
            amount = item['amount']
            order_id = new_order_id
            subtax = item['subtax']
            subtotal = item['subtotal']
            new_order_detail = Order_detail(product_id=product_id, product_name=product_name, product_price=product_price,
            product_tax=product_tax, amount=amount, order_id=order_id, subtax=subtax, subtotal=subtotal)
            res = requests.post(f"http://127.0.0.1:8000/order/new_order_detail", json=new_order_detail.dict())
            print(res)

        #Function handels payment and the check out of the cart. 
        # It searches for 
    def check_out(cart, sum_total_cost, display_total_cost, sum_total_tax, display_total_tax):
        loop_key = True
        while loop_key:
            confirm_checkout = input("Are you sure you want to head to check out? (y/n): ").lower().strip()
            if confirm_checkout == "y":
                employee_code = input("What is your employee code?: ").upper()
                member_info: Member
                memberloop_key = True
                while memberloop_key:
                    member_ask = input("Is the customer a member?(y/n): ").lower().strip()
                    if member_ask == "y":
                        all_members = Member_menu.get_all_members()
                        found_member = Member_menu.search_member(all_members)
                        print(f"Adding: {found_member.first_name} {found_member.last_name}")
                        member_info = found_member
                        memberloop_key = False
                    elif member_ask == "n":
                        print("")
                        create_member_loop = True
                        while create_member_loop:
                            create_new_member_ask = input("Would you like to create a new member?(y/n): ")
                            if create_new_member_ask == "y":
                                new_member = Member_menu.create_member()
                                members = Member_menu.get_all_members()
                                updated_new_member = Member_menu.get_new_member(members, new_member)
                                member_info = updated_new_member
                                create_member_loop = False
                            elif create_new_member_ask == "n":
                                print("adding guest")
                                new_guest = Member(first_name="Guest", last_name="Guest", phone_number= " ", email= " ")
                                res = requests.post(f"http://127.0.0.1:8000/member/create_member", json=new_guest.dict())
                                print(res)
                                member_info = new_guest
                                create_member_loop = False
                            else:
                                print("Error, try again")
                                create_member_loop = True
                        memberloop_key = False
                        break
                    else:
                        print("Error, try again")
                        memberloop_key = True
                self_display_total_cost = display_total_cost
                self_display_total_tax = display_total_tax
                sum_total_cost
                sum_total_tax
                member_info
                member_id = member_info.id
                employee_code
                print(f"The customer needs to pay ${self_display_total_cost} of which the tax is ${self_display_total_tax}")
                payment_gate = True
                while payment_gate:
                    payment_made = input("Has the payment been made?(y/n): ")
                    if payment_made =="y":
                        payment_gate = False
                        New_order.add_new_order(employee_code, member_id, sum_total_cost, sum_total_tax)
                        most_recent_order = New_order.select_most_recent_order()
                        new_order_id = most_recent_order['id']
                        New_order.add_new_order_detail(cart, new_order_id)
                        return (cart.clear())
                    else:
                        print("The customer needs to pay in order to continue")
                loop_key = False
            elif confirm_checkout == "n":
                print("Returning to main menu")
                loop_key = False
                break
            else:
                print("Error, try again")
                loop_key = True
        pass




