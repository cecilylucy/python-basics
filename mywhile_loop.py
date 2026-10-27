# while loop
i=1
while i< 6:
    print(i)
    i += 1

# break statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#   continue statement
i = 0
while i < 6:
    i+=1
    if i == 3:
        continue
    print(i)

#the else statement
i = 3
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

#     For Loops: Used for iterating over a sequences(That is either a list, a tuple, a dictionary, a set, or a string

fruits = ["apple", "banana", "cherry" ]
for x in fruits:
    print(x)
# Looping through a string
for x in "bananas":
    print(x)
#     The break statement >>>   Stops the loop before it has looped through
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

fruits = ["apple", ]

# continue statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# range function
for x in range(6):
    print(x)
#     range  parameter
for x in range(2, 6):
    print(x)
#    range increment
for x in range(2, 20, 3):
    print(x)

#     Else in for loop>>>specifies a block of code to be executed when the loop is finished
for x in range(6):
    print(x)
else:
    print("Finally finished!")


for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")

    # Nested loop >>.The inner loop will be executed one time for each iteration for the outer loop

adj = ["red", "big", "tasty"]
fruits=["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
        # The pass statement>>>for loops cannot be empty, but if you for some reason have a for
        # for loop with no content, put in the pass statement to avoid getting an error.

for x in [0, 1, 2]:
    pass