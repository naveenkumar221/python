# person_info={"name":"kumar",
#              "age":22 ,
#              "gender":"male",
#              "height":5.6,
#              "address":{"d.no":"162-1-4",
#                         "streatname":"higtech city",
#                         "district":"vzm",
#                         "state":"AP",
#                         "pincode":535591},
#                         "material_status":"no",
#                         "skills":{"html","python"}}
# print(type(person_info))
# person_info["hobbies"]="video_games"
# print(person_info)
# print(person_info["address"])

num=input("enter the number")
numbers=num.split()
a=int(numbers[0]) -18
b=int(numbers[1]) -9
c=int(numbers[2])
d=int(numbers[3]) -9
op=f"{a},{b},{c},{d}"
print("op:",op)
