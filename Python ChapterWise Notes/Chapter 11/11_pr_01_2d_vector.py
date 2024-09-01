class c2dvector:
    def __init__(self,i,j):
        self.icap = i
        self.jcap = j
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"
class c3dvector(c2dvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        # #Alternative
        # self.icap = i
        # self.jcap = j
        self.kcap = k
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

c2d = c2dvector(2,3)
c3d = c3dvector(3,6,9)
print(c2d)
print(c3d)