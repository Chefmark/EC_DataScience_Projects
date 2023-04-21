import requests

def url(route:str):
    return f"http://127.0.0.1:8000{route}"

# functions for Statistics
class Statistics:
    def total_sales():
        total_sales = requests.get(url("/statistics/total_sales"))
        print("")
        print(total_sales.json())

    def member_count():
        member_count = requests.get(url("/statistics/member_count"))
        print("")
        print(member_count.json())

    def guest_count():
        guest_count = requests.get(url("/statistics/guest_count"))
        print(guest_count.json())



