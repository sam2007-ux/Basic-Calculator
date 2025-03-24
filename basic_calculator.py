
import math

# Functions for calculator operations
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y
def exponent(x, y): return x ** y
def sqrt(x): return math.sqrt(x)
def log(x, _): return math.log(x) if x > 0 else "Cannot take log of non-positive number"

# Dictionary to map choices to functions
operations = {
    "1": add, "add": add,
    "2": subtract, "subtract": subtract,
    "3": multiply, "multiply": multiply,
    "4": divide, "divide": divide,
    "5": exponent, "exponent": exponent,
    "6": sqrt, "square root": sqrt, "sqrt": sqrt,
    "7": log, "logarithm": log, "log": log
}

# List of operation symbols (operation_characters)
operation_characters = ["+", "-", "*", "/", "**", "√", "log"]

# Contains the activity history of the user
history = []

def show_history():
    print("\nCalculation History:")
    if not history:
        print("No history yet.")
        return
    for index, hist in enumerate(history, start=1):
        print(f"{index}. {hist}")

# Main function for the calculator
def calculator():
    while True:
        print("Calculator\n")
        print("\nSelect Operation: \n")
        options = ["Add", "Subtract", "Multiply", "Divide", "Exponent", "Square root", "Logarithm", "View History"]

        # Loop through options list and print it out
        for index, i in enumerate(options, start=1):
            print(f"{index}. {i}")

        choice = input("\nEnter choice (1-7 or add/subtract/...): ").strip().lower()

        if choice in operations:
            try:
                if choice == "6" or choice == "sqrt" or choice == "7" or choice == "log":
                    x = float(input("Enter a number: "))
                    result = operations[choice](x,0)  # Only one input needed for sqrt and log
                    op_symbol = operation_characters[5] if choice in ["6", "sqrt"] else operation_characters[6]
                    history.append(f"{x} {op_symbol} = {result}")
                else:
                    x, y = float(input("Enter first number: ")), float(input("Enter second number: "))
                    result = operations[choice](x, y)
                    op_symbol = operation_characters[int(choice) - 1]  # Map the operation symbol to correct index
                    history.append(f"{x} {op_symbol} {y} = {result}")

                print(f"Result: {result}")

            except ValueError:
                print("Invalid input! Please enter numbers only.\n")
                print("--------------------------")
                continue

        elif choice == "8" or choice == "view history":
            show_history()

        else:
            print("Invalid choice. Please select a valid operation.\n")
            print("--------------------------")
            continue

        if input("Do another calculation? (Y/N): ").strip().lower() in ["n", "no"]:
            print("Goodbye!")
            break
        else:
            print()
            print("--------------------------")
            continue

# Run the calculator
calculator()