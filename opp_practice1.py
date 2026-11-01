#OOP stand for object oriented programming
# Python is an objet oriented language, allowing you to structure your code using classes and objects for better oraganization and reusability.
# When you create an object from a class, it inherits all the variables and functions inside that class.
# CLASSES/OBJECTS
# class
from loops import age_sorted


class Myclass: #class called Myclass
    x = 5 #property

# object
# Each object is independent and has its own copy of the class properties.
p1 = Myclass()
p2 = Myclass()
p3 = Myclass()


print(p1.x)
print(p1.x)
print(p1.x)

# code challenge
class Person: #create a class called person
    def __init__(self, name, age): #add an init that takes name and age as parameters
        self.name = name
        self.age = age

    def greet(self): #Add a method called greet that prints "Hello my name is" followed by the name
        print("Hello, my name is " + self.name)

p1 = Person ("John", 36) #create an object p1 of the class with name "John" and age 36.
p1.greet() #call the greet method on p1

