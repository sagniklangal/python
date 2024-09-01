with open("censor.txt") as a:
    b = a.read()
b = b.replace("donkey","####")
with open("censor.txt","w") as a:
    a.write(b)
