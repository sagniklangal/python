#Program is not working if "hiscore.txt" is empty
import random
randNumber = random.randint(1,100)
No_Of_Guesses = 0
userGuess = 0

while (userGuess != randNumber):
    userGuess = int(input("Enter your guess\n"))
    No_Of_Guesses+=1
    if userGuess == randNumber:
        print("You guessed it right")
    else:
        if userGuess<randNumber:
            print("Higher number please")
        elif userGuess>randNumber:
            print("Lower number please")

print(f"You have guessed the number in {No_Of_Guesses} guesses")

with open("hiscore.txt","r") as a:
    hiScore = a.read()
    if (No_Of_Guesses<int(hiScore)):
        print("You have just broken the high score")
with open("hiscore.txt","w") as a:
    a.write(str(No_Of_Guesses))


