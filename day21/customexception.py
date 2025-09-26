# try:
#     age=int(input("enter the age: "))
#     if age<18:
#         raise ValueError("children are not allowed")
#     else:
#         print("welcome to the show")
# except ValueError as e:
#     print(e)
# except:
#     print("unexpetced error: ")

# # here we are raising a new error for my own rules with existing error class.

# class MyErrorClass(Exception):
#     pass

# try:
#     age=int(input("enter the age: "))
#     if age<18:
#         raise ValueError("children are not allowed")
#     else:
#         print("welcome to the show")
# except ValueError as e:
#     print(e)
# except:
#     print("unexpetced error: ")





#user and pasword error

userinfo={ 'user':'naveen','password':'naveen123'}
class InvalidUsernameError(Exception):
    pass
class InvalidPasswordError(Exception):
    pass

try:
    username=input("enter the username: ")
    password=input("enter the password: ")
    if (username != userinfo["user"]):
        raise InvalidUsernameError("invalid user name")
    elif(password != userinfo["password"]):
        raise InvalidPasswordError("invalid password")
    else:
        print("login sucess ")
except InvalidUsernameError as e:
    print(e)
except InvalidPasswordError as e:
    print(e)
except:
    print("something went worng")