

dashboard=False
user=(input("Enter your skil:"))
if(dashboard):
    if(user=="frontend"):
        print("he is frontend developer")
    elif(user=="backend"):
        print("he is backend developer")
    elif(user=="database"):
        print("he know about the database")
    elif(user=="frontend,backend and database"):
        print("he is a fullstack developer")
    else:
        print("he is still learning institute")
else:
    print("go and join 10k coders")