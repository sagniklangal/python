class Employee:
    salary = 30000
    @classmethod 
    def change_salary(cls,money): # This classmethod is used to change the value of class
        cls.salary = money # classmethod always takes "cls" parameter

print(Employee.salary)
e = Employee()
e.change_salary(50000)
print(Employee.salary)
