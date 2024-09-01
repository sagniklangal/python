def great(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            return num1
        else:
            return num3
    else:
        if num2>num3:
            return num2
        else:
            return num3
num1 = int(input("Enter your number 1\n"))
num2 = int(input("Enter your number 2\n"))
num3 = int(input("Enter your number 3\n"))
a = great(num1,num2,num3)
print("Greatest among three is: "+str(a))