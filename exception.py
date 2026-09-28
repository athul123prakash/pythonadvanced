# def fileread():
#     try:
#         filename = input("Enter filename: ")
#         f = open(filename, 'r')
#         s = f.read()
#         print(s)
#         f.close()
#     except:
#         print("File Not Found")
# def filewrite():
#     filename = input("Enter filename: ")
#     f=open(filename,"w")
#     s=input("Enter the Content: ")
#     f.write(s)
#     f.close()
# def fileappend():
#     filename = input("Enter filename: ")
#     f = open(filename, "a")
#     s = input("Enter the Content: ")
#     f.write(s)
#     f.close()
# def filesearch():
#     filename = input("Enter filename: ")
#     f = open(filename, "r")
#     c = input("Enter the Content to Search: ")
#     if c in f:
#         print("Content Found",c)
#     else:
#         print("Not Found")
# def filedelete():
#     filename = input("Enter filename: ")
#     import os
#     os.remove(filename)
#     print("File is Deleted")
# while (True):
#     print("Menu Driven-File Operations")
#     print('1.File Read')
#     print('2.File Write')
#     print('3.File Append')
#     print('4.File Search')
#     print('5.File Delete')
#     print('6.Exit')
#
#     ch = int(input("Enter the choice: "))
#     if ch == 1:
#         fileread()
#     elif ch == 2:
#         filewrite()
#     elif ch == 3:
#         fileappend()
#     elif ch == 4:
#         filesearch()
#     elif ch == 5:
#         filedelete()
#     else:
#         exit()
#

# try:
#     n1=int(input("Enter the number: "))
#     n2=int(input("Enter the number: "))
#     r=n1/n2
# except:
#     print("zero division error")
# else:
#     print("the result is ",r)
# finally:
#     print("Done")

# multiple except

# try:
#     n1=int(input("Enter the number: "))
#     n2=int(input("Enter the number: "))
#     r=n1/n2
# except ValueError:
#     print("valueerror")
# except zerodividsionerror:
#     print("ZeroDivisionError")
# else:
#     print("Success")
# finally:
#     print("Done")

#write a program that takes a number as input from user and finds the factorial of that number
# using math.factorial().use a try -except block to handle the value error if user inputs a
# number/character input

# import math
# try:
#     x = int(input("Enter a number: "))
#     result=math.factorial(x)
#     print("result" ,result)
#
# except ValueError:
#     print("Valueerror")
# else:
#     print("factorial",result)


#Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
#and division based on user choice. Handle invalid inputs and division by zero using exception handling.

# while True:
#     try:
#         print('1.Addition')
#         print('2.Subtraction')
#         print('3.multiplication')
#         print('4.Division')
#         print('5.exit')
#
#         n = int(input("Enter choice"))
#         if n in [1,2,3,4]:
#             n1 = int(input("Enter number"))
#             n2 = int(input("Enter number"))
#
#             s=n1+n2
#             d=n1-n2
#             m=n1*n2
#             q=n1/n2
#     except ZeroDivisionError:
#         print("Zero Division Error")
#     except ValueError:
#         print("Invalid Input")
#     except:
#         print("Error")
#     else:

        # if n == 1:
        #         print('Result', s)
        # elif n == 2:
        #         print("Result", d)
        # elif n == 3:
        #         print("Result", m)
        # elif n == 4:
        #         print("Result", q)
        # else:
        #     exit()

# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not
# exist

# try:
#      s=input("Enter the File Name: ")
#      f=open(s,"r")
#      s=f.read()
# except:
#      print("file Does not Exist")
# else:
#     print(s)
#     f.close()

#Given a Dictionary
#
# d={"name':"arun","age":23,"place":"ekm"}
# Write a program to ask the user to enter a key and display its value.
# Handle KeyError if key does not exist

# try:
#     d={"name":"arun","age":23,"place":"ekm"}
#     key=input("Enter the Key: ")
#     print(d[key])
# except:
#     print("Invalid Key")



# import math
# while(1):
#
#     try:
#          x = int(input("Enter a number: "))
#          result=math.factorial(x)
#          print("result" ,result)
#     except ValueError:
#          print("Valueerror")
#     else:
#          print("factorial",result)
#          break
#
# def fact():
# import math
# while(1):
#
#     try:
#          x = int(input("Enter a number: "))
#          result=math.factorial(x)
#          print("result" ,result)
#     except ValueError:
#          print("Valueerror")
#          fact()#recursive function is a fumction that call itself
#     else:
#          print("factorial",result)
#          break
# fact()


# def fact():
# import math
# while(1):
#
#     try:
#               x = int(input("Enter a number: "))
#               result=math.factorial(x)
#               print("result" ,result)
#          except ValueError as e:
#               print(e)
#               print (type(e))
#               print("Valueerror")
#             fact()#recursive function is a fumction that call itself
#          else:
#               print("factorial",result)
#               break
#     fact()


#raise

# try:
#     n=int(input("enter age"))
#     if n<18:
#         raise ValueError("not eligible for voting")
#     else:
#         print("eligible for voting")
# except ValueError as e:
#     print(e)


# class MyException(Exception):
#     pass
# try:
#     n=int(input("enter age"))
#     if n<18:
#         raise MyException("not eligible for voting")
#     else:
#         print("eligible for voting")
# except MyException as e:
#     print(e)


#Ask the user to enter a number.if the number is less than or equal to 0,
# raise a ValueError with the message "Number must be Positive"

# try:
#     n=int(input("enter a number"))
#     if n<=0:
#         raise ValueError("Number must be Positive")
#     else:
#         print("Number is Positive")
# except ValueError as e:
#     print(e)


#Ask the user to enter a password.if its length is less than 8 characters ,raise
#a customexception InvalidPasswordError with the message ("Password should be 8
# characters")

# class InvalidPasswordError(Exception):
#     pass
# try:
#     n=input("enter a Password")
#     if len(n)<8:
#         raise InvalidPasswordError("Password should be 8 characters")
#     else:
#         print("Valid Password")
# except InvalidPasswordError as e:
#     print(e)


#Ask the user to enter an amount and if the amount<balance ,raise customException
#InsuffientBalanceError with the message("Not Enough Balance.Transaction Failed")

class InsufficientBalanceError(Exception):
    pass
try:
    balance=5000
    amount=int(input("enter the amount"))
    if amount > balance:
        raise InsufficientBalanceError("Not Enough Balance.Transaction Failed")
    else:
        print("Transaction Success")
except InsufficientBalanceError as e:
    print(e)

































    


