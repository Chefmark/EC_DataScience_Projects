from typing import List
import requests

from model_member import Member

def url(route:str):
    return f"http://127.0.0.1:8000{route}"

class Member_menu:
    def create_member():
        print("")
        print("Create a new member")
        first_name_input = input("First name: ").capitalize()
        last_name_input = input("Last name: ").capitalize()
        phone_number_input = input("Enter phone number: ")
        email_input = input("Enter email: ")
        new_member = Member(first_name=first_name_input, last_name=last_name_input, phone_number=phone_number_input, email=email_input)
        res = requests.post(url("/member/create_member"), json=new_member.dict())
        print(res)
        return(new_member)

    def get_all_members():
        print("Getting all members")
        members = []
        res = requests.get(url("/member/all"))
        if not res.status_code == 200:
            return
        data = res.json()
        ("found all members")
        for member in data:
            member = Member(**member)
            members.append(member)
        return members
    
    def get_new_member(members: List[Member], new_member:Member):
        new_member = new_member
        found = False
        for member in members:
            if (member.last_name == new_member.last_name) and (member.first_name == new_member.first_name) and (member.phone_number == new_member.phone_number):
                new_member.id = member.id
                found = True
                return new_member

        if not found: 
            print("There was an error.")

    def search_member(members: List[Member]):
        search_member_input = input("Enter last name of member you wish to find: ")
        print("Searching for member...")
        print("Printing member(s)")
        found = False
        for member in members:
            if member.last_name == search_member_input.capitalize():
                print("--------------------------------------------------------------------------------------")
                print(f"Member Id: {member.id} First Name: {member.first_name} Last Name: {member.last_name}")
                print("--------------------------------------------------------------------------------------")
                found = True
        if not found:
            print("")
            print("Sorry a member with that last name does not exist")
            print("")
            return
        
        selected_member_id = int(input("What is the ID of the person you were looking for?: ").strip())
        for member in members:
            if member.id == selected_member_id:
                print("")
                print("-------------------------------------")
                print(f"Member Id: {member.id}")
                print(f"First Name: {member.first_name}")
                print(f"Last Name: {member.last_name}")
                print(f"Phone number: {member.phone_number}")
                print(f"Email: {member.email}")
                print("-------------------------------------")
                selected_member = member
                return selected_member
                
    def update_member(members: List[Member]):
        print("Update member")
        member_update_input = input("Enter Id of member you wish to update: ").strip()
        if not str.isdigit(member_update_input):
            print("IDs need to be integers")
            return
        index = None
        for i, member in enumerate(members):
            if member.id == int(member_update_input):
                print("Member found")
                index = i
                break
        if index == None:
            print("Sorry that member does not exist")
            return
        member = members[index]
        first_name_update = input("First name (leave blank if there is no update): ").capitalize()
        last_name_update = input("Last name (leave blank if there is no update): ").capitalize()
        phone_number_update = input("Phone number (leave blank if there is no update): ")
        email_update = input("Email (leave blank if there is no update): ")

        if not first_name_update:
            first_name_update = member.first_name
        if not last_name_update:
            last_name_update = member.last_name
        if not phone_number_update:
            phone_number_update = member.phone_number
        if not email_update:
            email_update = member.email
        new_member = Member(first_name=first_name_update, last_name=last_name_update,
         phone_number=phone_number_update, email=email_update)
        res = requests.put(url(f"/member/update_member/{member_update_input}"), json=new_member.dict())
        print(res.json())

    def delete_member():
        print("Delete employee")
        member_delete_input = input("Enter ID of member you wish to delete: ").strip()
        if not str.isdigit(member_delete_input):
            print("IDs need to be integers.")
            return
        res = requests.delete(url(f"/member/delete_member/{member_delete_input}"))
        print(res.json())