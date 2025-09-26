# sum of the squares 
# num=126
# sqr=0
# while(num>0):
#     id=num%10
#     sqr +=id**2
#     num=num//10
# print(sqr)

# to find the count of total digits

# num=12504
# count=0
# while(num>0):
#     id=num%10
#     count+=1
#     num=num//10
# print(count)


#revesing a number without converting into string


num=123654
n=num
rev=0
while(num>0):
    id=num%10
    rev=rev*10+id
    num=num//10
print(rev)

# if n==rev:
#     print("is palindrome")
# else:
#     print("it is not a palindrome")


# num=int(input("enter the number : "))
# sum=0
# num1=num
# num2=num
# len=0
# while(num1>0):
#     num1=num1//10
#     len+=1
# while(num>0):
#     k=num%10
#     sum+=k**len
#     num=num//10
# if sum == num2:
#     print("is amstrong")
# else:
#     print("is not")




