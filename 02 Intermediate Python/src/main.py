"""
Author: Jonas Vanhulst
Project: Python Learning Roadmap
Description: A structured roadmap with projects to take learners from beginner 
             to professional in Python development.
Date: 2025
"""

import math
from datetime import datetime

print("Intermediate Python\nGoal: Mastering functions, modules, file handling, and error handling.")

print("\n1. Mastering functions")

# Arbitrary Arguments *args (if the number of arguments is unknown add a * before the parameter name so that the function will receive a tuple of arguments)
def my_arbitrary_function(*args) -> None:
    print("Arbitrary arguments:", args)

# Arbitrary Keyword Arguments **kwargs (if the number of keyword arguments is unknown add a ** before the parameter name so that the function will receive a dictionary of arguments)
def my_arbitrary_keyword_function(**kwargs) -> None:
    print("Arbitrary keyword arguments:", kwargs)
    
# Default Parameter Value (if we call the function without an argument, it uses the default value)
def my_default_parameter_function(country: str = "Norway") -> None:
    print("I am from", country)

# Passing statement, if you have a function with no content, put in the pass statement to avoid getting an error
def my_empty_function() -> None:
    pass

# Keyword-only Arguments (after the * in the function definition, all parameters are keyword-only parameters)
def my_keyword_only_function(*, name: str, age: int) -> None:
    print(f"Name: {name}, Age: {age}")

print("\n2. Overview of Python Modules")

# What is a module?
print("A module is a file containing Python definitions and statements. Modules help organize code into reusable components.")

# Importing a module
print("Example: import math")
print("math.sqrt(16) =", math.sqrt(16))

# Importing specific functions from a module
print("Example: from datetime import datetime")
print("Current datetime:", datetime.now())

# Creating your own module
print("You can create your own module by saving functions and variables in a .py file and importing it.")

# Listing some useful standard modules
print("Useful standard modules include: sys, os, math, random, datetime, json, re, collections, itertools, functools, pathlib, csv, and more.")

# Using the dir() function to see module contents
print("Contents of the math module:", dir(math)[:10], "...")  # Show only first 10 for brevity

print("\n3. File Handling and Error Handling")

# File Handling
print("File Handling: Opening, reading, writing, and closing files.")

def open_file(file_path: str) -> None:
    try:
        file = open(file_path, 'r')
        print("File opened successfully.")
        file.close()
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: An I/O error occurred.")

def close_file(file) -> None:
    try:
        file.close()
        print("File closed successfully.")
    except IOError:
        print("Error: An I/O error occurred while closing the file.")

def read_file(file_path: str) -> None:
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File content:", content)
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: An I/O error occurred.")
        
def write_file(file_path: str, content: str) -> None:
    try:
        with open(file_path, 'w') as file:
            file.write(content)
            print("File written successfully.")
    except IOError:
        print("Error: An I/O error occurred.")
        
# Error Handling
print("Error Handling: Using try, except, finally to manage exceptions.")
def divide_numbers(a: float, b: float) -> float:
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except TypeError:
        print("Error: Invalid input type.")
        return None
    else:
        print("Division successful.")
        return result
    finally:
        print("Execution of divide_numbers complete.")
        
