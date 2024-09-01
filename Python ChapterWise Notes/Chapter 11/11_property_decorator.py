class Employee:
    company = "Bharat gas"
    salary = 5000
    bonus = 500

    @property
    def totalSalary(self): # Here totalSalary is a property, not a method
        return self.salary + self.bonus
    
    @totalSalary.setter # Here we are setting the value of totalSalary
    def TotalSalary(self,val): # The method name can be anything(ex : TotalSalary, totalSalary)
        self.bonus = val - self.salary
    

e = Employee()
print(f"Total Salary before changing is {e.TotalSalary}")
print(f"Bonus before changing is {e.bonus}")
e.TotalSalary = 6000
print(f"Total Salary after changing is {e.TotalSalary}")
print(f"Bonus after changing is {e.bonus}")