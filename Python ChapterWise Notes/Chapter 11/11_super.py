class Person:
    country = "India"
    def __init__(self):
        print("Person initializing")
    def breath(self):
        print("I am breathing....")
class Employee(Person):
    company = "Google"
    def __init__(self):
        super().__init__()
        print("Employee initializing")
    def breath(self):
        super().breath()
        print("I am an employee and I'm breathing....")
class Programmer(Employee):
    company = "Microsoft"
    def __init__(self):
        super().__init__()
        print("Employee initializing")
    def breath(self):
        super().breath() #Calls the breath() of the super class(Employee)
        print("I am a programmer an I'm breathing++")

p = Person()
p.breath()
e = Employee()
e.breath()
pr = Programmer()
pr.breath()
