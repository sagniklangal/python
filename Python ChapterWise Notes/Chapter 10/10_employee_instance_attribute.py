class Employee:
    company = "Microsoft" # Class attribute(Same for all objects)
    salary = 200
sagnik = Employee()
saikat = Employee()
print(sagnik.company)
print(saikat.company)

# Changing Class attribute(For all objects)
Employee.company = "Google"
print(sagnik.company)
print(saikat.company)

# Instance attribute
sagnik.salary = 300
saikat.salary = 500
print(sagnik.salary) #Instance attribute overrides class attribute 
print(saikat.salary) #salary is changed here