def sum(num):
    if num == 1:
        return 1
    num = num + sum(num-1)
    return num
num1 = int(input("Enter your number 1\n"))
a = sum(num1)
print("The sum of "+str(num1)+" natural numbers is "+str(a))