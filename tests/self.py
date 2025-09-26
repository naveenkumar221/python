# # Print all prime numbers between 1 and 100.
# def prime(num):
#     isprime=True
#     if (num<=1):
#         print("give greater than one number:")

#     else:
#         for x in range(2,num):
#             if(num%x==0):
#                 isprime=False
#                 break
#     if isprime:
#         return True
#     else:
#         return False
# a=[i for i in range(2,101) if prime(i)]
# print(f"prime numbers from 1 to 101:",a)        

# # 2nd method 

# for num in range(2,101):
#     is_prime=True
#     for i in range(2, int(num**0.5) + 1):  
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=" ")


# # Check if a number is an Armstrong number (e.g., 153 → 1³ + 5³ + 3³ = 153).
# n=int(input("enter the number"))
# count=0
# temp=n
# num=n
# while temp>0:
#     count+=1
#     temp=temp//10
# sum=0
# temp=n
# while temp>0:
#     digit=temp%10
#     sum+=digit**count
#     temp=temp//10
# if sum==num:
#     print("arm")
# else:
#     print("not")

# # 2nd method
# def armstrong(num):
#     count=0
#     temp=num
#     n=num
#     while temp>0:
#         count+=1
#         temp=temp//10
#     sum=0
#     temp=num
#     while temp>0:
#         id=temp%10
#         sum+=id**count
#         temp=temp//10
#     if sum==n:
#         return True
#     else: 
#         return False
# a=[z for z in range(100,2000000) if armstrong(z)]
# print(a)


# # Find the factorial of a given number using a loop.
# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i 
# print(f"The factorial of {num} is {factorial}")


# # Print a number pyramid pattern like:

# # 1
# # 22
# # 333
# # 4444
# # 55555

# for x in range(1,6):
#    result=""
#    for y in range(1,x+1):
#       result+=str(x)
#    print(result)

# # 2nd method
# for x in range(1,6):
#     print(str(x)*x)

# # 🔤 Strings:
# # Write a function to check if a string is a palindrome. 

# def is_palidrome(text):
#     clean = text.replace (" " ," ").lowe()
#     return clean==clean[::-1]
# word=input("enter the string:")
# if is_palidrome:
#     print("it is palindrom:")
# else:
#     print("it is not palindrom:")

# Count the number of vowels and consonants in a string.


# Remove all duplicate characters from a string.
# def vowe_coun(text):
#     vowels='aeiouAEIOU'
#     vowels_c=0
#     consonant_c=0
#     i=0
#     while i<len(text):
#         char=text[i]
#         if char.isalpha():
#             if char in vowels:
#                 vowels_c+=1
#             else:
#                 consonant_c+=1
#         i+=1
#     return vowels_c,consonant_c
# str=input("enter the string:")
# vowel,consonants=vowe_coun(str)
# print(vowel)
# print(consonants)

# Write a function to capitalize the first letter of each word in a sentence.

# 📋 Lists:
# Write a program to find the largest and smallest number in a list.

# Remove all even numbers from a list.

# Merge two lists and remove duplicates.

# Create a list of squares from 1 to 10 using a loop and list comprehension.

# 🔣 Sets and Dictionaries:
# Write a program to find common elements in two sets.

# Count the frequency of each word in a sentence using a dictionary.

# Sort a dictionary by keys and by values.

# 🔧 Functions:
# Write a function to check if a number is even or odd.

# Write a function that takes a list and returns the sum of all elements.

# Create a function to convert Celsius to Fahrenheit.

# Write a function to check if a year is a leap year.

# Write a function that returns the fibonacci number at the nth position.

