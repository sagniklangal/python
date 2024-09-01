class Person:
    country = "India"
    def breath(self):
        print("I am breathing....")
class Employee(Person):
    company = "Google"
    def breath(self):
        print("I am an employee and I'm breathing....")
class Programmer(Employee):
    company = "Microsoft"
    def breath(self):
        print("I am breathing++")

p = Person()
e = Employee()
pr = Programmer()
pr.breath()
print(pr.company)
print(pr.country)

