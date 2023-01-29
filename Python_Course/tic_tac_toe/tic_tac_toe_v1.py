# Exercise 3
from typing import list, Tuple
# Steg att göra
# 1. skriv ut spelplanen med print_board() lista med listor
# 2. ta input från användaren (2 spelare, update board och print board mellan varje drag)
# 3. input måste valideras (ie kolla om board är # eller innehåller O eller X)
# check if there is a winner (row, kolumn, diagonal)

global board 
board = [["#", "#", "#"], 
        ["#", "#", "#"],
        ["#", "#", "#"]]

# markers O, X

def main():
    marker = "X"
    winner = False
    while not winner:
        marker = "O" if marker == "X" else "X"
        print_board()
        row, col = get_input()
        update_board(row, col, marker)
        winner = check_winner()
    print_board()
    print(f"Winner is {marker}")

def print_board():
    print("")
    for row in board:
        print(row)
    print("")

def get_input() -> Tuple[int, int]:
    valid = False
    while not valid:
        coordinates_str = input(
            "Enter row and column for placement of piece. Separate with comma: ")
        valid, res= validate_input(coordinates_str)
    
    return res

def validate_input(string:str) -> Tuple[bool,Tuple[int, int]]:
    string = string.strip()
    split_string: List[str] = string.split(",")
    if len(split_string) < 2:
        print("Error in input, retry")
        return(False, None)
    if not str.isdigit(split_string[0]) or not str.isdigit(split_string[1]):
        print("Error in input, retry")
        return(False, None)
    
    row: int = int(split_string[0])
    col: int = int(split_string[1])
    if not 1 <= row <= 3 or not 1 <= col <= 3:
        print("Error in input, retry")
        return(False, None)

    if board[row - 1][col - 1] != "#":
        print("Error in input, retry")
        return(False, None)

    return (True, (row - 1, col - 1))


def update_board(row: int, col: int, marker: str):
    board[row][col] = marker


def check_winner() ->bool:
    #check rows
    for row in board:
        row_set = set(row)
        if len(row_set) == 1 and row_set.pop() != "#":
            return True
    #check columns
    for i in range(2):
        col_set = {board[0][i], board[1][i], board[2][i]}
        if len(col_set) == 1 and col_set.pop() != "#":
            return True

    #check diagonal 
    across_set1 = {board[0][0], board[1][1], board[2][2]}
    if len(across_set1) == 1 and across_set1.pop() != "#":
            return True
    across_set2 = {board[0][2], board[1][1], board[2][0]}
    if len(across_set2) == 1 and across_set2.pop() != "#":
        return True
    return False



main()