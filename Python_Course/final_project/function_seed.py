import requests
import json

class Seed_data:
    def seed_admin():
        url = "http://127.0.0.1:8000/seed/admin"
        with open("seed_admin.json", "r") as seed:
            data = json.load(seed)
            r = requests.post(url, json=data)
            print("Admin seeded")
            return r

    def seed_demo():
        def url(route:str):
            return f"http://127.0.0.1:8000{route}"    
        with open("seed_data.json", "r") as seed:
            data = json.load(seed)
            for employee in data["employees"]:
                requests.post(url("/seed/admin"), json=employee)
            print("Employees seeded")
        
            for member in data["members"]:
                requests.post(url("/member/create_member"), json=member)
            print("Members seeded")
        
            for product in data["products"]:
                requests.post(url("/inventory/add_product"), json=product)
            print("Products seeded")

            for order in data["orders"]:
                requests.post(url("/order/new_order"), json=order)
            print("Orders seeded")

            for order_details in data["order_details"]:
                requests.post(url("/order/new_order_detail"), json=order_details)
            print("Order details seeded")
            

