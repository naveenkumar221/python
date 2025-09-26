# 🟢 Easy (1–40)

# 1. Check if a number is positive or negative.

def positive(num):
    if num>0:
        return "positive"
    elif num<0:
        return "negative"
    else:
        return "equal"   
print(positive(-10))
print(positive(10))
print(positive(0))


#or we use 

num=int(input("enter the number: ")) 
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("equal")

# 2. Check if a number is even or odd.

def even(num):
    if num %2 == 0:
        return "even"
    else:
        return "odd"
print(even(11))

#or............

num=int(input("enter the number: "))
if num%2==0:
    print("even")
else:
    print("odd")

# 3. Find the largest of two numbers.

def find_larg(a,b):
    if a>b:
        return "a is big"
    elif b>a:
        return "b is big"
    else:
        return "equal"

print(find_larg(10,8))
print(find_larg(10,18))
print(find_larg(10,10))

#or............

num1=int(input("enter the number1: "))
num2=int(input("enter the number2: "))
if num1>num2:
    print("num 1 is bigger")
elif num2>num1:
    print("num2 is bigger")
else:
    print("either both are equal")

# 4. Find the smallest of two numbers.

def find_larg(a,b):
    if a<b:
        return "a is small"
    elif b<a:
        return "b is small"
    else:
        return "equal"

print(find_larg(10,8))
print(find_larg(10,18))
print(find_larg(10,10))

# or.....................

num1=int(input("enter the number1: "))
num2=int(input("enter the number2: "))
if num1>num2:
    print("num2 is smaller ")
elif num2>num1:
    print("num1 is smaller ")
else:
    print("both are equal ")


# 5. Check if a year is a leap year.

def leap_ye(year):
    if year % 400==0 or (year %4==0 and year %100!=0):
        return "leap_year"
    else:
        return "not a laep_year"
print(leap_ye(2023))
print(leap_ye(2024))
print(leap_ye(2025))

# or ................

year=int(input("enter the year : "))
if year%400==0 or (year%4==0 and year%100 !=0):
    print("leap year ")
else:
    print("not a leap year ")

# 6. Check if a number is divisible by 5.

def div_5(num):
    if num%5==0:
        return "divisible by 5"
    else:
        return "not divisible by 5"
print(div_5(10))
print(div_5(13))
print(div_5(25))
print(div_5(44))

# or..............

num=int(input("enter the number: "))
if num%5==0:
    print("it is divisible by 5 ")
else:
    print("it  is not divisble by 5")


# 7. Check if a number is divisible by both 3 and 5.

def div_both(num):
    if num%3==0 and num%5==0:
        return "divisible by both"
    else:
        return "not divisible by both"
print(div_both(10))
print(div_both(15))
print(div_both(30))
print(div_both(46))

# or.................

num=int(input("enter the number: "))
if num%3==0 and num%5==0:
    print("it is divisble by both ")
else:
    print("it is not divisble by both ")

# 8. Check if a number is within 1 to 100.

def between(num):
    # if num=>1 and num<=100:
    if 1 <= num <= 100:
        return "between inside"
    else:
        return "outside"
print(between(10))
print(between(0))
print(between(1001))
print(between(-20))

# or........

num=int(input("enter the number"))
if 1<= num <=100:
    print("in between")
else:
    print("out side")

# 9. Check if a character is a vowel.

def check_vowel(chr):
    if chr.lower() in "aeiou":
        return " is vowel"
    else:
        return " is not vowel"
print(check_vowel("a"))
print(check_vowel("B"))
print(check_vowel("E"))
print(check_vowel("z"))

# or............

chr=input("enter the single character :")
if chr.lower() in 'aeiou':
    print("it is vowel")
else:
    print("it is not in vowel")
    
    
    
    
# 10. Check if a character is a digit.

def check_dig(num):
    if num.isdigit():
        return "is digit"
    else:
        return "it is not"

print(check_dig('10'))

# 11. Check if a number is single-digit or not.

def single_dig(num):
    if -9<=num<=9:
        return "single digit"
    else:
        return "not a single digit"

print(single_dig(9))
print(single_dig(-9))
print(single_dig(0))
print(single_dig(40))
print(single_dig(-91))


# or.......
num=int(input("enter the digit: "))
if -9<= num <=9:
    print("single digit ")
else:
    print("not single digit ")


# 12. Check if a person is eligible to vote.

def acct_vote(age):
    if age>=18:
        return "eligible to vote"
    else:
        return "not eligible"

print(acct_vote(19))
print(acct_vote(15))
print(acct_vote(-19))

# or.......

person=int(input("enter the age: "))
if person>=18:
    print("eligible to vote")
else:
    print("not eligible to vote ")


# 13. Check if a number is divisible by 2 or 3.

def divsi_both(num):
    if num %2==0:
        return "divisible by 2"
    elif num%3==0 :
        return  "divisible by 3"

print(divsi_both(6))
print(divsi_both(15))

# or...........

num=int(input("enter the number: "))
if num%2==0 or num%3==0:
    print("divisible by the 2 or 3")
else:
    print("not divisible by the both ")

# 14. Check if a number is divisible by 7 but not by 5.

def divi_one(num):
    if num %7==0 and num %5 !=0:
        return "divisible by 7 not 5"
    else:
        return "not divisble by 7 but 5"

print(divi_one(14))
print(divi_one(25))


# or....................

num=int(input("enter the nunber: "))
if num%7==0 and num%5!=0:
    print("it is divisible by 7 not 5")
else:
    print("it is not divisible by both ")

# 15. Check if temperature is below freezing point.

def temp_dec(num):
    if num<0:
        return "freezing"
    elif num==0:
        return "equal"
    else:
        return "normal"

print(temp_dec(-9))
print(temp_dec(0))
print(temp_dec(25))

# or...........

temp=int(input("enter the temperature: "))
if temp<0:
    print("frezzing point")
elif temp==0:
    print("it is equal")
else:
    print("it is normal state")

# 16. Compare two variables and print which is greater.

def compar_va(a,b):
    if a>b:
        return "a is big"
    elif b>a:
        return "b is big"
    else:
        return "equal"

print(compar_va(4,5))
print(compar_va(14,5))
print(compar_va(14,14))


# or.........
a=int(input("enter the 1st number: "))
b=int(input("enter the second number: "))
if a>b:
    print("a is bigger")
elif b>a:
    print("b is greater")
else:
    print("both values are equal ")

# 17. Print grade based on marks using if-else ladder.

def grrade_she(marks):
    if marks>=90:
        return "A grade"
    elif marks>=75:
        return "B grade"
    elif marks>=50:
        return "C grade"
    elif marks>=35:
        return "D grade"
    else:
        return "fail"
print(grrade_she(91))
print(grrade_she(76))
print(grrade_she(71))
print(grrade_she(40))
print(grrade_she(30))

# or...........
marks=int(input("enter the marks: "))
if marks>=90:
    print("A grade")
elif marks>=75:
    print("B grade")
elif marks>=65:
    print("c grade")
elif marks >=50:
    print("D grade ")
elif  marks>=35:
    print("E grade")
else:
    print("fail ")

# 18. Print if a number is in range 10 to 20.

def ran_num(num):
    if 10<=num<=20:
        return "in between"
    else:
        return "out of range"

print(ran_num(11))
print(ran_num(31))
print(ran_num(9))


# or...............
num=int(input("enter the number: "))
if 10<=num<=20:
    print("in between ")
else:
    print("outside of the range")

# 19. Print if a number is not in range 10 to 20.

def ran_num(num):
    if 10<=num<=20:
        return "in between"
    else:
        return "out of range"

print(ran_num(31))
print(ran_num(31))
print(ran_num(9))

# or......

num=int(input("enter the number: "))
if 10<=num<=20:
    print("in between ")
else:
    print("outside of the range")


# 20. Find the absolute value of a number using conditions.

def abso_val(num):
    if num<0:
        return -num
    else:
        return num

print(abso_val(-10))
print(abso_val(10))
print(abso_val(0))

# or.............

num=int(input("enter the number "))
if num<0:
    print(-num)
else:
    print(num)

# 21. Check if number is multiple of 10.

def multi_pl(num):
    if num%10==0:
        return "multiple of 10"
    else:
        return "not multiple of 10"

print(multi_pl(30))
print(multi_pl(25))
print(multi_pl(101))

# or............

num=int(input("enter the number: "))
if num%10==0:
    print("it is divisble by 10")
else:
    print("it is not divisible")

# 22. Classify person as child, teenager or adult.

def person(age):
    if age<=13:
        return "child"
    elif age<=18:
        return "teenager"
    else:
        return "adult"
print(person(12))
print(person(17))
print(person(22))

# 23. Check if number is three-digit.

def three_dig(num):
    if 100<=abs(num) <= 999:
        return "three-digit"
    else:
        return "not 3-digit"
print(three_dig(100))
print(three_dig(99))
print(three_dig(-100))
print(three_dig(987))
print(three_dig(1000))

# 24. Compare age of two people.

def compar_ag(age1,age2):
    if age1>age2:
        return "age1 is bigger"
    elif age1<age2:
        return "age2 is bigger"
    else:
        return "bot are same age "
    
print(compar_ag(21,19))
print(compar_ag(21,39))
print(compar_ag(19,19))

# 25. Check if number is less than 1000 and divisible by 11.

def check_nu(num):
    if num<1000 and num%11==0:
        return "less than 1k and divisible by 11"
    else:
        return "not less than and not divisible"
print(check_nu(99))
print(check_nu(9999))
print(check_nu(1001))

# 26. Check if number lies between two given numbers.

def num_lise(num,a,b):
    if a<num<b:
        return "between"
    else:
        return "not in between"

print(num_lise(15,10,20))
print(num_lise(10,20,40))

# 27. Check if both numbers are even.

def bot_num(a,b):
    if a%2==0 and b%2==0:
        return "even"
    else:
        return "not even"

print(bot_num(4,6))
print((bot_num(5,7)))

# 28. Check if number is non-zero and negative.

def number_n(num):
    if num!=0 and num<0:
        return "True"
    else:
        return "False"
print(number_n(-3))
print(number_n(0))

# 29. Print if number is zero, negative or positive.

def number_t(num):
    if num>0:
        return "positive"
    elif num<0:
        return "negative"
    else:
        return "zero"

print(number_t(5))
print(number_t(-9))
print(number_t(0))

# 30. Check if a triangle is valid (3 sides).

def traingle(a,b,c):
    if a==b==c:
        return "valid"
    else:
        return "not valid"
    
print(traingle(10,10,10))
print(traingle(10,32,14))
print(traingle(15,15,15))

# 31. Print season based on month number.

def season_1(month):
    if month in [12,1,2]:
        return "winter"
    elif month in [3,4,5]:
        return "spring"
    elif month in [6,7,8]:
        return "summer"
    elif month in [9,10,11]:
        return "rainy"
    else:
        return "invalid month"

print(season_1(10))
print(season_1(17))
print(season_1(8))

# 32. Check if number is divisible by 4 or ends with 0.

def divis_nu(num): 
    if num %4==0 or str(num).endswith('0'):
        return "divsible 4 and endswith 0"
    else:
        return " not divisible by 4 not end with 0"

print(divis_nu(40))
print(divis_nu(44))
print(divis_nu(45))

# 33. Check if a number is perfect square or not.

def perfect_sqr(num):
    i=1
    while i*i<=num:
        if i*i==num:
            return "is a perfect square"
            break
        i+=1
    else:
        return "not perfect square "

print(perfect_sqr(10))
print(perfect_sqr(25))

    
# 34. Print day of week from number (1–7).
def week(day):
    if day==1:
        return "sunday"
    elif day==2:
        return "monday"
    elif day==3:
        return "tuesday"
    elif day==4:
        return "wed"
    elif day==5:
        return "thurs"
    elif day==6:
        return "frida"
    elif day==7:
        return "sat"
    else:
        return "not a valid day"
    
print(week(3))
print(week(0))
print(week(7))

# 35. Print electricity bill slab using if-else.

def electri(units):
    if units<=100:
        return units*1.5
    elif units<=200:
        return 100*1.5+(units-100)*2.5
    elif units<=300:
        return 100*1.5+100*2.5+(units-200)*3.5
    else:
        return "invalid units"
print(electri(99))
print(electri(150))
print(electri(250))

# 36. Identify if input is integer or float (using input check).

def number(val):
    if isinstance(val,float):
        return "float"
    else:
        return "integer"
    
print(number(2.5))
print(number(25))
print(number(25.5))

# 37. Check if number is divisible by 9 but not 6.

def divis_ble(num):
    if num%9==0 and num%6!=0:
        return "divsible by 9 but not 6"
    else:
        return "not divisible by both"

print(divis_ble(27))

# 38. Print which digit is larger in a two-digit number.

def dig_it(num):
    id=num//10
    temp=num%10
    if id > temp:
        return "id is greater"
    if temp>id:
        return "temp is greate"
    else:
        return "both are equal"
    
print(dig_it(47))
print(dig_it(98))

# 39. Print pass/fail based on minimum marks.

def min_mar(marks):
    if marks>=35:
        return "pass"
    else:
        return "fail"
print(min_mar(34))
print(min_mar(30))
print(min_mar(43))

# 40. Find if three numbers are equal.

def thre_num(a,b,c):
    if a==b==c:
        return "3 numbers are equal"
    else:
        return "3 numbers are not equal"
print(thre_num(10,10,10))
print(thre_num(23,44,32))

# 🟠 Medium (41–80)

# 41. Find largest among three numbers using nested if.

def large_st(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    if b>c:
        return b
    else:
        return c
    
print(large_st(4,5,6))
print(large_st(4,9,6))
print(large_st(14,5,6))

# 42. Find smallest among three numbers using nested if.

def small_st(a,b,c):
    if a<b:
        if a<c:
            return a
        else:
            return c
    if b<c:
        return b
    else:
        return c
    
print(small_st(6,5,4))
print(small_st(6,2,4))
print(small_st(3,5,4))

# 43. Check if triangle is equilateral, isosceles or scalene.

def traingle(a,b,c):
    if a==b==c:
        return "equilateral"
    elif a==b or b==c or c==a:
        return "isosceles"
    else:
        return "scalene"
print(traingle(9,9,9))
print(traingle(10,10,8))
print(traingle(4,8,8))
print(traingle(8,9,10))

# 44. Check if a number is Armstrong (3-digit only).

def arms_trong(num):
    if 100<=num<=999:
        n=sum(int(digit)**3 for digit in str(num))
        if n==num:
            return "armstrong number"
        else:
            return "not a armstrong number"
    else:
        return "not a 3 digigts number"
print(arms_trong(153))
print(arms_trong(135))

# 45. Check if a number is prime.

def is_prime(num):
    if num<=1:
        return "it is not a prime"
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return "is not a prime"
        return "is prime"
print(is_prime(7))

# 46. Use nested if to classify number (positive/negative/zero).

def number(num):
    if num>=0:
        if num==0:
            return "it is 0"
        else:
            return "it is positive"
    else:
        return "it is negative"
print(number(-9))
print(number(0))
print(number(9))

# 47. Print week day using elif ladder.

def week(day):
    if day==1:
        return "sunday"
    elif day==2:
        return "monday"
    elif day==3:
        return "tuesday"
    elif day==4:
        return "wed"
    elif day==5:
        return "thurs"
    elif day==6:
        return "frida"
    elif day==7:
        return "sat"
    else:
        return "not a valid day"
    
print(week(3))
print(week(0))
print(week(7))

# 48. Find roots of quadratic equation using if.
# 49. Check eligibility for scholarship (based on marks & income).
# 50. Check driving license eligibility (age & test).
# 51. Create calculator using if-elif.

def calculater(a,b,operation):
    if operation=="+":
        return a+b
    elif operation=="-":
        return a-b
    elif operation=="*":
        return a*b
    elif operation=="%":
        return a%b
    elif operation=="/":
        return a/b
    elif operation=="//":
        return a//b
    elif operation=="**":
        return a**b
    else:
        return "please give the valid number"
    
print(calculater(10,5,'+'))
print(calculater(10,5,'-'))
print(calculater(10,5,'*'))
print(calculater(10,3,'%'))
print(calculater(10,5,'/'))
print(calculater(10,5,'//'))
print(calculater(10,5,'**'))

# 52. Check voting eligibility based on age and nationality.
# 53. Use multiple ifs to check divisibility by 2, 3, 5.
# 54. Find if a year is century year.
# 55. Determine quadrant of a point (x, y).
# 56. Check if number is palindrome (without string).
# 57. Use conditions to assign grade based on percentage.
# 58. Classify employee based on experience.
# 59. Compare three values using if-elif-else.
# 60. Find max and min from three values using logic.
# 61. Identify shape based on sides (if-else).
# 62. Check if triangle is right-angled.
# 63. Classify number as even, odd, or divisible by 5.
# 64. Determine if temperature is cold, warm, or hot.
# 65. Check admission eligibility (age, score, etc.).
# 66. Classify product rating (1 to 5 stars).
# 67. Find profit or loss using conditional logic.
# 68. Determine if number is special 2-digit number.
# 69. Check pass/fail/distinction using marks.
# 70. Detect triangle type from angles.
# 71. Grade based on multiple subject marks.
# 72. Identify largest digit in 3-digit number.
# 73. Use if-else to simulate light signals (R/Y/G).
# 74. Validate input is within certain range.
# 75. Compare area of two rectangles.
# 76. Compare volumes of two cubes.
# 77. Calculate BMI and classify range.
# 78. Determine overtime pay based on hours.
# 79. Use nested if to categorize shopping discounts.
# 80. Identify leap year and century leap year./

# 🔴 Hard (81–100)

# 81. Simulate basic ATM withdrawal and balance check.
# 82. Compare three numbers and sort them.
# 83. Validate triangle with side and angle conditions.
# 84. Calculate electricity bill with conditional slabs.
# 85. Classify water usage into categories.
# 86. Find leap year from string input (convert and check).
# 87. Identify strong number (sum of factorials of digits).
# 88. Find largest of four numbers using if.
# 89. Print calendar month name from number.
# 90. Generate logic gate outputs using conditions.
# 91. Create simple grade book with if-else.
# 92. Calculate tax based on salary brackets.
# 93. Check if date is valid (dd-mm-yyyy).
# 94. Evaluate a logical expression using if.
# 95. Check triangle inequality condition.
# 96. Create billing system with offers based on price.
# 97. Find second largest among three numbers.
# 98. Simulate vending machine logic with coins.
# 99. Validate user credentials using conditional logic.
# 100. Simulate simple chatbot decision using if-elif.