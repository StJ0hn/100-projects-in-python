from math import trunc
from random import randint

#Create a list with options
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
___________
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = [rock, paper, scissors]
options_random = options[randint(0,2)]

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_choice = int(input())
#print choices
print(options[user_choice])
print("Computer chose:\n")
print(options_random)

#draw
if user_choice == options.index(options_random):
    print("Draw")
#User Win
elif (user_choice == 0 and options_random == options[2]) or \
(user_choice == 1 and options_random == options[0]) or \
(user_choice == 2 and options_random == options[0]):
    print("You win")
#Computer win
else:
    print("You lose")
