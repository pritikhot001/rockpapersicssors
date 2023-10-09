import random
def game(Comp,You):
    if Comp == You :
        return None
    if Comp =='r':
        if You =='p':
            return False
        elif You =='s':
            return True
        elif Comp =='p':
            if You == 's':
                return False
            elif You =='r':
                return True
        elif Comp =='s':
            if You == 'r':
                return False
            elif You =='p':
                return True
            

print("Comp Turn : Rock(r) Paper(p) or Scissors(s)?")
randNO = random.randint(1,3)
#print(randNO)
if randNO == 1:
    Comp = 'r'
elif randNO == 2:
    Comp = 'p'
elif randNO == 3:
    Comp = 's'

You = input("Player's Turn : Rock(r) Paper(p) or Scissors(s)?")
a = game(Comp , You)
print(f"Computer chose {Comp}")
print(f" You chose {You}")
game(Comp, You)
if a == None:
    print("the game is a tie!")
elif a:
    print("YOU WIN !")
else:
    print("YOU LOSE!")
