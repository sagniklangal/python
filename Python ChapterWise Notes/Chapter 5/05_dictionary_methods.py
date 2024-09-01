dict = {
    "Sagnik":"He is a coder",
    "Langal": "It's his title",
    "Marks": [50,40,30],
    "dict1": {"Age": "His age is 22"},
    1:2
}

# # Prints the keys 
# print(dict.keys())
# print(type(dict.keys()))
# print(list(dict.keys()))

# # Prints the key values
# print(dict.values())
# print(type(dict.values()))
# print(list(dict.values()))
# print(tuple(dict.values()))

# #Prints the (key,item) of every element in the dictionary
# print(dict.items()) # Used for iteration purpose

# #Add more values into dictionary 
# dict1 = {
#     "Techno": "College",
#     "Sagnik": "He is a dancer" # Updates the previous value of key "Sagnik"
# }
# dict.update(dict1) # Updates the dict with new (key,data) pair from dict1
# print(dict)

# get() method
print(dict.get("Sagnik")) #Both works the same
print(dict["Sagnik"])
print(dict.get("Sagnik2")) # Prints none as "Sagnik2" is not present
# print(dict["Sagnik2"]) # Throws error as "Sagnik2" is not present

