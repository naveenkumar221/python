# print the perfect square or not 

num=int(input("enter the numebr :"))
issqure=False
for x in range(1,num):
    if x**2==num:
        issqure=True
        break
if issqure:
    print("it is a perfect number")
else:
    print("it is not a perfect number")


# print sunny number or not

num=int(input("enter the number: "))
issunny=False
for x in range(1,num):
    if(x**2==num+1):
        issunny=True
        break
if issunny:
    print("it is sunny number: ")
else:
    print("it is a not a sunny number: ")



# print the number is neon or not

num=int(input("entr the number:"))
sqr=num**2
sum=0
while(sqr>0):
    id=sqr%10
    sum+=id
    sqr=sqr//10
if sum==num:
    print("it is a neon number:")
else:
    print("it is not a neon number:")


# print prime number or not

num=int(input("enter the nunmber "))
isprime=True
if(num<=1):
     print("please give grester than 1: ")
else:
    for x in range(2, num):
         if(num%x==0):
             isprime=False
             break
    if isprime:
        print("it is prime number:")
    else:
        print("it is not a prime number:")
       



# print give list in revers

list=["hello","hii","welcome","good", "morning"]
for x in list:
    rev=""
    for i in range(len(x)-1,-1,-1):
        rev+=x[i]
    print(rev)
