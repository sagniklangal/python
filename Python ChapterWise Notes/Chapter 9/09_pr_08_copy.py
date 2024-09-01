with open("this.txt","r") as a:
    b = a.read()
with open("this_copy.txt","w") as c:
    c.write(b)   