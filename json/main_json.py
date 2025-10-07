import json

#first list
first_list=["jhon","Ravi","Priya","swathi"]
with open('products.json','w') as f:
    json.dump(first_list,f)
print(first_list)

#reading the list
with open('products.json','r') as f:
    data=json.load(f)
print(data)

#adding the new names
new_names=["Arjun","Karthik","Naveen"]
data.extend(new_names)
print(data)

#removing the names 
name_remove="Naveen"
if name_remove in data:
    data.remove(name_remove)
print(data)

#again updating the list
with open('products.json','w') as f:
    json.dump(data,f)
