# write a program to find the simple interest with using formula
P = float(input("principal amount :"))
R = float(input("rate of intrest :"))
T = float(input("time in years  :"))
SI = (P * R * T) / 100
print("Simple Interest is:", SI)

# Temperature Conversion (Celsius to Fahrenheit)
Celsius = float(input("temperature in celsius :"))
Fahrenheit = (Celsius * 9/5) + 32
print("Temperature in Fahrenheit:", Fahrenheit)

#Finding Average of Three Numbers
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
num3 = float(input("Enter 3rd number: "))
average = (num1 + num2 + num3) / 3
print("Average of the 3 numbers is:", average)

# Area of Circle
import math as m
r = float(input("Enter the radius of the circle: "))
A = m.pi * r ** 2
print("Area of the circle is:", A)
