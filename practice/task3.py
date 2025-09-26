import random
import math

# 1. Generate 5 random floats between 0 and 1:

random_float=[random.random() for i in range(5) ]
print(random_float)

# 2. Dice roll simulator using random.randint.
random_dice=random.randint(1,6)
print(random_dice)

# 3. Convert 90 degrees to radians.
convert_90=math.radians(90)
print(convert_90)

# 4. Factorial of a user-given number.
num=int(input("Enter the number: "))
fact=math.factorial(num)
print(fact)

# 5. Shuffle a list of 10 integers.
list=[1,2,3,4,5,6,7,8,9,10]
random.shuffle(list)
print(list)

# 1. Lottery draw of 6 unique numbers from 1 to 49.
random_choices=random.choices(range(1,50),k=6)
print(random_choices)

# 2. Approximate using Monte Carlo.
count=0
points=100000
for i in range(points):
    x=random.random()
    y=random.random()
    if x**2 + y**2<=1:
        count+=1
aprox=4*count/points
print(aprox)

# 3. Calculate compound interest using math.pow.
p=100000
r=5
t=3
n=4
# A = P * (1 + r/n)^(nt)
a=p*math.pow((1+r/(100*n)),n*t)
print(round(a,2))

# 4. Trigonometry calculator using degrees.
# 5. Roll two dice 1000 times and plot the sum frequency.

