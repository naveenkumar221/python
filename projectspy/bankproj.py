import random

class BANK():

    T_Holders=[]

    def create_new_Account(self):

        H_Details={}

        data=random.randint(100000000000,999999999999)
        H_Details['name']=input("enter the user name:")
        H_Details['M_no']=input("enter the mobile number: ")
        H_Details['Adhar no'] = input("enter the Adhar_no: ")
        H_Details['E-mail']=input("enter email: ")

        H_Details['Acc_no']=data
        H_Details['Acc_Type']=input("Enter Acctype:zero/savings------>")
        while True:
            if H_Details['Acc_Type']=='savings':
                balance=input("deposit 1000 rupess.......")
                if balance==1000:
                    H_Details['balance']=balance
                    break
                else:
                    print("deposite the amount sir ")
            if H_Details['Acctype']=='zero':
                balance=input("Deposit 500 rupees....")
                if int(balance)>=500:
                    H_Details['balance']=balance
                    break
        obj2=BANK.H_Details.append(H_Details)
        print(obj2)










obj1=BANK()
obj1.create_new_Account()



