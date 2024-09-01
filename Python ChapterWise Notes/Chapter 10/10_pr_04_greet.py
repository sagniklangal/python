class Calculator:
    def __init__(self,num):
        self.num = num
    def square(self):
        print(f"Square of {self.num} is {self.num**2}")
    def cube(self):
        print(f"Cube of {self.num} is {self.num**3}")
    def SquareRoot(self):
        print(f"Squareroot of {self.num} is {self.num**0.5}")
    @staticmethod
    def greet():
        print("Welcome to the calculator")

a = Calculator(9)
a.greet()
a.square()
a.cube()
a.SquareRoot()