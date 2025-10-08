import json


# #using dumps 
# op=["mango","orange","apple"]
# with open('data1.json','w') as k:
#     # k.write(json.dumps(op)) 
#     json.dump(op,k)

# with open('data1.json','r') as k:
#     data=k.read()
#     print(data[5])    #here the data is acting like complete string 
   
# with open('data1.json','r') as k:
#     # data=k.read()
#     # convert=json.loads(data)   #here loads is changing from string to the original pposition
#     # print(convert[2])   
#     data=json.load(k)    
#     print(data[1])    



# # checking the fruit in the list or not 

# op1=input("enter the fruits name: ")
# with open ('data1.json') as f:
#     data=json.load(f)
#     if op1 not in data["fruits"]:
#         data["fruits"].append(op1)
#         print("excuted sucessfully")
#     else:
#         print(f"{op1} is already is there")
# with open('data1.json',"w") as f:
#     json.dump(data,f)



# # removing the particular fruits


# op1=input("enter the fruit name: ")
# name="data1.json"
# with open(name,'r') as f:
#     data=json.load(f)
#     if op1 not in data['fruits']:
#         print(f"{op1} is not avaliable ")
#     else:
#         data['fruits'].remove(op1)
#         print(f"{op1} is removed sucessfully ")
# with open (name,'w') as f:
#     json.dump(data,f)


# # remove operation for the authorised person 

# op1=input("enter the fruit name: ")
# user=input("enter the user name: ")
# name="data1.json"
# with open(name,'r') as f:
#     data=json.load(f)
#     if user in data['users']:
#         if op1 not in data['fruits']:
#             print(f"{op1} is not avaliable ")
#         else:
#             data['fruits'].remove(op1)
#             print(f"{op1} is removed sucessfully ")
#     else:
#         print(f"{user} you were not the authorised person to remove")
# with open (name,'w') as f:
#     json.dump(data,f)


#adding operation only for authorised persons

add=input("enter the fruit name: ")
user=input("enter the user name: ")
name="data1.json"
with open(name,'r') as f:
    data=json.load(f)
    if user in data['users']:
        if add  in data['fruits']:
            print(f"{add} is already there")
        else:
            data['fruits'].append(add)
            print(f"{add} is added sucessfully ")
    else:
        print(f"{user} you were not the authorised person to adding option" )
with open (name,'w') as f:
    json.dump(data,f)


