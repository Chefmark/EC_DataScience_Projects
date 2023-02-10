#Course plan
# 1) create a Course class with following attributes (Name, code, credits)
# create a function to print.
# 2) create a main method that creates an instance of the class

# 3) create a class called teacher with a method to print
# 4) add teacher to course
# 5) create a class for students
# 6) create a list in the course with the students
# 7) add lessons to the course
# 8) add a method to remove or add lessons or students from the course
# 9) add a menu in the main() with the following options:
#       - add a teacher to the course
#       - add a student to the course
#       - add a lesson to the course
#       - print out the course
#       - exit

from typing import List, Tuple

class Teacher():
    t_first_name:str
    t_last_name:str
    t_age:int
    t_specialization:str
    
    def __init__(self, t_first_name:str, t_last_name:str, t_age:int, t_specialization:str):
        self.t_first_name: t_first_name
        self.t_last_name: t_last_name
        self.t_age: t_age
        self.t_specialization = t_specialization
    
    def __str__(self) -> str:
        first_name_string = f"First Name: {self.t_first_name}"
        last_name_string = f"Last Name: {self.t_last_name}"
        age_string = f"Age: {self.t_age}"
        specialization_string = f"Specialization: {self.t_specialization}"
        return f"{first_name_string}, {last_name_string}, {age_string}, {specialization_string}"


class Course():
    course_name:str
    course_code:str
    course_credits:int
    course_teacher: Teacher

    
    def __init__(self, course_name:str, course_code:str, course_credits:int, course_teacher: Teacher):
        self.course_name = course_name
        self.course_code = course_code
        self.course_credits = course_credits
        self.course_teacher = course_teacher

    def __str__(self) -> str:
        return f'{self.course_name}, {self.course_code}, {self.course_credits}, {self.course_teacher}'


python_course = Course("Python programming", "PY-2023", 40, Teacher("Anton", "Appelblom", 30, "Python"))
print(python_course)


# def main():

    # python_course = Course("Python programming", "PY-2023", 40, Teacher("Anton", "Appelblom", 30, "Python"))
    
    # print(python_course)


# main()

class Company:
    name: str
    number_of_employees: int
    address: str
    CEO: str

    def __init__(self, name: str, number_of_employees: int, address: str, ceo: str):
        self.name = name
        self.address = address
        self.number_of_employees = number_of_employees
        self.CEO = ceo

    def __str__(self) -> str:
        name_string = f"Name: {self.name}"
        address_string = f"Address: {self.address}"
        employees_string = f"Employees: {self.number_of_employees}"
        ceo_string = f"CEO: {self.CEO}"
        return f"{name_string}, {address_string}, {employees_string}, {ceo_string}"


class Person:
    first_name: str
    last_nam: str
    age: int
    height: int
    full_name: str
    company: Company

    def __init__(self, first_name: str, last_name: str, age: int, height: int, company: Company):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.company = company
        self.full_name = f"{first_name} {last_name}"

    def __str__(self) -> str:
        return f'Hej jag heter {self.first_name} {self.last_name} och är {self.age} år gammal och {self.height} cm lång och jobbar på {self.company}'

    def __int__(self) -> int:
        return self.first_name.count("n")


anton = Person("Anton", "Appelblom", 30, 180, Company(
    "Mujina", 4, "Någonstans in stockholm", "Anton Appelblo"))


print(anton)