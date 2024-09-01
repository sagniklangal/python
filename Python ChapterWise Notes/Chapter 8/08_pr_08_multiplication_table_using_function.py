def table(n):
    for i in range(1,11):
        print(str(n)+" x "+str(i)+" = "+str(n*i))
num = int(input("Enter your number\n"))
table(num)