num1 = input("Enter the number 1\n")
num2 = input("Enter the number 2\n")
num3 = input("Enter the number 3\n")
num4 = input("Enter the number 4\n")

if(num1>num2):
    f1 = num1
else:
    f1 = num2

if(num3>num4):
    f2 = num3
else:
    f2 = num4

if(f1>f2):
    print(f1, "is greatest")
else:
    print(f2, "is greatest")
