num = int(input("Enter your number\n"))
prime = True
for item in range(2,num):
    if (num%item == 0):
        prime = False
        break
if prime:
    print("The number is a prime number")
else:
    print("Not a prime number")
