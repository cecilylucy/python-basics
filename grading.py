score = int(input("Enter score :"))
# if statement
if score >= 90:
    print("A")
elif score >=80 and score <= 89:
    print("A-")
elif score >=70 and score <= 79:
    print("B")
elif score >=60 and score <= 69:
    print("B-")
elif score >=50 and score <= 59:
    print("C")
elif score >=40 and score <= 49:
    print("C-")
elif 30 <= score <= 39:
    print("D")
elif score >=30 and score <= 29:
    print("D-")

else:
    print("E")
