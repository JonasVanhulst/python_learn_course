from math import dist
from numpy import integer


print("Python Basics\nGoal: Understanding syntax, variables, data types, and basic programming logic.")

print("\n1. Variables and Data Types")

# Variables
integer_var: int = 10 # Integer type stores round numbers without decimal points.
float_var: float = 10.5 # Float type stores numbers with decimal points.
string_var: str = "Hello, Python!" # String type stores sequences of characters.
boolean_var: bool = True # Boolean type stores True or False values.

print(f"Integer: {integer_var}, Type_proof: {type(integer_var)}\nFloat: {float_var}, Type_proof: {type(float_var)}\nString: '{string_var}', Type_proof: {type(string_var)}\nBoolean: {boolean_var}, Type_proof: {type(boolean_var)}")

print("\n2. Basic Operations")

# Arithmetic Operations
# Addition -> +
# Subtraction -> -
# Multiplication -> *
# Division -> /
# Modulus (Remainder) -> %
# Exponentiation -> **

a: int = 2
b: int = 4
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")
print(f"Integer Division: {a} // {b} = {a // b}") # Floor division
print(f"Complex Number: 1 + 2j = {1 + 2j}") # Complex number

print("\n3. Input/Output Operations")
# Input from user
# user_input: str = input("Enter your name: ")

# Output to console
# print(f"You entered: {user_input}")
# print(f"Type of input: {type(user_input)}") # Input is always string type

print("\n4. Conditional Statements")
# If-Else Statement
num: int = 7
if num > 0:
    print(f"{num} is a positive number.")
elif num == 0:
    print(f"{num} is zero.")
else:
    print(f"{num} is a negative number.")
    
# Nested If
if num > 0:
    if num % 2 == 0:
        print(f"{num} is a positive even number.")
    else:
        print(f"{num} is a positive odd number.")

# Ternary Operator
result: str = "Even" if num % 2 == 0 else "Odd"
print(f"{num} is an {result} number.")

# Match-Case (Python 3.10+)
day: int = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number.")

print("\n5. Loops Structures")

# For Loop
print("For Loop Example:")
for i in range(5): # Iterates from 0 to 4
    print(f"Iteration {i}")

# foreach with list
fruits: list[str] = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# While Loop
print("While Loop Example:")
count: int = 0
while count < 5:
    print(f"Count is {count}")
    count += 1 # Increment count by 1
    if count == 3:
        print("Count reached 3, breaking the loop.")
        break # Exit the loop when count is 3\
    else:
        print("While loop ended normally.")
        
print("\n6. Functions")
# A simple function to demonstrate function definition and calling
def greet_without_name():
    """Function to greet without a name."""
    print("Hello, World!")

# Function Call
greet_without_name()

# Function Definition
def greet(name: str) -> str:
    """Function to greet a person with their name."""
    return f"Hello, {name}!"

greeting: str = greet("Alice")
print(greeting)

# Function with Default Argument
def power(base: int, exponent: int = 2) -> int:
    """Function to calculate power of a number with default exponent as 2."""
    return base ** exponent
print(f"2 to the power of 3 is {power(2, 3)}")

print("\n 7. lists, Tuples, Dictionaries, and Sets")
# List (Ordered, Mutable)
my_list: list[int] = [1, 2, 3, 4,]
print(f"List: {my_list}, Type_proof: {type(my_list)}")

#tuple (Ordered, Immutable)
my_tuple: tuple[str, int, bool] = ("Jonas", 21, True)
print(f"Tuple: {my_tuple}, Type_proof: {type(my_tuple)}")
(name, age, is_student) = my_tuple # Unpacking tuple
print(f"Name: {name}, Age: {age}, Is Student: {is_student}")

# Dictionary (Unordered, Mutable, Key-Value pairs)
my_dict: dict[str, int] = {"Alice": 25, "Bob": 30}
print(f"Dictionary: {my_dict}, Type_proof: {type(my_dict)}")

# Set (Unordered, Mutable, No duplicate elements)
my_set: set[int] = {1, 2, 3, 4, 4, 4} # Duplicate 4 will be ignored
print(f"Set: {my_set}, Type_proof: {type(my_set)}")
my_set.add(5) # Adding element to set
print(f"Set after adding 5: {my_set}")
my_set.remove(2) # Removing element from set
print(f"Set after removing 2: {my_set}")


# Time measurement of the differend list creation methods
import timeit
print("\nTime measurement of the different list creation methods:")

# Data sizes
N = 1_000_000


# Prepare data structures
data_list: list[int] = list(range(N))
data_tuple: tuple[int, ...] = tuple(range(N))
data_dict: dict[int, None] = {i: None for i in range(N)}
data_set: set[int] = set(range(N))


# Element to search
target = N - 1


# Define tests
tests: dict[str, any] = {
"List Membership": lambda: (target in data_list),
"Tuple Membership": lambda: (target in data_tuple),
"Dict Membership": lambda: (target in data_dict),
"Set Membership": lambda: (target in data_set),


"List Iteration": lambda: [x for x in data_list],
"Tuple Iteration": lambda: [x for x in data_tuple],
"Dict Iteration": lambda: [x for x in data_dict],
"Set Iteration": lambda: [x for x in data_set],


"List Index Access": lambda: data_list[N // 2],
"Tuple Index Access": lambda: data_tuple[N // 2],
"Dict Key Access": lambda: data_dict[N // 2],
}


# Run benchmarks
results:dict = {}
for name, func in tests.items():
    t: float = timeit.timeit(func, number=10)
    results[name] = t


# Print results sorted by time
print("Benchmark Results (smaller is faster):")
for name, t in sorted(results.items(), key=lambda x: x[1]):
    print(f"{name:20s}: {t:.6f} seconds")


print("\nEnd of Python Basics demonstration.")


