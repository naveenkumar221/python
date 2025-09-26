balance = float(input("Enter your current balance: "))
amount = float(input("Enter amount to withdraw: "))

if amount > balance:
    print("Insufficient balance.")
elif amount % 100 != 0: 
    print("Please enter the amount in multiples of 100.")
else:
    balance -= amount
    print(f"Withdrawal successful. Remaining balance: {balance:}")