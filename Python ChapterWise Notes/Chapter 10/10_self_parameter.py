class Employee:
    company = "Microsoft"
    def show(self):
        print(self.name)
sagnik = Employee()
sagnik.name = "Sagnik"
sagnik.show() # sagnik.show() is executed as Employee.show(sagnik)
Employee.show(sagnik)