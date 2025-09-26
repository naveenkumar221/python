# 1) Variables 

x = 10          
name = "Naveen" 
pi = 3.14       
is_valid = True

print(x, name, pi, is_valid)

# 2) Swapping Two Variables (The Pythonic Way)

a,b = 6,7
a,b = b,a
print(a,b)

# 3) Memory Address of an Object

x = 50  
y = 50  
print(id(x))      
print(id(y))      
print(id(x) == id(y))

# 4) Know the Data Type

x = 10          
name = "Naveen" 
pi = 3.14       
is_valid = True

print(type(x))           #int
print(type(name))        # str   
print(type(pi))          #float
print(type(is_valid))    #bool


# 5) Type Conversion

s = "123"
print(int(s))         # 123
print(float(s))       # 123.0

# 6) Multiple Assignments

a, b, c = 1, 2, 3
print(a, b, c)

# 7) Assign Same Value to Multiple Variables

x = y = z = 0
print(x, y, z)

# 8) Delete a Variable

a = 10
del a
# print(a)  # This will throw an error





