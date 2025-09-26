def sample():
    print("hello world")
def main(x):
    x()
main(sample)


def add(x,y):
    sum=x+y
    return sum
def sub(x,y):
    sub=x-y
    return sub
def calculator(fun,a,b):
    op=fun(a,b)
    print(op)
calculator(add,5,6)
calculator(sub,6,10)
calculator(lambda x,y:x*y,10,10)
calculator(lambda x,y:x%y,10,3)
calculator(lambda x,y:x/y,100,10)
calculator(lambda x,y:x//y,100,10)


#ip=[1,2,3,4,5]
#op=[1,4,9,16,15]


# def process(fun,x):
#     result=[]
#     for i in x:
#         op=fun(i)
#         result.append(op)
#     print(result)
# process(lambda x: x**2,[1,2,3,4,5])


# ip=['naveen','sai','kumar','seetha']
# op=['naveen hello','sai hello','kumar hello','seetha hello']

# def addinghel(fun,y):
#     result=[]
#     for i in y:
#         op=fun(i)
#         result.append(op)
#     return result
# op1=addinghel(lambda y: 'hello'+ y,['naveen','sai','kumar','seetha'])
# print(op1)

# op=map(lambda x:'hello'+x,['naveen','sai','kumar','seetha'])
# print(list(op))


# op=filter(lambda x:len(x)>5,['naveen','sai','kumar','seetha'])
# print(list(op))



# ecommerce_data = [
#     {"id": 1, "name": "iPhone 15", "category": "Electronics", "price": 79999, "stock": 25},
#     {"id": 2, "name": "Nike Air Max", "category": "Fashion", "price": 8999, "stock": 50},
#     {"id": 3, "name": "Organic Almonds 1kg", "category": "Grocery", "price": 1200, "stock": 100},
#     {"id": 4, "name": "Samsung 55-inch 4K TV", "category": "Electronics", "price": 54999, "stock": 15},
#     {"id": 5, "name": "Wooden Dining Table", "category": "Furniture", "price": 25999, "stock": 10},
#     {"id": 6, "name": "Sony WH-1000XM5 Headphones", "category": "Electronics", "price": 29990, "stock": 35},
#     {"id": 7, "name": "Adidas Hoodie", "category": "Fashion", "price": 4999, "stock": 60},
#     {"id": 8, "name": "Dettol Hand Wash (Pack of 3)", "category": "Health & Hygiene", "price": 299, "stock": 200},
#     {"id": 9, "name": "Harry Potter Box Set", "category": "Books", "price": 3499, "stock": 40},
#     {"id": 10, "name": "Lenovo IdeaPad Laptop", "category": "Computers", "price": 42999,"stock": 20}
# ]

# f_op=list(filter(lambda x: x['category']=='Fashion',ecommerce_data ))
# print(f_op)


# f_op=list(filter(lambda x: x['price']>=3000 and x['price']<=50000,ecommerce_data))
# print(f_op)


# from functools import reduce
# li=[3,4,9,6,7]
# op1=reduce( lambda x,y:x+y,li)
# op1=reduce( lambda x,y:x+y,li,5)
# op1=reduce( lambda x,y:x+y,li)

# print(op1)


# li=[10,4,6,7,9,2,8,23]
# op1=reduce(lambda x,y: x if x<y else y,li)
# op2=reduce(lambda x,y: x if x>y else y,li)
# print(op1)
# print(op2)

# ip=['I',"LOVE","MY","INDIA"]
# op1=reduce( lambda x,y : x if len(x)<len(y) else y,ip)
# op2=reduce( lambda x,y : x if len(x)>len(y) else y,ip)
# op3=reduce( lambda x,y : x+y,ip)
# print(op3)
# print(op2)
# print(op1)


# ip1=[4,6,3,2]
# #op=4632
# op1=reduce( lambda x,y : x*10+y,ip1 )
# print(op1)



