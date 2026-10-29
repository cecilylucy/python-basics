from yt_dlp.extractor.hellporno import HellPornoIE


def my_function():
    print("Hello from a function")
my_function() #Calling the function
my_function()
#can only strt with an underscore or letter, they are case-sensitive, can contain letters, numbers or underscores

# Temperature conversion
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(56))
# greeting

def get_greeting():
    return "Hello from a function"
print(get_greeting())

# same as
def get_greetings():
    return "Hello from a pycharm"
message = get_greetings()
print(message)

# pass>> Used when developing, allowing you to define the structure first and implement details later.
def my_function():
    pass


# >>>Arguments
# A function with one argument
def my_function(fname): # fname is the parameter
    print(fname + "Refsness")
my_function("Emil") #Emil is the argument
my_function("Tobias")
my_function("Linus")

# Parameters vs Arguments
#  A parameter is the variable listed inside the parentheses in the function definition
# An argument is the actual value that is sent to the function when it is called.
# If your function expects 2 arguments, you must call it with exactly 2 arguments;
def my_function(fname, lname):
    print(fname + "" + lname)

my_function("James", "Refsnes")

# default parameter values
def my_function(name = "friend"):
    print("Hello", name)

my_function("Emily")
my_function("Tobias")
my_function()
my_function("Linus")

def my_function(country = "Not a citizen"):
    print("Am a citizen of", country)
my_function("Nigeria")
my_function("Kenya")
my_function("Egypt")
my_function()

# Keyword argument>>>>The phrase keyword argument is often shortened to kwargs in python documention

def my_function(animal, name):
    print("I have a ", animal)
    print("My", animal + "'s name is ", name)
my_function(animal = "dog", name = "Buddy")

# Positional argument>>>>When you call a function argument without using keywords, they are called positional arguments.& And the order matters in Position arguments

def my_function(subject, teacher):
    print("My favorite subject is", subject)
    print("My teacher is called", teacher +".I love her")
my_function("Math", "Jane" )

# Missing positional and keyword arguments
def my_function(name, email, age):
    print("My name is", name, "I am" ,age, "Years old", "Myemail is", email)
my_function("name",email="Yahoo.com", age="23 ")

# Passing different Data Types>>>sending a list as an argument
def my_function(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

# sending dictionary as an argument
def my_function(person):
    print("name", person["name"])
    print("Age", person["age"])
my_person = {"name": "Emily", "age": 25}
my_function(my_person)

# return value
def my_function(x, y):
    return x+y
result = my_function(5,3)
print(result)

# A function that returns a list
def my_function():
    return["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

# a function that returns a turple
def my_function():
    return(10, 20)
x, y = my_function()
print("x:", x)
print("y:", y)








# PYTHON *ARGD AND *KWARGS >>>they allow functions to accept a unknown number of arguments
# using *args to accept any number of arguments

def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Emily", "Tobias", "Linus")
# The args parameter allows a function to accept any number of positional arguments.
#Inside the function, args becomes a tuple containing all the passed arguments:

# Accesing individual arguments from *args


def my_function(*args):
    print("Type:", type(args))
    print("First argument: ", args[0])
    print("Second argument: ", args[1])
    print("All arguments:", args)
my_function("Emily", "Tobias", "Linus")


# Using *args with regular Arguments
def my_function(greeting, *names):
    for name in names:
        print(greeting, name)
my_function("Hello", "Emily", "Tobias", "Linus")

#  Afunction that calculates the sum of any number of values
def my_function(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

# Finding the maximum value
def my_function(*numbers):
    if len(numbers) ==0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
print(my_function(3, 7, 2, 9, 1))

# Arbitrary keyword Arguments - **kwargs>>If you do not know many how many keywords will be passed into your function, add two asterisks ** before the parameter name.
# Arbitry keywords are often shortened to **kwargs in python documentation
# Kwargs is a parameter that allows a function to accept any number of keyword arguments
# Using keyword to accept any number of keyword arguments
def my_function(**kid):
    print("His last name is " +kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

# Accesing values from **kwargs
def my_function(**myvar):
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)
my_function(name = "Tobias", age = 30, city= "Bergen")

# Using **kwargs with regular Arguments
def my_function(username, **details):
    print("Username:", username)
    print("Additional details: ")
    for key, value in details.items():
        print(" ", key + ":", value )
my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

# Combining *args and **kwargs
# You can use both *args and **kwargs in the same function.
#
# The order must be:
#
# regular parameters
# *args
# **kwargs

def my_function(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("Keyword arguments: ", kwargs)
my_function("User info", "Emil", "Tobias", age = 25, city = "Oslo")

# Unpacking Lists with  *
def my_function(a, b, c):
    return a+b+c
numbers = [1, 2, 3]
result = my_function(*numbers) #same as: my_function(1, 2, 3)
print(result)

# Using ** to unpack a dictionary into keyword arguments
def my_function(fname, lname):
    print("Hello", fname, lname)

person = {"fname": "Emily", "lname": "Refnes"}
my_function(**person) #same as: my_function(fname="Emil", lname="Refnes"






