class Customer:
    def __init__(self, names: str, email: str, kra: str, dob: str, gender: str):
        self.names = names
        self.email = email
        self.kra = kra
        self.dob = dob
        self.gender = gender

    def show_details(self):
        print(f"Name: {self.names} and KRA PIN: {self.kra}")

    def __str__(self):
        return f"Name: {self.names} and KRA PIN: {self.kra}"


class Account:
    def __init__(self, owner: Customer, acc_no: str, acc_type: str, balance: float):
        self.owner = owner
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.balance = float(balance)

    def print_details(self):
        print(f"Owner: {self.owner.names}")
        print(f"Account No: {self.acc_no}")
        print(f"Type: {self.acc_type}")
        print(f"Balance: {self.balance}")
        print("**************")

    def deposit(self, amount: float):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def __str__(self):
        return f"Account {self.acc_no} for {self.owner.names}"


# Example Usage
owner1 = Customer("Jim Jong", "hj@gmail.com", "hj79", "23/6/2010", "M")
owner2 = Customer("Morris", "liam@gmail.com", "yj89h9", "19/7/2019", "F")

acc1 = Account(owner1, "87899976542", "current", 78000)
acc2 = Account(owner1, "67856452", "savings", 6780000)
acc3 = Account(owner2, "89095976542", "savings", 100000)

acc1.print_details()
acc1.deposit(9000)
acc1.print_details()
acc1.withdraw(1000)
acc1.print_details()