# Typecasting is must
num = int(input("Enter your number\n"))
for i in range(1,11):
    print(str(num) + " x " + str(i) + " = " + str(num*i))
    # print(f"{num}x{i}={num*i}") # Using f string