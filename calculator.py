# Define four functions for basic arithmetic operations

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b
def calculator():
    print("Welcome to the simple calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    operations = {
        "1": add,
        "2": subtract,
        "3": multiply,
        "4": divide
    }

    while True:
        # Get user select
        choice = input("Enter your choice (1/2/3/4) or 'exit' to quit: ")
        if choice.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        if choice not in operations:
            print("Invalid choice. Please select a valid option.")
            continue

        # input two number
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        operation = operations[choice]
        result = operation(num1, num2)
        
        # Display the result
        print(f"The result is: {result}\n")
calculator()