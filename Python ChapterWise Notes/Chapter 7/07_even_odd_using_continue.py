print("For even printing") 
for i in range(10):
    if i%2 != 0:
        continue
    print(i)

print("For odd printing") 
for i in range(10):
    if i%2 == 0:
        continue
    print(i)