# convert a floating-point number to integer:

a=4.89
print(type(a))
print(type(int(a)))

# coverting a string to int and multiply it by 5:
a="7"
print(type(a))
b=(int(a))
print(b*5)

# covert an integer input to float:
a=8
print(float(a))

#converting string to float and add 1:
a="3.1415"
print(type(a))
b=(float(a))
print(b+1)

#create a complex number from real and imaginary inputs
a=10
b=16
print(complex(a,b))

#return squres of a complex number:
a=5
b=6
c=(complex(a,b))
c1=c**2
print(c1)

# round to 2 decimal places:
a=6.72849
print(round(a,2))

#round user-input float to nearest integer:
num=float(input("enter the number "))
rounded=round(num)
print(rounded)

#find min and max [2,5,1,9,-3,6]
a=[2,5,1,9,-3,6]
print(min(a),max(a))
#max of largest 3 numbers
a=[4,5,3]
print(max(a))
# alphabetically first name 
a=["Zara","Bob","Alice"]
b=sorted(a)
print(b)

# find using pow..
a=2
b=5
print(pow(a,b))

# user return result
a=int(input("Enter the number:" ))
b=int(input("enter the number:"))
print(pow(a,b))

x=2
y=3
z=5
a=pow(x,y)
b=a%z
print(b)

# using divmod()
a=23
b=5
print(divmod(a,b))

#function to return quotient and remainder
def divmod(a,b):
    quotient=a/b
    reminder=a%b
    return quotient,reminder
print(divmod(5,10))

# absolute value of a user-input
n=int(input("enter the number:"))
print(abs(n))

# between 2 numbers
n=int(input("enter the number:"))
m=int(input("enter the number:"))
print(abs(n+m))

#distance 
n=int(input("enter the number:"))
m=int(input("enter the number:"))
distance=abs(n)+abs(m)
print(distance)

# multiply 2 strings
a=input()
b=input()
print(int(a)+int(b))

#round pow
print(round(pow(5,3)/7,3))

#print largest absolute val
list=[-2,-8,3,7]
print(abs(max(list)))

#roound user float input
print(pow(round(45.76),2))

