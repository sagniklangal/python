# Faulty, not done yet
import random
def game(comp,you):
    id = False
    if comp == you:
        return None
    elif comp == 'snake':
        if you == 'water':
            return id
        elif you == 'gun':
            id = True
            return id
    elif comp == 'water':
        if you == 'snake':
            id = True
            return id
        elif you == 'gun':
            return id
    elif comp == 'gun':
        if you == 'snake':
            return id
        elif you == 'water':
            id = True
            return id

print("Computer's turn")
comp = random.randint(1,3)
if comp ==1:
    comp='snake'
elif comp ==2:
    comp='water'
else:
    comp='gun'

you = input("Your turn: Snake(1) Water(2), Gun(3)\n")
print("Computer has chosen",comp)
a = game(comp,you)
if a==True:
    print("You win")
elif a == False:
    print("Computer wins")
else:
    print("Tie")