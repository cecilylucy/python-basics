#Properties are variables that belong to a class. They store data for each object created from the class.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

# You can access a class property using a dot.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Corolla" )
print(car1.brand)
print(car1.model)

# You can modify the value of properties on objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Tobias", 25)
print(p1.age)
p1.age = 26
print(p1.age)

# Deleting a property
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Linus", 30)

del p1.age

print(p1.name)

# Class Properties vs Object Properties
# Properties defined inside __init__() belong to each object(instance properties)
# Properties defined outside methods belong to the class itself(class properties)

class Person:
    species = "Human" #Class property

    def __init__(self, name):
        self.name = name #instance property("

p1 = Person("Emily")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

# Modifying Class Properties. When you modify a class property, it affects all objects
class Person:
    lastname = ""

    def __init__(self, name):
        self.name = name

p1 = Person("Linus")
p2 = Person("Emily")

Person.lastname = "Refness"

print(p1.lastname)
print(p2.lastname)

# Adding new properties to existing objects
class Person:
    def __init__(self, name):
        self.name = name

p1= Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)


