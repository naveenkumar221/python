# n=5
# for i in range(5):
#     for j in range(5):
#         print("*",end="")
#     print()

# *****
# *****
# *****
# *****
# *****

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*", end=" ")
#         else:
#             print(" ",end=' ')
#     print()

# * * * * * 
# *       * 
# *       * 
# *       * 
# * * * * * 


# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# * 
# * * 
# * * *
# * * * *
# * * * * *


# n=5
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# * * * * * 
# * * * * 
# * * *
# * *
# *


# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# 1 
# 1 2 
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# n=5
# for i in range(n,0,-1):
#     for j in range(1,n+1):
#         print(j,end=" ")
#     print()

# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5


# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(2*i+1):
#         print("*",end=" ")
#     print()


#         * 
#       * * * 
#     * * * * *
#   * * * * * * *
# * * * * * * * * *


# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print("",end="")
#     for j in range(2*i+1):
#         print("*",end="")
#     print()


# *
# ***
# *****
# *******
# *********

# n = 5
# for i in range(n, 0, -1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()


# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1


# n = 5
# for i in range(1, n+1):
#     for j in range(i):
#         print(i, end=" ")
#     print()


# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5



# n = 5
# for i in range(1, n+1):
#     # spaces
#     for j in range(n-i):
#         print(" ", end=" ")
#     # numbers
#     for j in range(1, 2*i):
#         print(j, end=" ")
#     print()


#         1
#       1 2 3
#     1 2 3 4 5
#   1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8 9



# n = 5
# # Upper half
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end=" ")
#     for j in range(2*i+1):
#         print("*", end=" ")
#     print()
# # Lower half
# for i in range(n-2, -1, -1):
#     for j in range(n-i-1):
#         print(" ", end=" ")
#     for j in range(2*i+1):
#         print("*", end=" ")
#     print()



#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *


# n = 5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end=" ")
#     for j in range(2*i+1):
#         if j == 0 or j == 2*i or i == n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


#         *
#       *   *
#     *       *
#   *           *
# * * * * * * * * *

