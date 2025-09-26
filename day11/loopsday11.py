# n=int(input("Enter the number"))
# for i in range(1,11):
#     print(f"{n} X {i} = {n *i}")

# for i in range(1,21):
#     if i%2==0 and i%3==0:
#         print(f"{i} - fizzbuzz")
#     elif i%2==0:
#         print(f"{i} - fuzz")
#     elif i%3==0:
#         print(f"{i} - buzz")


# first ten natural number and squres of it

def sum_1(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum
def sum_2(n):
    sum=0
    for i in range(1,n+1):
        sum+=i*i
    return sum
n=10
print("sum of first natural number",n, sum_1(n))
print("sum of squarres of first ten numbers",n, sum_2(n))
