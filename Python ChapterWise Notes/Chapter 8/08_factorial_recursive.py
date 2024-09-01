def factor(num):
    if num == 0 or num == 1:
        return 1
    return num*factor(num-1)

num = int(input("Enter your number\n"))
a = factor(num)
print(a)