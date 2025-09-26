# # writing print hello world 
# print("Hello world")

# # Write a Python program to do arithmetical operations addition and division.
# # Addition
# num1=int(input("enter the first number for addition: "))
# num2=int(input("enter the second number for addition: "))
# add=num1+num2
# print(f"sum: {num1}+{num2}={add}")

# #division
# num3=int(input("enter the dividend for divisor: "))
# num4=int(input("enter the divisor for divisor: "))
# if num4==0:
#     print("Error: Dicisor by zero is not allowed ")
# else:
#     div=num3/num4
#     print(f" div:={num3}/{num4}={div}")

# # Write a Python program to find the area of a triangle
# l=int(input("enter the length: "))
# h=int(input("enter the height:"))
# aera=0.5*l*h
# print(f"the aera of triangle is {aera}")

# #  Write a Python program to swap two variables.
# a=int(input("enter the first value: "))
# b=int(input("enter the second variable: "))
# temp=a
# a=b
# b=temp
# print((f"Swapped values: a={a},b={b}"))


# # Write a Python program to generate a random number
# import random
# print(random.randint(1,10))


# #  Write a Python program to convert kilometers to miles

# kilometers=int(input("enter the kilometers: "))
# covrtmile=0.62137119
# miles=kilometers*covrtmile
# print(f"the kilo meters are in the {miles} miles")

# #  Write a Python program to convert Celsius to Fahrenheit

# celsius=int(input("enter the temperature: "))
# fahrenheit=(celsius*9/5)+32
# print(f"{celsius} degrees celsius is equal to {fahrenheit} degrees faherenheit")


# Write a Python program to display calendar

import calendar
year=int(input("enter year: "))
month=int(input("enter the month: "))
cal=calendar.month(year,month)
print(cal)