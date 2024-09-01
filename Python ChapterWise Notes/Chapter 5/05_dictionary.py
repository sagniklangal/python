# "" and '' doesn't matter
dict = {
    "Sagnik":"He is a coder",
    "Langal": "It's his title",
    "Marks": [50,40,30],
    "dict1": {"Age": "His age is 22"}
}
print(dict["Sagnik"])
dict["Marks"] = [34,29,61] # Dictionaries are mutable
print(dict["Marks"]) 
print(dict["Langal"])
print(dict["dict1"]["Age"])
