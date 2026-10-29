def add(x, y, z):
    return x + y + z

# res = add(1, 2, 3) #args/params
# print(res)
def addition(*nums):
    total = sum(nums)
    return total

# key and word arguments **kwargs
def save(**data):
    with open("values.txt", "w") as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")


def some_function(name, *scores, **details):
    pass

def cylinder(r  , h):
    """
    calculates the volume and SA of a cylinder
    parameters:
    radius and height of the cylinder
    :returns: volume and surface Area of the cylinder
    :param r:
    :param h:
    :return:
    """
    v = 22/7 * r*r*h
    sa = 22/7 *r **2 *2 + 22/7 * r *2 *h
    return sa, v

surf_area, volume = cylinder(7, 15)
print(surf_area, volume)
sum([1, 2, 3])

some_function("Hellen", 10, 90, 85, gender= "Female", course="Chem")

# save(age = 18, dob='2001-2-3', profession = 'Enginner')
save(dob='2025-01-18', gender='female', color='black', profesion='Doctor')


# print(addition(9,10,45,67,78,12,90,78))
# print(addition(90 , 100))
data = {"name":"ken", "gender": "Male"}
for item in data.items():
    print(item)

# lamba functions >>>anonymous functions.
divider= lambda x, y: x/y

area_circle =lambda r: 22/7 * r *r

print(divider(45, 7))
res = area_circle



