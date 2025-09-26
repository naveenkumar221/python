a=int(input("Enter num1: "))
b=int(input("Enter num2: "))
def add():
    print(a+b) 
def sub():
    print(a-b)
def mul():
    print(a*b)
def div():
    print(a/b)

op=input("enter the operation") 
if(op=="add"):
    add()
elif(op=="sub"):
    sub()
elif(op=="mul"):
    mul()
elif(op=="div"):
    div()
else:
    print("Enter the correct operation : add,sub,mul,div")