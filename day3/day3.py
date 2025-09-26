# Function it is a named block of code peform a specific task...

# User-Defined Function

def greet():
    print("Hello, welcome to Day 3!")
greet()

# Function with Parameters

def add(a, b):
    return a + b
print(add(3, 5))        # Output: 8

# Default Parameters

def greet(name="Guest"):
    print(f"Hello, {name}!")
greet()                 # Output: Hello, Guest!
greet("Naveen")         # Output: Hello, Naveen!

# Return Statement

def square(x):
    return x * x
result = square(4)
print(result)           # Output: 16

# Function with Multiple Returns

def calculate(a, b):
    return a + b, a * b
add, mul = calculate(2, 3)
print("Sum:", add)
print("Product:", mul)

# Lambda (Anonymous) Function

square = lambda x: x * x
print(square(5))       # Output: 25

# Built-in Higher-Order Functions

#map()

nums = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, nums))
print(squares)               # Output: [1, 4, 9, 16]

#filter()

nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)                 # Output: [2, 4]

