sub1=int(input("Enter the sub1 marks"))
sub2=int(input("Enter the sub2 marks"))
sub3=int(input("Enter the sub3 marks"))
sub4=int(input("Enter the sub4 marks"))
sub5=int(input("Enter the sub5 marks"))
sub6=int(input("Enter the sub6 marks"))
total=sub1+sub2+sub3+sub4+sub5+sub6
avg=total/6

if avg>=90:
    print("A Grade")

elif(avg>=80 and 89<=avg):
    print("B Grade")

elif(avg>=70 and 79<=avg):
    print("C Grade")

elif(avg>=60 and 69<=avg):
    print("D Grade")
else:
    print("Fail")



