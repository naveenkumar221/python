#  1) check Even or odd
# n=int(input("Enter the number"))
# if n%2==0:
#     print("the number is even")
# else:
#     print("the number is odd" )

# 2) Divisible by 5 but not 10

# n=int(input("Enter the number "))
# if n%5==0 and n%10!=0:
#     print(" satisfy")
# else:
#     print("unsatisfy")


# 3) biggest among two numbers
# A=4
# B=7
# if A>=B:
#     print(f"Bggest is: {A}")
# else:
#     print(f"Biggest is: {B}")

# 4) Smallest among the numbers

# A=4
# B=7
# if A<=B:
#     print(f"Smallest is: {A}")
# else:
#     print(f"Smallest is: {B}")


#5) divible by 2,3,and 6

# n= int(input("Enter the number"))
# if n%2==0 and n%3==0 and n%6==0:
#     print("satisfy")
# else:
#     print("Unsatisfy")



# 6) voting eligibility

# age=int(input("Enter the number "))
# if age>=18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote ")


# 7) student pass or faill

# maths=int(input("Enter the marks"))
# physics=int(input("Enter the marks"))
# chemistry=int(input("Enter the marks "))
# if maths>=35 and physics>=35 and chemistry>=35:
#     print("pass")
# else: 
#     print("fail")


# 9) wether 2 sumbjest pass print pass else fail

# maths=int(input("Enter the marks"))
# physics=int(input("Enter the marks"))
# chemistry=int(input("Enter the marks "))

# marks=0
# if(maths>=35):
#     marks+=1
# if(physics>=35):
#     marks+=1
# if(chemistry>=35):
#     marks+=1
# if(marks==2):
#     print("you are pass: ")
# else:
#     print(" you are fail: ")


# 8) student pass one subject print pass

# maths=int(input("Enter the marks :"))
# physics=int(input("Enter the marks :"))
# chemistry=int(input("Enter the marks : "))

# if maths>=35 or physics>=35 or chemistry>=35:
#     print("pass")
# else:
#     print("fail")


# 10) biggest among the numbers

# A = 7
# B =4
# C = 9
# big = A
# if B > big:
#     big = B
# if C > big:
#     big = C

# print("Biggest is:", big)

# or this code 

# A = 7
# B = 4
# C = 3

# Biggest = max(A, B, C)
# print("Biggest is:", Biggest)



# 11)  smallest among the numbers

# A = 7
# B = 4
# C = 9

# small = A
# if B < small:
#     small = B
# if C < small:
#     small = C

# print("Smallest is:", small)

#or we use this code 

# A = 7
# B = 4
# C = 3

# smallest = min(A, B, C)
# print("Smallest is:", smallest)


# 12)  Perfect squre or not 

n=int(input("enter the number: "))
i=1
while i*i<=n:
    if i*i==n:
        is_perfectsquare=True
        break
    i+=1
if is_perfectsquare:
    print("it is perfect square:")
else:
    print("it is not a perfect square:")

    

    


