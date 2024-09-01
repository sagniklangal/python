with open("this.txt","r") as a:
    b = a.read()
with open("this_copy.txt","r") as c:
    d = c.read()
if b == d:
    print("The files are identical")
else:
    print("The files are not identical")