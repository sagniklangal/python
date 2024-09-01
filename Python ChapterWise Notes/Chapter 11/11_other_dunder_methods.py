class Number:
    def __init__(self,num):
        self.num = num
    def __str__(self):
        return f"Decimal number {self.num}"
    def __len__(self):
        return 1

n = Number(9)
print(n)
print(f"The length is {len(n)}")

'''def __str__(self):: This is another special method in Python called a 
"magic method" or "dunder method." It's defined with the double underscore (__) 
before and after the method name. In this case, it's the "__str__" method, which 
is used to define a human-readable string representation of the object. This method 
is automatically called when you use the str() function or when you try to convert 
an instance of the Number class to a string, for example, when printing it.'''