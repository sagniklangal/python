def remove(string,word):
    new_str = string.replace(word,"")
    return new_str.strip()
string = "  Sagnik is a good boy  "
a = remove(string,"Sagnik")
print(a)
# In Python, the strip() method is used to remove 
# specified characters (whitespace characters by default) 
# from the beginning and end of a string. It's a common 
# operation for cleaning up user input or processing 
# text data.