# This program is of game Rock, Paper or Sissor

import random

def gamewin(comp, you):
    if comp == you :
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False
    elif comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False

print("Comp Turn: Rock(r) Paper(p) or Sissor(s)")
randno = random.randint(1,3)
if randno == 1:
    comp = 'r'
elif randno == 2:
    comp = 'p'
elif randno == 3:
    comp = 's'

you = input("Your Turn: Rock(p) Paper(p) or Sissor(s):")
a = gamewin(comp, you)

print(f"computer chose {comp}")
print(f"Your chose {you}")

if a == None:
    print("Your game is a Tie!")
elif a :
    print("You Win!")
else:
    print("You Lose!")

# Below program ia for snake, water or gun
# import random 

# def gameWin(comp, you):
#     if comp == you: 
#         return None
#     elif comp == 's':
#         if you== 'w':
#             return False
#         elif you== 'g':
#             return True
#     elif comp == 'w':
#         if you== 'g':
#             return False
#         elif you== 's':
#             return True
#     elif comp == 'g':
#         if you== 's':
#             return False
#         elif you== 'w':
#             return True

# print("Comp Turn: Snake(s) water(w) or Gun(g)?")
# randNo = random.randint(1, 3)
# if randNo == 1:
#     comp = 's'
# elif randNo == 2:
#     comp = 'w'
# elif randNo ==3:
#     comp = 'g'

# you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
# a = gameWin(comp, you)

# print(f"Computer chose {comp}")
# print(f"You chose {you}")

# if a == None:
#     print("The game is a tie!")
# elif a:
#     print("You Win!")
# else:
#     print("You Lose!")

#include<stdio.h>
#include<stdlib.h>
#include<time.h>


