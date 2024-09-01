# (a + ib) (c + id) = (ac - bd) + i(ad + bc).
class Complex:
    def __init__(self,real,im):
        self.real = real
        self.im = im
    def __add__(self,c):
        return Complex(self.real + c.real, self.im + c.im)
    def __mul__(self,c) :
          mulReal = ((self.real*c.real) - (self.im*c.im))
          mulImg = ((self.real*c.im) + (self.im*c.real))
          return Complex(mulReal,mulImg)
    def __str__(self):
        if self.im<0:
            return f"{self.real} - {-self.im}i"
        else:
            return f"{self.real} + {self.im}i"

c1 = Complex(3,2)
c2 = Complex(1,7)
print(c1+c2)
print(c1*c2)