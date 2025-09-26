# #primitive datatype

x=10  #integer
y=3.4   #float
z="kumar"     #string
k=3+9j    #complex
is_raining=True  #boolean
print(type(x))
print(type(y))
print(type(z))
print(type(k))
print(type(is_raining))

# #these are immutable and stores single value
value=30
print(id(value))  #before change
value=45
print(id(value))  #after change
print(value)


# #nonprimitive data type

vechiles=["bus","car","bike","lorry","cycle"]  #list
print(id(vechiles))

vechiles[2]="aeroplane" #updateing list
print(vechiles)

print(id(vechiles))





#1st
fruits = ["apple","mango","banna"]
#print first and last
print(fruits[0],fruits[-1])
#print total number of fruites  
print("Total number of fruites:", len(fruits))
#replace
fruits[1]="pineapple"
print(fruits)

#2nd
x = ["harish","naresh","suresh","mahesh"]
print(id(x)) #id of before change
#updating 
x[2]="kiran"
print(x) #printing updated list
print(id(x)) # id after changing

#3rd
data = [1,2,[4,5],[6,7],8,["something"]]
#print 4 value
print(data[2][0])
#print 7 value 
print(data[3][1])
#printing m 
print(data[5][0][2 ]) 

#4th

mixed =[1,2,"hi",12.5,True]
print (f"value: {mixed[0]}, Type: {type(mixed[0])}")
print(f"value: {mixed[2]}, Type: {type(mixed[2])}")