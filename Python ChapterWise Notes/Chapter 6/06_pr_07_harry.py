text = input("Enter your post\n")
list = [text]
if("Harry" in text):
    print("The post is talking about Harry")
elif("HARRY" in text):
    print("The post is talking about Harry")
elif("HarrY" in text):
    print("The post is talking about Harry")
else:
    print("The post is not talking about Harry")