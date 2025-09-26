# if, elif, else
marks = 85

if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
else:
    print("Grade: C or below")

# Nested Conditionals
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Access Granted ")
    else:
        print("ID Required ")
else:
    print("Access Denied ")

# Problem 1: Check if a number is positive, negative, or zero
num = -5

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Problem 2: Find the largest of 3 numbers using nested conditionals
a = 15
b = 25
c = 20

if a > b:
    if a > c:
        print("a is the largest")
    else:
        print("c is the largest")
else:
    if b > c:
        print("b is the largest")
    else:
        print("c is the largest")




#jenny problem 

h=int(input("enter your height: "))
bill=0
if h>=3:
    print("can ride:")
    age=int(input("what is your age ? "))
    if age<12:
        bill=150
        print("Ticket price  150 Rs.")
    elif age<=18:
        bill=250
        print("Ticket price  250 Rs.")
    else:
        bill=500
        print("Ticket price  500 Rs. ")
        
    w=input("Do you want to take photots ? ")
    if w=="y" or w=="Y":
        bill=bill+50
    
    print(f"your total bill is {bill} Rs. ")
        
else:
    print("cant ride:")
print("bye")





# pizza problem  


size=input("what size pizza do you want (S/M/L) ")
bill=0
if size=='s' or size=='S':
    bill+=100
    print("small piza is 100rs")

elif size=='m' or size=='M':
    bill+=200
    print("medium piza is 200rs ")

elif size=='l' or size=='L':
    bill+=300
    print("large piza is 300rs ")
else:
    print("select the given options only")


pepperoni=input("Do you want pepperoni ? (Y/N)")
if pepperoni=='y' or pepperoni=='Y':
    if size=='s' or size=='S':
        bill+=30
    else:
        bill+=50
else:
    print("ok sir, thank you ")
        
cheese= input("Do you want extra cheese ? (Y/N)")
if cheese=='y' or cheese=='Y':
    bill+=20
else:
    print("ok sir, thank you")
    
print(f" your final bill is {bill} ")


# love calculator
name1=input("what is your name? ")
name2=input("what is her name? ")
str_1=name1+name2
lr_str=str_1.lower()

t=lr_str.count('t')
r=lr_str.count('r')
u=lr_str.count('u')
e=lr_str.count('e')
true=t+r+u+e


l=lr_str.count('l')
o=lr_str.count('o')
v=lr_str.count('v')
e=lr_str.count('e')
love=l+o+v+e