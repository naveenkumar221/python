a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
c = float(input("Enter length of side c: "))

if a==b==c:
  print("Equilateral triangle")
elif a==b or b==c or c==a:
  print( "Isosceles triangle")
elif(a!=b!=c):
  print("Scalene triangle")
elif(a+b>c or b+c>a or c+a>b):
  print("Forms a inquality triangle")
else:
  print("not forms a triangle")

