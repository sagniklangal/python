# For writing
# with open("withfile.txt","w") as a:
#     b = a.write("This is the with file")

'''No need to close the file manually(a.close())
If we use "with", file closing is done manually'''

# For reading
with open("new.txt","r") as a:
    b = a.read()
print(b)