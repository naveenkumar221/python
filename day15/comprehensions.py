# list=[]
# for x in range(1,10):
#     if(x%2==0):
#         list.append(x)
# print(list)

# op=[x for x in range(1,10)]
# print(op)

# op=[x for x in range(2,15)]
# print(op)

# op=[x**2 for x in range(1,21)]
# print(op)

# list=["kiran","harish","pradeep","nandini","akhil"]
# op=[x.upper() for x in list]
# print(op)

# op=[x**2 for x in range(10,31) if x%2==0]
# print(op)

# list=["hiee","hell","welcome","something","king","queen"]
# op=[x.upper() for x in list if len(x)%2==0]
# print(op)

# list=["hie","hello","welcome","something","king","queen"]
# def vowelcount(ip):
#     count=0
#     for x in ip:
#         if (x in ["a","e","i","o","u"]):
#             count+=1
#     if(count%2==0):
#         return True
#     else:
#         return False
# op=[x.upper() for x in list if vowelcount(x)]
# print(op)

#create a list of perfect numbers from 1 to 50 range using comprehensions
# def perfectnumber(num):
#     sum=0
#     for x in range(1,num):
#         if(num%x==0):
#             sum+=x
#     if(sum==num):
#         return True
#     else:
#         return False
# op=[x for x in range(1,51) if perfectnumber(x)]
# print(op)
    
#create a list of armstrong numbers from 100 to 1000
# def armstrong(num):
#     n=num
#     temp=num
#     count=0
#     while(temp>0):
#         count+=1
#         temp=temp//10
#     temp=num
#     sum=0
#     while(temp>0):
#         id=temp%10
#         sum+=id**count
#         temp=temp//10
#     if(sum==n):
#         return True
#     else:
#         return False
# op=[x for x in range(100,1000) if armstrong(x)]
# print(op)

# aramstrong number
# def armstrong(num):
#     count=0
#     n=num
#     temp=num
#     while(temp>0):
#         count+=1
#         temp=temp//10
#     temp=num
#     sum=0
#     while(temp>0):
#         digit=temp%10
#         sum+=digit**count
#         temp=temp//10
#     if sum==n:
#         return True
#     else:
#         return False

# a=[x for x in range(100,1000) if armstrong(x)]
# print(a)


# perfect square using List Comprehensions

def perfectsquare(num):
    isperfect=False
    for x in range(1,num):
        if x**2==num:
            isperfect=True
            break
    if isperfect:
        return True
    else:
        return False
a=[i for i in range(1,101) if perfectsquare(i)]
print(f"perfect squares from 1 to 101:",a)

# sunny number using List Comprehensions

def sunny(num):
    issunny=False
    for x in range(1,num):
        if(x**2==num+1):
            issunny=True
            break
    if issunny:
        return True
    else:
        return False
a=[i for i in range(1,101) if sunny(i)]
print(f"sunny number from 1 to 101:",a)

# neon number using List Comprehensions

def neon(num):
    sqr=num**2
    sum=0
    while(sqr>0):
        id=sqr%10
        sum+=id
        sqr=sqr//10
    if sum==num:
        return True
    else:
        return False
a=[i for i in range(1,101) if neon(i)]
print(f"neon number from 1 to 101:",a)

# prime number using List Comprehensions

def prime(num):
    isprime=True
    if (num<=1):
        print("give greater than one number:")

    else:
        for x in range(2,num):
            if(num%x==0):
                isprime=False
                break
    if isprime:
        return True
    else:
        return False
a=[i for i in range(2,101) if prime(i)]
print(f"prime numbers from 1 to 101:",a)        



# revesrs using List Comprehensions

list=["hi","hello","welcome","to","here"]

def reverse(num):
        rev=""
        for i in range(len(num)-1,-1,-1):
            rev+=num[i] 
        return rev       
a=[reverse(j)  for j in list]
print(f"reversing the given list:",a)




























