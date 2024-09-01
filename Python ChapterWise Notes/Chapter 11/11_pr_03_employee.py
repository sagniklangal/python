class Employee:
    salary = 30000
    increment = 3
    @property
    def salaryAfterIncrment(self):
        return self.salary*self.increment
    @salaryAfterIncrment.setter
    def totalSalary(self,val):
        self.increment = val/self.salary

e = Employee()
print(e.salaryAfterIncrment)
print(e.increment)
e.totalSalary = 50000
print(e.salaryAfterIncrment)
print(e.increment)
