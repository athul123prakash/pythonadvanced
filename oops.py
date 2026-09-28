# class EMPLOYEE:
#     def _init_(self):
#             self.id = int(input("Enter Employee ID: "))
#             self.name = input("Enter Name: ")
#             self.age = int(input("Enter Age: "))
#             self.salary = int(input("Enter Salary: "))
#             self.designation = input("Enter Designation: ")
#     def showsalary(self):
#         print("Salary ",self.salary)
#     def show(self):
#         print(self.name,self.id,self.age)
# e1=EMPLOYEE()
# e1.showsalary()
# e1.show()



# class STUDENT:
#         def _init_(self):
#                 self.rollnumber = int(input("Enter the Roll Number: "))
#                 self.mark1 = int(input("Enter the Mark 1: "))
#                 self.mark2 = int(input("Enter the Mark 2: "))
#                 self.mark3 = int(input("Enter the Mark 3: "))
#                 self.total = self.mark1 + self.mark2 + self.mark3
#
#         def show(self):
#                 print("Roll Number is", self.rollnumber, "Total Mark is ", self.total)

# s = STUDENT()
# s.show()




# class BOOK:
#     def _init_(self):
#         self.title=input("Enter the Title: ")
#         self.author=input("Enter the Author: ")
#         self.price=int(input("Enter the Price: "))
#         self.pages=int(input("Enter the Pages: "))
#         self.language=input("Enter the Language: ")
#     def show(self):
#         print("Title is ", self.title)
#         print("Author is ", self.author)
#         print("Price is ", self.price)
#         print("Pages is ", self.pages)
#         print("Language is ", self.language)
# b=BOOK()
# b.show()




# class BOOK:
#     def _init_(self):
#         self.title = input("Enter the Title: ")
#         self.author = input("Enter the Author: ")
#         self.price = int(input("Enter the Price: "))
#         self.page = int(input("Enter the Number of Pages: "))
#         self.language = input("Enter the Language: ")
#     def gettitle(self):
#         print("Title of the BOOK is", self.title)
#     def getauthor(self):
#         print("Author of the BOOK is", self.author)
#     def getprice(self):
#         print("Price of the BOOK is", self.price)
#     def settitle(self):
#         self.title = input("Enter the New Title: ")
#     def setauthor(self):
#         self.author = input("Enter the New Author: ")
#     def setprice(self):
#         self.price = int(input("Enter the New Price: "))
# b1 = BOOK()
# b1.gettitle()
# b1.getauthor()
# b1.getprice()
# b1.settitle()
# b1.setauthor()
# b1.setprice()






# class ACCOUNT:
#     def _init_(self):
#         self.name = input("Enter the Name: ")
#         self.accnumber = int(input("Enter the Account Number: "))
#         self.balance = int(input("Enter the Balance: "))
#     def withdraw(self):
#         amount = int(input("Enter the Amount to Withdraw: "))
#         self.balance = self.balance - amount
#     def deposit(self):
#         amount = int(input("Enter the Amount to Deposit: "))
#         self.balance = self.balance + amount
#     def showbalance(self):
#         print("Total Balance is", self.balance)
# a1 = ACCOUNT()
# a1.withdraw()
# # a1.deposit()
# a1.showbalance()



# class Account:
#     def __init__(self, name, balance):
#         self.acctnumber =int(input('enter your account number:'))
#         self.acctname = input('enter your account name:')
# while(1):
#     print('1.create account')
#     print('2.witdraw')
#     print('3.deposit')
#     print('4.show balance')
#     print('5.exit')
#
#     ch=int(input('enter your choice:'))
#     if ch==1:
#         a=Account()
#         l.append(a)
#         print(l)
#     elif ch==2:
#         number=int(input('enter your account number:'))
#         for i in l:
#             if i.acctnumber==number:
#                 i.withdraw()
#
#         else:
#             print("account not exist")
#
#     elif ch==3:
#         number = int(input('enter your account number:'))
#         for i in l:
#             if i.acctnumber==number:
#                 i.deposit()
#                 break
#         else:
#             print("account not exist")
#
#     elif ch==4:
#         number = int(input('enter your account number:'))
#         for i in l:
#             if i.acctnumber==number:
#                 i.showbalance()
#                 break
#         else:
#             print("account not exist")
#
#
#
# #Write a menu-driven Python program using a class Student to perform the following operations:
# #
# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.


# class Student:
#     def _init_(self):
#         self.rollnumber=int(input("Enter the Roll Number: "))
#         self.name=input("Enter the Name: ")
#         self.marks=int(input("Enter the Marks: "))
#     def update(self):
#         self.marks = int(input("Enter the New Marks: "))
#         print("Marks Updated")
#     def details(self):
#         print("Roll Number is",self.rollnumber)
#         print("Name is ", self.name)
#         print("Mark is ", self.marks)
# l=[]
# while(1):
#     print("Student MENU")
#     print("Option 1 : Add Student ")
#     print("Option 2 : Update Marks")
#     print("Option 3 : Display All Student Details")
#     print("Option 4 : Search Student")
#     print("Option 5 : Delete Student")
#     print("Option 6: Exit")
#     ch=int(input("Enter the Choice: "))
#     if ch==1:
#         s=Student()
#         l.append(s)
#     elif ch==2:
#         number=int(input("Enter the Roll Number: "))
#         for i in l:
#             if i.rollnumber==number:
#                 i.update()
#                 break
#             else:
#                 print("Student Does Not Exit")
    # elif ch==3:
    #     for i in l:
    #         i.details()
    # elif ch==4:
    #     number = int(input("Enter the Roll Number: "))
    #     for i in l:
    #         if i.rollnumber == number:
    #             i.details()
    #             break
    #         else:
    #             print("Student Does Not Exist")
    # elif ch==5:
    #     number = int(input("Enter the Roll Number: "))
    #     for i in l:
    #         if i.rollnumber == number:
    #             l.remove(i)
    #             break
    #         else:
    #             print("Student Does not Exist")
    # elif ch==6:
    #     exit()

# oops principle






