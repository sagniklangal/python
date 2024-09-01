with open("log.txt","r") as a:
    b = a.read().lower() # For taking taking content as lower
if "python" in b:
    print("Python is present")
else:
    print("Python is not present")