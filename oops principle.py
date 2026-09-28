# class Parent:
#     def m1(self):
#         print("in class parent m1")
#     def m2(self):
#         print("in class parent m2")
# class Child(Parent):
#     def m3(self):
#         print("in class child m3")
# c=Child()
# c.m1()
# c.m2()
# c.m3()
#
# #method overriding
#
# class Child(Parent):
#     def m3(self):
#         print("in class method m3")
#     def m1(self):
#         print("in class method m1")
# c=Child()
# c.m1()
# c.m2()
# c.m3()
#
# class Child(Parent):
# #     def m3(self):
#         print("in class method m3")
#     def m1(self):
#         super().m1()#modify/extend the parent functionality
#         print("in class method m1")
# c=Child()
# c.m1()
# c.m2()
# c.m3()


# class Person:
#      def _init_(self):
#          self.name=input("Enter the Name: ")
#          self.age=int(input("Enter the Age: "))
#      def show(self):
#          print("Name is ",self.name,"Age is ",self.age)
# class Student(Person):
#      def _init_(self):
#          super()._init_()
#          self.marks = int(input("Enter the Marks: "))
#          self.rollno = int(input("Enter the Roll Number: : "))
#      def show(self):
#          super().show()
#          print("Mark is ",self.marks,"Roll Number is ",self.rollno)
#      def update(self):
#          self.marks=int(input("Enter the New Marks: "))
#          print("Updated Marks",self.marks)
# s=Student()
# s.show()
# s.update()


#next qn
# class Category:
#     def __init__(self):
#         self.categoryname=input("Enter the Category Name: ")
#     def show(self):
#         print("Category Name is ",self.name)
# class Product(Category):
#     def __init__(self):
#         super().__init__()
#         self.name=input("Enter the Product Name: ")
#         self.price=int(input("Enter the Product Price: "))
#         self.quantity=int(input("Enter the Product Quantity: "))
#         self.totalprice=(self.price*self.quantity)
#     def show(self):
#         super().show()
#         print("Product Name is ",self.name)
#         print("Product Price is ",self.price)
#         print("Product Quantity is ",self.quantity)
#     def total_price(self):
#         print("Total Price",self.price*self.quantity)
# p1=Product()
# p1.show()
# p1.total_price()

#qn

# class Company:
#     def _init_(self):
#         self.company_name=input("Enter the Company Name: ")
#         self.location=input("Enter the Location: ")
#     def display(self):
#         print("Name of the Company is ",self.company_name)
#         print("Location of the Company is ",self.location)
# class Employee(Company):
#     def _init_(self):
#         super()._init_()
#         self.id=int(input("Enter the Id: "))
#         self.name=input("Enter the Name: ")
#         self.salary=int(input("Enter the Salary: "))
#     def display(self):
#         super().display()
#         print("Id is ",self.id,"Name is ",self.name,"Salary is ",self.salary)
#     def update(self):
#         self.salary=self.salary*0.10+self.salary
#         print("Updated Salary is ",self.salary)
# e1=Employee()
# e1.display()
# e1.update()

# multiple inheritance
# class Hospital:
#     def __init__(self):
#         self.hospital_name=input("Enter the Hospital Name: ")
#         self.location=input("Enter the Location: ")
#         self.phone=int(input("Enter the Phone Number: "))
#     def details(self):
#         print("Name of the Hospital is ",self.hospital_name)
#         print("Location of the Hospital is ",self.location)
#         print("Phone Number is ",self.phone)
# class Department:
#     def __init__(self):
#         self.department_name=input("Enter the Department Name: ")
#         self.doctor_name=input("Enter the Doctor Name: ")
#     def display(self):
#         print("Name of the Department is ",self.department_name)
#         print("Doctor Name is ",self.doctor_name)
# class Patient(Hospital,Department):
#     def __init__(self):
#         Hospital.__init__(self)
#         Department.__init__(self)
#         self.patient_name=input("Enter the Patient Name: ")
#         self.age=int(input("Enter the Age: "))
#         self.admission_date=int(input("Enter the Admission Date: "))
#         self.bed_no=int(input("Enter the Bed No: "))
#         self.discharge_date=int(input("Enter the Discharge Date: "))
#     def update_discharge_date(self):
#         self.discharge_date=int(input("Enter the Discharge Date: "))
#     def full_summary(self):
#         Hospital.details(self)
#         Department.display(self)
#         print("Patient Name is ",self.patient_name)
#         print("Age is ",self.age)
#         print("Admission Date is ",self.admission_date)
#         print("Bed No is ",self.bed_no)
#         print("Discharge Date is ",self.discharge_date)
#
#
# p1=Patient()
# p1.update_discharge_date()
# p1.full_summary()

# polymorphism

# class A:
#     def f(self):
#         print("in first function f")
#     def f(self,a)
#         print("in second function f")
#     def f(self,a,b):
#         print("in third function f")
# a=A()
# a.f()
# a.f(10)
# a.f(20,30)

# Abstraction

# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass
#     @abstractmethod
#     def get_perimeter(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self):
#         self.length=int(input("Enter the length of the rectangle: "))
#         self.breadth=int(input("Enter the breadth of the rectangle: "))
#     def get_area(self):
#         print("area is" ,self.length*self.breadth)
#     def get_perimeter(self):
#         print("perimeter is" ,2*(self.length+self.breadth))
# s=Square()
# s.get_area()
# s.get_perimeter()class Square(Shape):
#     def __init__(self):
#         self.length=int(input("Enter the length of the square: "))
#         self.length=int(input("Enter the length of the square: "))
#     def get_area(self):
#         print("area is" ,self.length*self.length)
#     def get_perimeter(self):
#         print("perimeter is" ,4*(self.length*self.length))
#
# r=Rectangle()
# r.get_area()
# r.get_perimeter()


# from abc import ABC, abstractmethod
# class Employee(ABC):
#     def __init__(self):
#           self.empid = int(input("Enter the employee id: "))
#           self.name = input("Enter the employee name: ")
#     @abstractmethod
#     def calculate_salary(self):
#         pass
# class Fulltime_Employee(Employee):
#     def __init__(self):
#         super().__init__()
#         self.salary=int(input("Enter the employee salary: "))
#     def calculate_salary(self):
#         print("salary is" ,self.salary)
# class Parttime_Employee(Employee):
#     def __init__(self):
#         super().__init__()
#         self.hour=int(input("Enter the employee hour: "))
#         self.rate=int(input("Enter the employee rate: "))
#     def calculate_salary(self):
#         print("salary is" ,self.hour*self.rate)
#
# print("\n------------")
# e=Fulltime_Employee()
# e.calculate_salary()
# print("\n------------")
# e1=Parttime_Employee()
# e1.calculate_salary()




















