class Vector:
    def __init__(self,vec):
        self.vec = vec
    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1+= f" {i}a{index} +"
            index+=1
        return str1[:-1]
    def __add__(self,vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)
    def __mul__(self,vec2): # For dot product
        dot_product = 0
        for i in range(len(self.vec)):
            dot_product+=self.vec[i]*vec2.vec[i]
        return dot_product
            
v1 = Vector([1,4,5])
v2 = Vector([1,6,5])
print(v1)
print(v2)
print(v1+v2)
print(v1*v2)

'''This code defines a Python class called `Vector`, which represents mathematical vectors in a two-dimensional space. The `Vector` class is equipped with a constructor, a string representation method, and an addition method. Here's a breakdown of the code and its functionality:

1. **Class Definition**:
   ```python
   class Vector:
   ```
   This line defines the `Vector` class, which is designed to represent mathematical vectors.

2. **Constructor (`__init__` method)**:
   ```python
   def __init__(self, vec):
       self.vec = vec
   ```
   The `__init__` method is the constructor for the `Vector` class. It takes two parameters: `self` (referring to the instance being created) and `vec`, which is a list representing the vector. The constructor initializes the `vec` attribute of the `Vector` object with the provided list.

3. **String Representation (`__str__` method)**:
   ```python
   def __str__(self):
       str1 = ""
       index = 0
       for i in self.vec:
           str1 += f" {i}a{index} +"
           index += 1
       return str1[:-1]
   ```
   The `__str__` method defines how a `Vector` object should be represented as a string when it is converted to a string (e.g., when you print it). It constructs a string that represents the vector's components with their respective indices.

4. **Addition Method (`__add__` method)**:
   ```python
   def __add__(self, vec2):
       newList = []
       for i in range(len(self.vec)):
           newList.append(self.vec[i] + vec2.vec[i])
       return Vector(newList)
   ```
   The `__add__` method allows you to perform vector addition. When you use the `+` operator between two `Vector` objects, this method is called. It takes two parameters: `self` and `vec2`, where `self` represents the first vector, and `vec2` represents the second vector. It returns a new `Vector` object representing the result of adding the two vectors element-wise. It does this by creating a new list (`newList`) where each element is the sum of the corresponding elements from `self.vec` and `vec2.vec`.

5. **Creating `Vector` Objects**:
   ```python
   v1 = Vector([1, 4, 5])
   v2 = Vector([1, 6, 5])
   ```
   Two `Vector` objects, `v1` and `v2`, are created, each initialized with a list of numeric values representing vectors.

6. **Printing `v1` and `v2**:
   ```python
   print(v1)
   print(v2)
   ```
   The `print` statements display the string representations of `v1` and `v2` by calling their respective `__str__` methods. This representation shows the vector components with their indices.

7. **Vector Addition**:
   ```python
   print(v1 + v2)
   ```
   This line demonstrates vector addition by adding `v1` and `v2` using the `+` operator. The `__add__` method is called, and the result is printed. It creates a new `Vector` object that represents the result of adding the two vectors `[1, 4, 5]` and `[1, 6, 5]` element-wise. The result is `[2, 10, 10]`, and you will see it printed.'''
