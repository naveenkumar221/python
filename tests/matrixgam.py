list1=[1,1,1]
list2=[2,2,2]
list3=[3,3,3]
matrix=[list1,list2,list3]
print(f"{list1}\n{list2}\n{list3}")
position=input("where you need hide the money?")
row_1=int(position[0])
coloum_2=int(position[1])
selected=matrix[row_1-1]
selected[coloum_2-1]='X'
print(f"{list1}\n{list2}\n{list3}")




nav=input("enter the more numbers seperated by spaces:")
list =nav.split()
count=0
for nav in list:
    count= count+1
print(count)
for i in range(count): 
    list[i]=int(list[i])
total=0
for x in list:
    total = total+x

avg=total/count
print(round(avg))




numbers=input("enter the numbers: ")
numbers_list=numbers.split()
count=0
for number in numbers_list:
    count=count+1
print(count)
for i in range(count):
    numbers_list[i]=int(numbers_list[i])
maximum_number=numbers_list[0]
for number in numbers_list:
    if number > maximum_number:
        maximum_number=number
print(maximum_number)
    

