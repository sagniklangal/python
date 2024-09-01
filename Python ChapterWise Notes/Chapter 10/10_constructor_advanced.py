class Employee:
    company = "Microsoft"
    def __init__(self,name,salary): # __init__ is used to define constructor
        print("Object is created")
        self.name = name
        self.salary = salary
        print(f"Employee name is {self.name} and salary is {self.salary}")

sagnik = Employee("Sagnik",50000)