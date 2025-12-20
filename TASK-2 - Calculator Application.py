# CodSoft Python Internship Task
# Task Name: Calculator
# Author: Kaavya B M


def get_numbers():
    """Function to get two numbers from the user"""
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Please enter valid numbers.")
        return None, None

def calculate(num1, num2, operator):
    """Function to perform calculation"""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Invalid operation selected."

def show_menu():
    print("\n--- SIMPLE CALCULATOR ---")
    print("Choose operation:")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")

# Main Program
show_menu()

operator = input("Enter operation (+, -, *, /): ")
num1, num2 = get_numbers()

if num1 is not None and num2 is not None:
    result = calculate(num1, num2, operator)
    print("\nResult:", result)
else:
    print("Calculation failed due to invalid input.")
