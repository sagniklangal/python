def great(num1,num2,num3):
    if num1>num2:
        g1 = num1
    else:
        g1 = num2
    if g1>num3:
        greatest = g1
    else:
        greatest = num3
    return greatest
num1 = int(input("Enter your number 1\n"))
num2 = int(input("Enter your number 2\n"))
num3 = int(input("Enter your number 3\n"))
a = great(num1,num2,num3)
print("Greatest among three is: ",a)