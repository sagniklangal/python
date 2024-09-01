class Employee:
    company = "Google"
    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language  = "Python"
    company = "Youtube"
    def getLanguage(self):
        print(f"The language is {self.language}")
    def showDetails(self): # It will override the showDetails() of Employee class
        print("This is a programmer")

e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company) # overrides the company of parent class Employee