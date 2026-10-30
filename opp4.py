# Inheritance

# employees --name, id, department, gender
# salaried -- + salary, tenure
# casuals -- rates

class Employee:
    def __init__(self, name:str, id_no:str,department:str, gender:str, ): #constructor
        self.full_name = name
        self.identity_no = id_no
        self.department = department
        self.gender = gender

    def print_details(self):
        print(self.full_name)
        print(self.identity_no)
        print(self.department)
        print(self.gender)
        print("***************************")

class SalariedEmployee(Employee):
    def __init__(self, name: str, id_no: str, department: str, gender: str,salary:int, tenure:int ):
        super().__init__(name, id_no, department, gender) #call the function,,,its like go to your parent
        self.tenure = tenure
        self.salary = salary

class CasualWorker(Employee):
    def __init__(self, name:str, id_no:str,department:str, gender:str,rate:float ):
        super().__init__(name, id_no, department, gender)
        self.rate = rate
    def calc_wage(self, hours: float):
        return hours * self.rate

s1 = SalariedEmployee("Joseph Jah", "4467888", "HR", "F", 8789, 87)
c1 = CasualWorker("Collins Nde", "676789", "Sales", "F", 546.0)
s1.print_details()
c1.print_details()
print(c1.calc_wage(19))
