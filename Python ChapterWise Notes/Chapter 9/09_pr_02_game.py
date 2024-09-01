def game():
    return 36
newscore = game()
with open("hiscore.txt") as a:
    score = a.read()
if score == "":
    with open("hiscore.txt","w") as b:
        b.write(str(newscore)) # In text file everything goes as characters 
                                # So we have to typecats into str
elif int(score)<newscore:
    with open("hiscore.txt","w") as b:
        b.write(str(newscore))

