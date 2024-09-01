import os
oldfile = "name1.txt"
with open("name1.txt","r") as a:
    b = a.read()
with open("renamed_by_python.txt","w") as c:
    c.write(b)
os.remove(oldfile)
# Here the contents of the old file has been copied
# into new file and then old file has been removed