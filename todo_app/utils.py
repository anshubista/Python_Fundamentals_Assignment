import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def read_input(prompt):
    return input(prompt)
1