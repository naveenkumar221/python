# Syntax Error Check

# if True
# print("Hello")
print("Syntax Error Check:")
if True:
    print("Hello - Syntax Error \n")


#ZeroDivisionError

print(" ZeroDivisionError:")
try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.\n")


#ValueError

print(" ValueError:")
try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)
except ValueError:
    print("Error: Please enter a valid number for age.\n")


#TypeError

print("TypeError:")
try:
    num = 10
    text = "five"
    result = num + text
except TypeError:
    print("Error: Cannot add integer and string together.\n")


#Finally Block

print(" Finally Block:")
try:
    n = int(input("Enter an integer: "))
    print("You entered:", n)
except Exception as e:
    print("An error occurred:", e)
finally:
    print("Program Completed\n")


#Multiple Exceptions

print(" Multiple Exceptions:")
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")
print()


#File Handling Error

print(" File Handling Error:")
try:
    file = open("student_data.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Error: The file 'student_data.txt' does not exist.\n")


#Catch All Exceptions

print("Catch All Exceptions:")
try:
    num = int(input("Enter a number: "))
    print("Square:", num ** 2)
except Exception as e:
    print("An unexpected error occurred:", e)
print()


#Custom Error Message

print("Custom Error Message:")
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print("Your age is:", age)
except ValueError as e:
    print("Error:", e)
print()


#Safe Calculator

print("Safe Calculator:")
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    if operation == '+':
        print("Result:", num1 + num2)
    elif operation == '-':
        print("Result:", num1 - num2)
    elif operation == '*':
        print("Result:", num1 * num2)
    elif operation == '/':
        print("Result:", num1 / num2)
    else:
        print("Invalid operation!")
except ValueError:
    print("Error: Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print("Unexpected error:", e)
finally:
    print("Program Completed Successfully!")
