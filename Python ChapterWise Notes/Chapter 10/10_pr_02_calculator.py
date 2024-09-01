class Calculator:
    def __init__(self,num):
        self.num = num
    def square(self):
        print(f"Square of {self.num} is {self.num**2}")
    def cube(self):
        print(f"Cube of {self.num} is {self.num**3}")
    def SquareRoot(self):
        print(f"Squareroot of {self.num} is {self.num**0.5}")

a = Calculator(9)
a.square()
a.cube()
a.SquareRoot()
'''In Python, the ** operator is used for exponentiation, 
which means raising a number to a power. 
It is used to calculate the result of a number raised to the 
power of another number.'''

'''# Calculate 2 raised to the power of 3
result = 2 ** 3  # result will be 8

# Calculate 5 raised to the power of 2
result = 5 ** 2  # result will be 25
'''


