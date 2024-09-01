comment = input("Enter your text\n")
flag = False
if("make a lot of money" in comment):
    flag = True
elif("buy now" in comment):
    flag = True
elif("subscribe this" in comment): # yo bro, subscribe this -->spam
    flag = True
elif("click this" in comment): # hey you, click this -->spam
    flag = True

if(flag is True):
    print("Spam")
else:
    print("Not spam")