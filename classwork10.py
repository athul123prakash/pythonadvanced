#Create a class named Movie with attributes moviename,year,language,director,rating
# and methods display_details() and update_rating()

# class Movie:
#     def __init__(self):
#         self.movie_name=input("Enter Movie Name: ")
#         self.year=int(input("Enter Movie Year: "))
#         self.language=input("Enter Movie Language: ")
#         self.director=input("Enter Movie Director: ")
#         self.rating=int(input("Enter Movie Rating: "))
#     def display_details(self):
#         print("Movie name is:", self.movie_name)
#         print("Movie year is:", self.year)
#         print("Movie language is:", self.language)
#         print("Movie director is:", self.director)
#         print("Movie rating is:", self.rating)
#     def update_rating(self):
#         self.new_rating=int(input("Enter New Rating : "))
#         print("rating is updated")
# m=Movie()
# m.display_details()
#m.update_rating()
#m.display_details()

# 2.Create a Python program using Hierarchical Inheritance for a vehicle management system.
#
# Create a parent class Vehicle with the attributes brand, model, color, and year.
# Add a method display() in the Vehicle class to display these details.
# Create two child classes:
# Car with an additional attribute mileage
# Bike with an additional attribute cc
# Override the display() method in both child classes to display the vehicle details along with their respective additional attributes.
# Create objects of both classes, accept input from the user, and display the details.

# class Vehicle:
#     def __init__(self):
#         self.brand=input("enter brand:")
#         self.model=input("enter model:")
#         self.color=input("enter color:")
#         self.year=input("enter year:")
#     def display(self):
#         print("brand:",self.brand)
#         print("model:",self.model)
#         print("color:",self.color)
#         print("year:",self.year)
# # class Car(Vehicle):
#     def __init__(self):
#         super().__init__()
#         self.mileage=int(input("enter mileage:"))
#     def display(self):
#         super().display()
#         print("mileage:",self.mileage)
# class Bike(Vehicle):
#     def __init__(self):
#         super().__init__()
#         self.cc=int(input("enter cc:"))
#     def display(self):
#         super().display()
#         print("cc:",self.cc)
# c=Car()
# c.display()
# b=Bike()
# b.display()

# Abstraction





