class Person:
    country = "India"
    def __init__(self):
        print("Person initializing")
    def breath(self):
        print("I am breathing....")

class Employee(Person):
    company = "Google"
    def __init__(self):
        super().__init__() # Calling constructor of superclass Person
        print("Employee initializing")
    def breath(self):
        super().breath()
        print("I am an employee and I'm breathing....")

class Programmer(Employee):
    company = "Microsoft"
    def __init__(self):
        super().__init__() # Calling constructor of superclass Employee
        print("Employee initializing")
    def breath(self):
        super().breath()
        print("I am a programmer an I'm breathing++")

p = Programmer()
