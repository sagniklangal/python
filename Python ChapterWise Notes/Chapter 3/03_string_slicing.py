#Using concatenation of two strings
a = "Good morning, "
b = "Sagnik"
print(a+b)

# Printing particular character of a string
print(a[0])
print(b[0])
print(a[3])
# a[0] = 's' #Not possible

#Slicing
print(b[0:6])   #b[0:6] 0 = including, 6 = excluding
print(b[0:])    #Automatically goes upto last index
print(b[:6])    #Automatically starts from first(0 th) index
print(b[-6:0])  #Same as b[0:6]

#Slicing with skip value
print(b[0:6:2]) #It will skip every 2nd character
print(b[0::2])  #same as the upper. Automatically goes upto last index. 

