import re


#using match

ip="hello world"
regex=r"hello"
op=re.match(regex,ip)
print(op)    #op:<re.Match object; span=(0, 5), match='hello'>

ip="world hello"
regex=r"hello"
op=re.match(regex,ip)
print(op)  #op: None because it was taking from starting index

#using search

ip="hello world"
regex=r"hello"
op=re.search(regex,ip)
print(op)     #op:<re.Match object; span=(0, 5), match='hello'>

ip="world hello"
regex=r"hello"
op=re.search(regex,ip)
print(op)     #op: <re.Match object; span=(6, 11), match='hello'>

ip=" name hello hello world hello"
regex=r"hello"
op=re.search(regex,ip)
print(op)  

ip="world"
regex=r"hello"
op=re.search(regex,ip)
print(op)       #op:None   if it is not there then it show the none


#using find
ip="world hello"
regex=r"hello"
op=re.findall(regex,ip)
print(op)         #op:['hello']


ip="hello hello world hello"
regex=r"hello"
op=re.findall(regex,ip)
print(op)           #op: ['hello', 'hello', 'hello']


ip="world"
regex=r"hello"
op=re.findall(regex,ip)
print(op)   #op: []


#patterns

#Singel character

regex=r"c.t"
ip="catcoyutcut"
op=re.search(regex,ip)
print(op)

#matches 3-lette 
regex=r"p.t"
ip="okcdpkt"
op=re.search(regex,ip)
print(op)

#IFSC Code 

regex=r"^sbin"
ip="sbin09987989"
op=re.search(regex,ip)
print(op)

regex=r"^apgv"
ip="apgv09987989"
op=re.search(regex,ip)
print(op)

regex=r"gmail.com$"  #$ end with
ip="naveen@gmail.com"
op=re.search(regex,ip)
print(op)

regex=r"\s"  #white space
ip="hello world"
op=re.search(regex,ip)
print(op)

regex=r"[A-Z]"  
ip="helloOworld"
op=re.search(regex,ip)
print(op)


regex=r"[aeiou]"   # findall vowels 
ip="elemintd"
op=re.findall(regex,ip)
print(op)

regex=r"[^aeiou]"  # find all the consonent
ip="elemintd"
op=re.findall(regex,ip)
print(op)

regex=r"^\w{5,15}$"  
ip="hello6worlojynf"
op=re.findall(regex,ip)
if op:
    print("valid")
else:
    print("invalid")


#FOR PANCARD NUMBER

regex=r"^[A-Z]{5}\d{4}[A-Z]{1}$"
ip="LDHPK1447A"
op=re.search(regex,ip)
if op:
    print("valid",ip)
else:
    print("invalid")



#FOR DRIVING LICENSE VALIDATION

regex=r"^[A-Z]{2}\d{2}[A-Z]{2}\d{4}$"
ip="AB12CD3456"
op=re.search(regex,ip)
if op:
    print("valid",ip)
else:
    print("invalid")


# Date Validation (YYYY-MM-DD)

regex=r"^\d{4}-\d{2}-\d{2}$"
ip="2023-09-25"
op=re.search(regex,ip)
if op:
    print("valid",ip)
else:
    print("invalid")

# Phone number validation

regex=r""
















