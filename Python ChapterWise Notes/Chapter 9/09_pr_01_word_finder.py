a = open("poem.txt")
b = a.read()
if "twinkle" in b:
    print("twinkle is found")
else:
    print("twinkle is not found")