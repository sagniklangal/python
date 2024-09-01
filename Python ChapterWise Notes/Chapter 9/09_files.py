a = open('new.txt','r') # Open the file in "r" mode
# f = a.read() # Read it's contents and stores in a variable(Here f)
f = a.read(5) # Reading the first 5 characters
print(f) # print the contents
a.close() # Close the file