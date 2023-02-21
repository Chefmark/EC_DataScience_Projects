from typing import List
import requests

from model_product import Product

def url(route:str):
    return f"http://127.0.0.1:8000{route}"

class Inventory_menu:
    def create_product():
        print("")
        print("Add a new product to inventory")
        name_input = input("Name of new product: ").capitalize()
        description_input = input("Add a description (optional): ")
        stock_input = input("Enter how much of the product you have in stock: ").strip()
        print("Price includes the tax")
        price_input = input("Enter the price use . to add decimal: ").strip()
        tax_input = input("Enter the tax use . to add decimal: ").strip()
        new_product = Product(name=name_input, description=description_input, stock=stock_input, price=price_input, tax=tax_input)
        res = requests.post(url("/inventory/add_product"), json=new_product.dict())
        print(res)

    def get_all_products():
        products = []
        res = requests.get(url("/inventory/print_inventory/"))
        if not res.status_code == 200:
            print("Error")
            return
        data = res.json()
        for product in data:
            product = Product(**product)
            products.append(product)
        return products

    def print_inventory(products: List[Product]):
        for product in products:
            print("_____________")
            print(f"Name of product: {product.name}")
            print(f"ID of product: {product.id}")
            print(f"Amount in stock: {product.stock}")
            print(f"Price of item including tax: {product.price}")
            print("")

    def update_product(products: List[Product]):
        print("Update Product")
        product_update = input("Enter the product ID that you wish to update: ")
        if not str.isdigit(product_update):
            print("IDs need to be integers")
            return
        index = None
        for i, product in enumerate(products):
            if product.id == int(product_update):
                print("Product found")
                index = i
                break
        if index == None:
            print("Sorry can not find the product, try again")
            return
        product = products[index]

        name_update = input("Name (leave blank if there is no update): ")
        description_update = input("Description (leave blank if there is no update): ")
        stock_update = input("Stock (leave blank if there is no update): ").strip()
        price_update = input("Price (leave blank if there is no update): ").strip()
        tax_update = input("Tax (leave blank if there is no update): ").strip()

        if not name_update:
            name_update = product.name
        if not description_update:
            description_update = product.description
        if not stock_update:
            stock_update = product.stock
        if not price_update:
            price_update = product.price
        if not tax_update:
            tax_update = product.tax
        new_product = Product(name=name_update, description=description_update, stock=stock_update, price=price_update, tax=tax_update)
        res = requests.put(url(f"/inventory/update_product/{product_update}"), json=new_product.dict())
        print(res.json())

    def delete_product():
        print("Delete product")
        product_delete =input("Enter product ID that you wish to delete: ").strip()
        if not str.isdigit(product_delete):
            print("IDs need to be integers.")
            return
        res = requests.delete(url(f"/inventory/delete_product/{product_delete}"))
        print(res.json())