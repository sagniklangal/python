letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''
name = input("Enter your name\n")
date = input("Enter date\n")

# #Wrong
# letter.replace("<|Name|>", name)
# letter.replace("<|Date|>", date)

#Correct
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)
print(letter)