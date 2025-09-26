op=map(lambda x:'hello'+x,['naveen','sai','kumar','seetha'])
print(list(op))


op=filter(lambda x:len(x)>5,['naveen','sai','kumar','seetha'])
print(list(op))


#task

#1
op1=map(lambda x:'+91' + x,["9876543210","9123456780","9988776655"] )
print(list(op1))

#2
#exc=0.01132843
usdt=map(lambda x: x * 0.01132843,[10,25,40,100])
print(list(usdt))

#5
user=map(lambda x: x.lower()+'@gmail.com',["Harish",'Sushma','Naveen'] )
print(list(user))

#3
mail=filter(lambda x: x.endswith('@gmail.com'),["harish@gmail.com",'abc@yahoo.com','xyz@gmail.com'])
print(list(mail))

#4
name=filter(lambda x:len(x)<=5,['Pen','Notebook','Laptop','CHarger','Bag'])
print(list(name))

#6
expire=filter(lambda x : x < 2025,[2022,2023,2025,2026])
print(list(expire))

#7



#8
high=filter(lambda x:x>=40000 ,[25000,45000,60000,15000,80000])
print(list(high))


#9