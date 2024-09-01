class Employee:
    company = "Microsoft"
    def salary(self):
        print("Salary is given")
    @staticmethod
    def greet(): # When we don't want to pass the self parameter @staticmethod is used
        print("Good Day")
sagnik = Employee()
sagnik.greet()
sagnik.salary()