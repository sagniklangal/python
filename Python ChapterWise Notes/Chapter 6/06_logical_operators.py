# and,or,not
age = int(input("Enter your age\n"))
temp = int(input("Enter temp\n"))
sunny = True
a = None
if(age>=18 and age<70): # Not &
    print("You can drive a car")
else:
    print("You can't drive a car")

if(temp>=0 and temp<=30):
    print("Good temperature")
else:
    print("Bad temperature")

if(temp<=0 or temp>=30):
    print("Bad temperature")
else:
    print("Good temperature")

if sunny:
    print("Weather is sunny")
else:
    print("Weather is cloudy")

if not sunny:
    print("Weather is cloudy")
else:
    print("Weather is sunny")

if(a is None): # is keyword
    print("a is none")
else:
    print("a is not none")

b = [1,2,3,4,5]
print(1 in b) # in keyword
