
#  Part C: Write the Program (5 Questions)
#  1. Write a program that takes a number and prints whether it is a multiple of 3, 5, or both.
n=int(input("enter the number:"))
if n%3==0 and n%5==0:
    print("it is multiple of both:")
elif n%3==0:
    print("it is multiple of 3")
elif n%5==0:
    print("it is multiple of 5")
else:
    print("it is not multiple of both")

#  2. Write a Python function to check whether a number is a palindrome.
num=int(input("enter the number:"))
temp=num
sum=0
while(num>0):
    digit=num%10
    sum=sum*10+digit
    num=num//10
if temp==sum:
    print("it is palindrome:")
else:
    print("not a palindrome")

#  3. Write a program that takes a list of numbers and prints the sum of all even numbers.
def even(list):
    sum=0
    for x in list:
        if x%2==0:
            sum+=x
    return sum
list=[1,2,3,4,5,6,7,8,9,10]
print("sum of even",even(list))

#  4. Write a user-defined function that takes a string and returns it in reverse.
def string(rever):
    return rever[::-1]
st=("enter the string")
print("revers of string",string(st))

#  5. Write a Python program to print the Fibonacci sequence up to n terms using a loop
n=int(input("enter the terms: "))
a=0
b=1
for x in range(n):
    print(a,end=" ")
    sum=a+b
    a=b
    b=sum