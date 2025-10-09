products = [ 
{"id": 1, "name": "Laptop", "price": 45000}, 
{"id": 2, "name": "Smartphone", "price": 15000}, 
{"id": 3, "name": "Headphones", "price": 2000}, 
{"id": 4, "name": "Keyboard", "price": 1200}, 
{"id": 5, "name": "Mouse", "price": 800}, 
{"id": 6, "name": "Charger", "price": 500}, 
{"id": 7, "name": "USB Cable", "price": 300}, 
{"id": 8, "name": "Backpack", "price": 2500} 
]

cart=[]

def viewProducts():
    print("view Products is excuted ")
    for p in products:
        print(f"prodcut name is {p['name']} and price is {p['price']}")

def viewCart(cart):
    if not cart:
        print("cart is empty")
        return
    print("your cart ")
    for item in cart:
        print(f"ID: {item['id']} | {item['name']} | Quantity: {item['quantity']} | Price: {item['price']}")
    print()

def addToCart(products,cart,product_id,quantity):
    product=None
    for items in products:
        if items["id"]==product_id:
            product=items
            break
    if not product:
        print("the cart is empty ")
        return
            
    
    for item in cart:
        if  item["id"]==product_id:
            item["quantity"]+=quantity
            item["price"]+=product['price']*quantity
            print(f"Updated {item['name']} | Quantity: {item['quantity']} | Price: {item['price']}")
            return
    
    new_item={
        "id":product["id"],
        "name":product["name"],
        "price":product["price"]*quantity,
        "quantity":quantity
    }

    cart.append(new_item)
    print(f"Added items are {new_item["name"]} and {new_item["price"]}")
    

def updateCart(cart):
    id=int(input("enter the ID"))
    for item in cart:
        if item['id']==id:
            print("item quantity updated sucessfully")
            break
        else:
            print("product not Found")

def removeFromcart(cart):
    id=int(input("enter the product id to remove: "))
    for item in cart:
        if item['id']==id:
            cart.remove(item)
            print(f"{item['name']} removed from cart")
            return
    print(" product id is not found  ")


def checkOut(cart):
    if not cart:
        print("cart is empty")
        return
    print("checkout")
    total= sum(item['price'] for item in cart )
    for item in cart:
        print(f"{item['name']} | {item['quantity']} | {item['price']}")
    print("total amount",total)
    print("thank you for shoping ")

def menu():
    while True:
        print("Shopping cart menu ")
        print("1.view cart ")
        print("2.Add to cart ")
        print("3.view Products ")
        print("4.Update cart ")
        print("5.Remove from cart ")
        print("6.Checkout & Exit ")


        ip=int(input("enter the choice from 1 to 6 : "))
        if ip == 1:
            viewCart(cart)
        elif ip==2:
            pid=int(input("enter the product id :"))
            qty=int(input("enter the quqntity: "))
            addToCart(products,cart,pid,qty)
        elif ip==3:
            viewProducts()
        elif ip==4:
            updateCart(cart)
        elif ip==5:
            removeFromcart(cart)
        elif ip==6:
            checkOut(cart)
            break
        else:
            print("invalid options")

menu()


