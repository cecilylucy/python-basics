 # Opp means object oriented programming
 # properties + functions
 # class # template

 # book title. author, isbn, price
 class Book:
      # constructor == function
    def __init__(self, title, author, isbn, price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
    def print_details(self):
        print("Title", self.title)
        print("Author", self.author)
        print("Price", self.price)
        print("-------------")
    def apply_discount(self, discount):
        self.price= self.price * (1- discount/100)
        print("New price is", self.price)

b1 = Book("River between", "Ngugi Wa Thiongo", "GH678", 400)
b2 = Book("The Alpha", "Josphine", "RT657", 250)

b1.print_details()
b1.apply_discount(10)
b1.print_details()
print(b2.price)



