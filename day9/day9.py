number=int(input("Enter the values"))
if number%2==0:
    p="even"
else:
    p="odd"
if number > 0:
    sign = "positive"
elif number < 0:
    sign = "negative"
else:
    sign = "zero"

print(f"The number {number} is {p} and {sign}.")




