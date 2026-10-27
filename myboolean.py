# # Boolean>>In programming you often need to know id an expression is true or false
#
# Almost any value is evaluated to True if it has some sort of content.
#
# Any string is True, except empty strings.
#
# Any number is True, except 0.
#
# Any list, tuple, set, and dictiost, tuple, set, and dictionary are true except empty ones
print(10>9)
print(10==9)
print(10 < 9)

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
    # Evaluate a string and a number:
print(bool("Hello"))
print(bool(15))

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))

def myFunction():
    return True
print(myFunction())

def myFunction():
    return True

if myFunction():
    print("YES")
else:
    print("NO")
    # Check if a value is an integer

x = 200
print(isinstance(x, int))