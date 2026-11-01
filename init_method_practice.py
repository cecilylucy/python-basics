class Person:
    def __init__(self, name, age = 18):
        self.name = name
        self.age = age

p1 = Person("John")
p2 = Person("Joseph", 28)

print(p1.name, p1.age)
print(p2.name, p2.age)

class Student:
    def __init__(self, name, course, id_no, school, country):
        self.name = name
        self.course = course
        self.id_no = id_no
        self.city = school
        self.country = country

s1 = Student("James", "BCOM", "HJG6899", "Univesity of Cape Town", "southafrica")
s2 = Student("Lonah", "BBIT", "6g87thj", "Kabianga", "Uganda")
s3 = Student("Mary", "Medicine", "ghy657", "Oxford", "Paris")

print(s1.name, s1.course, s1.id_no, s1.country)
print(s3.name, s3.course)