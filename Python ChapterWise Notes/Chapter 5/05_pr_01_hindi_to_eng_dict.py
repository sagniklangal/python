dict = {
    "ladka":"Boy",
    "ladki":"Girl",
    "pedh":"Tree",
    "ghar":"Boy",
    "gaon":"Village",
    "din":"Day"
}
print("Options are: ",dict.keys())
key = input("Enter the hindi word: ")

# # Throws an error if wrong key is given
# print("The english translation is: ",dict[key])

# Doesn't throw an error if wrong key is given
print("The english translation is: ",dict.get(key)) #Better