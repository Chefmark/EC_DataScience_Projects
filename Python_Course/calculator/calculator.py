#EXERCISE 2

from typing import Tuple

global OPERATIONS
OPERATIONS = ['+', '-', '*', '/']

def main():
    print("Calculator")
    will_continue = True
    res = 0
    reuse = False
    
    while True:
        if not reuse:
            res = None

        num1, num2 = get_input(prev_value=res) 
        operation = get_operation()

        if operation == "+":
            res = add(num1, num2)
        elif operation == "-":
            res = subtract(num1, num2)
        elif operation == "*": 
            res = multiply(num1, num2)
        elif operation == "/":
            res = divide(num1, num2)
        print(res)
        
        will_continue = get_continue()
        if not will_continue:
            break
        reuse = get_re_use_res()

    
def get_input(prev_value: int | float | None) -> Tuple[int | float, int]:
    valid = False
    if prev_value:
        valid = True
        validated1 = prev_value
    while not valid:
        choice1 = input("Vilket är ditt första nummer?: ")
        valid = check_input(choice1.strip())
        if valid:
            validated1 = int(choice1.strip())
    valid = False
    while not valid:
        choice2 = input("Vilket är ditt andra nummer?: ")
        valid = check_input(choice2.strip())
        if valid:
            validated2 = int(choice2.strip())
    
    return(validated1, validated2)
    
def check_input(choice_string: str) -> bool:
    valid = str.isdigit(choice_string) 
    if not valid:
        print("Error, value is not valid")
    return valid

def get_operation() -> str:
    global OPERATIONS
    valid = False
    while not valid:
        operation = input(
            "What operation do you wish to perform?: ('+', '-', '*', or '/') ")
        operation = operation.strip()
        if operation in OPERATIONS:
            valid = True
    return operation    

def add(a: int, b:int):
    result = a + b
    return(result)

def subtract(a: int, b:int):
    result = a - b
    return(result)

def multiply(a: int, b:int):
    result = a * b
    return(result)

def divide(a: int, b:int):
    if b == 0:
        print("Can not divide by 0")
        a, b = get_input(prev_value=a)
    result = a/b
    return(result)

def get_continue() -> bool:
    while True:
        choice = input("Do you wish to continue?: ('y' or 'n') ")
        if choice == "y":
            return True
        if choice == "n":
            return False


def get_re_use_res() ->bool:
    while True:
        choice = input("Do you want to reuse the result?: ('y' or 'n') ")
        if choice == "y":
            return True
        if choice == "n":
            return False

main()