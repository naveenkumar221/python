# # no error in the try block it will excute the sum
# try:
#     a=10
#     b=6 
#     sum=a+b
#     print(sum)
# except:
#     print("no error")


# # error in the try block str and int we can't add them then it was ecute thr no error
# try:
#     a=10
#     b="string"  
#     sum=a+b
#     print(sum)
# except:
#     print("no error")







try:
    x=int(input("enter the x value :"))
    y=int(input("enter the y value :"))
    print(x/y)
except TypeError as error:
    print("division can between numbers ",error)
except ZeroDivisionError as error:
    print(" we cant divide any number with 0",error)
except ValueError as error:
    print(" input should be a number",error)
except NameError:
    print("variable is not defined")
except IndentationError:
    print("indentation is not proper ")
except:
    print("something went wrong")
finally:
    print("code is excuted sucessfully here")





