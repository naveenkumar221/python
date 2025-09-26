#packing 

# x=1,2,3
# print(x)

#unpacking

# values=[9,8,7,6]
# a,b,c,d=values
# print("a:",a,"b:",b,"c:",c,"d:",d)


# mk=[9,7,5,4]
# a,*b=mk
# print(a,b)


# a=6
# b=7

# a,b=b,a
# print(a,b)


# a=[1,2]
# b=[3,4]
# print(a+b)

# a=(1,2)
# b=(3,4)
# print(a+b)
# op=(*a,*b)
# print(op)


# a=[1,2]
# b=[3,4]
# op=[*a,*b]
# print(op)


# a={1,2}
# b={3,4}
# op={*a,*b}
# print(op)


x={"name":"naveen","gender":"male"}
y={"city":"hyd","role":"frontend"}
op={**x,**y}
print(op)