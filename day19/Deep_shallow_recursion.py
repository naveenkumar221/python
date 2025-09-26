# Deep copy and shallow copy recursion

import copy

shopping_cart = [
    {"item": "Laptop", "price": 1000},
    {"item": "Phone", "price": 500}
]


shallow_cart = copy.copy(shopping_cart)


deep_cart = copy.deepcopy(shopping_cart)


shopping_cart[0]["price"] = 900

print("Original cart:", shopping_cart)
print("Shallow copy:", shallow_cart)
print("Deep copy:", deep_cart)






# sum of the numbers in the nestedlist

# def sum_nested(lst):
#     total = 0
#     for item in lst:
#         if isinstance(item, list):
#             total += sum_nested(item)  
#         else:
#             total += item
#     return total


# x = [1, 2, 3, [2,3,4], 4, 5, 6, [3, 4, 5, [2, 3, 4, [1, 2, 3]]]]
# print("Sum of all numbers:", sum_nested(x))




# Fibonacci series program

# def fibonacci(n):
   
#     if n == 0:
#         return 0
    
#     elif n == 1:
#         return 1
   
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# number_of_terms = 10


# print("Fibonacci series:")
# for i in range(number_of_terms):
#     result = fibonacci(i)  
#     print(result, end=" ")  
