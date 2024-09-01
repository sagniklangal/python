a = open("appendfile.txt","a") # a is append mode
b = a.write("This line has been appended. \n") # \n is used to append in new line
print(b)
a.close()