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
cards = ["1234567890123456", "9876543210987654"]
masked_cards = list(map(lambda c: '*' * 12 + c[-4:], cards))
print("Masked Cards:", masked_cards)


#8
high=filter(lambda x:x>=40000 ,[25000,45000,60000,15000,80000])
print(list(high))


#9
products = ["apple", "mango", "orange"]
formatted_products = list(map(lambda p: f"Product: {p.capitalize()}", products))
print("Formatted Product Labels:", formatted_products)

#10
marks = [35, 80, 55, 20, 90]
passed_students = list(filter(lambda m: m >= 40, marks))
print("Students Passed:", passed_students)


#11
passwords = ["abc123", "Admin@123", "hello", "Pa$$word"]
strong_passwords = list(filter(lambda p: len(p) >= 8 and ('@' in p or '$' in p), passwords))
print("Strong Passwords:", strong_passwords)

#12
transactions = ["1000-CREDIT", "500-DEBIT", "1200-CREDIT", "200-DEBIT"]
#map using
amounts = list(map(lambda t: int(t.split('-')[0]), transactions))
print("Amounts:", amounts)
#filter using
credits = list(filter(lambda t: 'CREDIT' in t, transactions))
debits = list(filter(lambda t: 'DEBIT' in t, transactions))
print("Credits:", credits)
print("Debits:", debits)

