words = ["mote","donkey","gadha"]
with open("censor.txt") as a:
    b = a.read()
for word in words:
    b = b.replace(word,"####")
with open("censor.txt","w") as a:
    a.write(b)
