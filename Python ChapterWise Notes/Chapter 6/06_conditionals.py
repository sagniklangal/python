# Typecasting is must here
a = 8

# If-elif-elif-else ladder
if(a>3):
    print("a is greater than 3")
elif(a>5):
    print("a is greater than 5")
elif(a>7):
    print("a is greater than 7")
elif(a<10):
    print("a is less than 10")
else:
    print("No condition is true")
# In if-elif-else ladder, only the first true condition will get executed
# That's why 2nd,3rd and 4th elif didn't get executed
if(a>3):
    print("a is greater than 3")
if(a>5):
    print("a is greater than 5")
if(a>7):
    print("a is greater than 7")
if(a>10):
    print("a is less than 10")
else:
    print("a is not grater than 10")
# Here all the if are autonomous
# The else is connected with only the last if