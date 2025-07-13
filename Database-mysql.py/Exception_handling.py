# try-except block :

try:
    a = int(input("enter first number"))
    b = int(input("enter second number"))
    n= a/b
except ZeroDivisionError as e:
    print(e) 
except ValueError as e:
    print(e)

print("After try-except block ")

# general exception :
try:
    a = int(input("enter first number"))
    b = int(input("enter second number"))
    n= a/b
except Exception as e:
    print("Error",e)

print("After try-except block ")

# else and final block :
try:
    a = int(input("enter first number"))
    b = int(input("enter second number"))
    a,b = 12,0
    n= a/b
    with open("abc.txt","r") as f:
        print(f.read())

except Exception as e:
    print("Error:",e) 

else : #this line is executed if there is no error in try block 
    print("inside else block.")

finally: #this block is executed always.
    print("Inside finally block.")

print("After try-except block. ")


# Custom Exception 
import traceback
try:
    a = int(input("enter first number"))
    b = int(input("enter second number"))
    a,b = 12,0
    if b== 0:
        raise ZeroDivisionError("b=0") 
    else:
       n= a/b
    with open("abc.txt","r") as f:
        print(f.read())

except Exception as e:
    print("Error:",e) 
    traceback.print_exc() #traceback shows on which line the error is caught

else : #this line is executed if there is no error in try block 
    print("inside else block.")

finally: #this block is executed always.
    print("Inside finally block.")

print("After try-except block. ")


# defining custom error exceptions
class AppError(Exception):
    '''Base class for application exceptions'''
    pass
class ValidationError(AppError):
    def __init__(self,message):
        super().__init__(message)

n=input("enter a number :")
try:
    if not n.isnumeric():
        raise ValidationError("Invalid numeric input from user.")
    print("you entered a valid number=",n)
except ValidationError as e:
    print(e)
    traceback.print_exc()

