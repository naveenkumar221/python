#variables defines values
x=5
y=4.6
z="Sai"
print(x)
print(y)
print(z)

#variables check and print the type of data
x=5
y=3.6
z="kumar"
print(type(x))
print(type(y))
print(type(z)) 

#variables whithout any data 
x=int(input("Enter the number"))
y=int(input("Enter the number"))
z=int(input ("Enter the name"))
#which type of data it was show
print(type(x))
print(type(y))
print(type(z))
#here it was show the memory address 
print(id(x))
print(id(y))
print(id(z))

#formating print 
name="uppe"
loves="puri"
year=3
print(f"{name} and {loves} are lover since {year} years")
