fact = int(input("Enter the number\n"))
for i in range(1,fact):
    fact = fact*i
    i = i + 1
print(fact)