# check even or odd number 

n=int(input("enter the number:"))
if n%2==0:
    print("it is even")
else:
    print("it is odd")

# age classifier

age=int(input("enter the age: "))
if age<13:
    print("Child")
elif 13<=age <20:
    print("teen")
elif age>=20:
    print("adult")


# number positive or negative

num=int(input("enter the number: "))
if num>0:
    print("positive")
elif num<0:
    print("negative")
elif num==0:
    print("the number is zero")
else:
    print("give the correct number")


# divisibility check 3 and 5

num=int(input("enter the number: "))
if num%3==0 and num%5==0:
    print("it is divisible by both 3&5")
elif num%3==0:
    print("it is divisible by 3")
elif num%5==0:
    print("it is divisible by 5")
else:
    print("it was not dvisible by both ")

# Largest of Two Numbers

a=int(input("enter the number: "))
b=int(input("enter the number:"))
if a>b:
    print(a,"is big")
else:
    print(b," is big ")


#Triangle Validity Checker

s1=int(input("enter the side:"))
s2=int(input("enter the side:"))
s3=int(input("enter the side:"))
if (s1+s2>s3) and (s2+s3>s1) and (s3+s1>s2):
    print("it was forms a triangle")
else:
    print("it was not form atriangle ")


#for loop
#Print each character of a string

n="Hello"
for i in n:
    print(i,end=" ")


# Sum of first 10 natural numbers

sum=0
for i in range(1,11):
    sum+=i
print(sum)

# Print even numbers from 1 to 20

for i in range (1,21) :
    if i%2==0:
        print(i)

# print the list

list=["pen", "pencil", "eraser"]
for i in list:
    print(i)

#print set

my_set = {"apple", "banana", "cherry"}
for i in my_set:
    print(i)


#Count how many items are in a set using a loop

count=0
colors = {"red", "blue", "green", "yellow"}
for i in colors:
    count+=1
print(count)


#Print all keys and values in a dictionary

person = {"name": "Alice", "age": 25, "city": "Delhi"}
for i in person:
    print(f"{i}:{person[i]}")


# Count how many values in a dictionary are greater than 50

count=0
scores = {"math": 45, "english": 55, "science": 80, "history": 40}
for i in scores:
    if scores[i]>50:
        count+=1
print(count)


#Create a new dictionary with only items where the value is even

data = {"a": 1, "b": 4, "c": 6, "d": 3}
s={}
for i in data:
    if data[i]%2==0:
        s[i]=data[i]
print(s)




        
