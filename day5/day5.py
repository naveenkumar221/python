# Print the first 10 natural numbers using a for loop
for i in range(1,11):
    print(i)

#Sum of digits of a number using a while loop
num=12345
sum=0
while(num>0):
    sum+=num%10
    num=num//10
print("sum of digits:",sum)

# Print even numbers between 1 to 50
for i in range(1,51):
    if i%2==0:
        print(i,end=" ")

# Use break to stop when a number divisible by 7 is found
for i in range(1,51):
    if i%7==0:
        print(" the number is divisible by 7: ",i) 
        break

# Use continue to skip numbers divisible by 3
for i in range(1,51):
    if i%3==0:
        print("the number is divisible by 3",i)
        continue
   