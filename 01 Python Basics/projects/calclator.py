"""
Author: Jonas Vanhulst
Project: Python Learning Roadmap
Description: A structured roadmap with projects to take learners from beginner 
             to professional in Python development.
Date: 2025
"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def power(x, y):
    return x ** y

def modulus(x, y):
    return x % y


def main():
    print("Python Calculator\n")
    
    user_input = input("Enter operation (add, subtract, multiply, divide, power, modulus) or 'exit' to quit: ").strip().lower()
    
    while (user_input != 'exit'):
        if user_input in ('add', 'subtract', 'multiply', 'divide', 'power', 'modulus'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if user_input == 'add':
                    print(f"Result: {add(num1, num2)}")
                elif user_input == 'subtract':
                    print(f"Result: {subtract(num1, num2)}")
                elif user_input == 'multiply':
                    print(f"Result: {multiply(num1, num2)}")
                elif user_input == 'divide':
                    print(f"Result: {divide(num1, num2)}")
                elif user_input == 'power':
                    print(f"Result: {power(num1, num2)}")
                elif user_input == 'modulus':
                    print(f"Result: {modulus(num1, num2)}")
            except ValueError as ve:
                print(f"Error: {ve}")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Invalid operation. Please try again.")
        
        user_input = input("\nEnter operation (add, subtract, multiply, divide, power, modulus) or 'exit' to quit: ").strip().lower()
        
    print("Thanks for using the calculator, Goodbye!")
        

if __name__ == "__main__":
    main()