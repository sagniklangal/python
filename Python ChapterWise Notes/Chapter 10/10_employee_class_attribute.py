class Employee:
    company = "Microsoft" # Class attribute(Same for all objects)
Sagnik = Employee()
Saikat = Employee()
print(Sagnik.company)
print(Saikat.company)

# Changing Class attribute(For all objects)
Employee.company = "Google"
print(Sagnik.company)
print(Saikat.company)