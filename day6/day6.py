# problems on using while condition
#amstrong or not 
num=int(input("enter the number:"))
n=num
count=0
temp=num
while temp>0:
    count+=1
    temp=temp//10
print(count)
temp=num
sum=0
while(temp>0):
    digit=temp%10
    sum=digit**count+sum
    temp=temp//10
if sum==n:
    print("it is amstrong number")
else:
    print('it is not mstrong number')

# the number is neon or not
num=int(input("enter the number"))
square= num*num
sum=0
n=square
while(n>0):
    id=n%10
    sum+=id
    n=n//10
if sum==num:
    print(num,"neon")
else:
    print(num,"not neon")

# the number is sunny number or not
num=int(input("enter the number"))
num1=num+1
i=1
num2=False
while i*i <=num1:
    if i*i == num1:
        num2=True
        break
    i+=1
if num2:
    print("it is the summy number")
else:
    print("it is not sunny number")

# Print Square of Numbers from 1 to N
n = int(input("Enter a number: "))
i = 1
while i <= n:
    print(f"{i}^2 = {i**2}")
    i += 1

# palindrome or not 
num=121
n=num
rev=0
while(num>0):
    id=num%10
    rev=rev*10+id
    num=num//10
print(rev)
if rev==n:
    print("is palindrome")
else:
    print("it is not")


    

    
    
