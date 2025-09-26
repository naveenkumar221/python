# armstrong using str method

# num=int(input("enter the number:"))
# sum=0
# temp=num
# n=len(str(num))
# while(temp>0):
#     digit=temp%10
#     sum+=digit**n
#     temp=temp//10
# if sum==num:
#     print("armstrong")
# else:
#     print("not armstrong")


# armstrong  without using str method

# num=int(input("enter the number:"))
# n=num
# count=0
# temp=num
# while temp>0:
#     count+=1
#     temp=temp//10
# print(count)
# temp1=num
# sum=0
# while(temp1>0):
#     digit=temp1%10
#     sum+=digit**count
#     temp1=temp1//10
# if sum==n:
#     print("it is amstrong number")
# else:
#     print('it is not mstrong number')



# persons = list(range(1, 10))   # Creates a list of persons from 1 to 100
# count = 0                       # Starting index

# while len(persons) > 1:         # Loop until one person remains
#     killcount = (count + 1) % len(persons)   # Eliminate every second person
#     print(persons[killcount], 'is killed')
#     persons.pop(killcount)      # Remove that person from the list
#     count = killcount % len(persons)  # Update the next start position

# print('the last survivor is:', persons[0])  # Print the final survivor



# factorial
n=int(input("Enter the number: "))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)

# number is prime
n=int(input("Enter the number: "))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=i
if n>2:
    print("prime")
else:
    print("not prime")

# gcd
a=int(input("enter the number:"))
b=int(input("enter the number :"))
gcd=0
c=min(a,b)
for i in range(1,c+1):
    if a%i==0 and b%i==0:
        gcd=i
print(gcd)

# armstrong
num=int(input("Enter the number: "))
n=num
temp=num
count=0
while temp>0:
    count+=1
    temp=temp//10
sum=0
temp=num
while temp>0:
    id=temp%10
    sum+=id**count
    temp=temp//10
if sum==n:
    print("armstrong:")
else:
    print("not armstrong")

# reverse
num=int(input("enter the number: "))
rev=0
while num>0:
    id=num%10
    rev=rev*10+id
    num=num//10
print(rev)

# palindrme
num=int(input("Enter the number:"))
n=num
count=0
while num>0:
    id=num%10
    count=count*10+id
    num=num//10
if count==n:
    print("it is palidrome:")
else:
    print("it is not palidrome:")

# fibonacci
num=int(input("enter the terms:"))
a=0
b=1
for i in range(num):
    print(a,end=" ")
    sum=a+b
    a=b
    b=sum


