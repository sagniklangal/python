text = "My name is  Sagnik"
print(text)
text = text.replace("  "," ")
print(text)

text1 = "My name is    Tarju"
print(text1)
text1 = text1.replace("  "," ")
print(text1) #Here the two consecutive double spaces will be replaced by single spaces
#So there will be one double space left. It will be done properly in loops