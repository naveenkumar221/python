# list1=[1,2,3,4,5,6,7,8,9,10]
# even=len([x for x in list1 if x%2==0])
# odd=len([x for x in list1 if x%2!=0]) 
# print("the even numbers are: ", even)
# print("the odd numbers are: ", odd)

# even_count=0
# odd_count=0
 
# for num in list1:
#     if num%2==0:
#         even_count +=1
#     else:
#         odd_count +=1
# print(" the even nubers are", even_count)
# print("the odd nubers are ", odd_count)

# list1=[23,43,28,57,12,11]
# largest = list1[0]

# for i in list1:
#     if i>largest:
#         largest=i
# print("Largest number is:", largest)

# PALINDROME PROBLEM IN 2 METHODS

# def is_palindrome(s):
#     return s == s[::-1]      
# input ="madam"
# print(is_palindrome(input))


# str1="madam"
# palindrome=True
# for i in range(len(str1)//2):
#     if str1[i] != str1[-(i+1)]:
#         palindrome=False
#         break
# if palindrome:
#     print("it is a plaindrome")
# else:
#     print("it is not a paliindrome")

# SUM OF STRINGS IN THE INPUT

# s="abc123xyz"
# digits=0
# for char in s:
#     if char.isdigit():
#         digits +=int(char)
# print(digits)

# s="abc123xyz456"
# rev=0
# for i in s:
#     if i in "0123456789":
#         rev+=int(i)
# print(rev)


# FIND THE DUPLICATES FROM THE LIST 

# list1 = [1, 2, 2, 3, 1]
# list2 = []

# for item in list1:
#     if item not in list2:
#         list2.append(item)
# print(list2)

# PRINT PRIME NUMBERS FROM (1,50).............

# for num in range(2,51):
#     prime=True
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             prime=False
#             break
#     if prime:
#         print(num,end=" ")





#is prime........... 

# def is_prime(x):
#     if n<=1:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# n=int(input())
# print(is_prime(n))



#binary sum problem...............

# binary1=input("enter the number:")
# binary2=input("enter the number:")
# sum=0
# j=0
# for i in range(len(binary1)-1,-1,-1):
#     sum+=int(binary1[i])*(2**j)
#     j+=i
# k=0
# for i in range(len(binary2)-1,-1,-1):
#     sum+=int(binary2[i])*(2**k)
#     k+=i
# print(str(bin(sum)[2:]))




# name=input("enter the name: ")
# op=name[0]
# c=1
# for i in range(1,len(name)):
#     if name[i] == name[i-1]:
#         c+=1
#         if c<3:
#             op+=name[i]
#     else:
#         c=1
# print(op)



#cholocates problem 

a=21
t_c=a
w=a
while w>=3:
    id=w//3
    t_c+=id
    w=id+w%3
print(t_c)