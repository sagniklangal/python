def factor(num):
    for i in range(1,num):
        num = num*i
    return num
num = int(input("Enter your number\n"))
a = factor(num)
print(a)