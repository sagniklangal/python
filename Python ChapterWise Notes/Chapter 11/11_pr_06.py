# class Vector:
#     def __init__(self,i,j,k):
#         self.i = i
#         self.j = j
#         self.k = k
#     def __str__(self):
#         return (f"{self.i}i+{self.j}j+{self.k}k")
# v = Vector(1,2,3)
# print(v)

# Alternative
class Vector:
    def __init__(self,vec):
        self.vec = vec
    def __str__(self):
        return f"{self.vec[0]}i +{self.vec[1]}j +{self.vec[2]}k"

v1 = Vector([1,2,3])
v2 = Vector([4,5,6])
print(v1)
print(v2)
