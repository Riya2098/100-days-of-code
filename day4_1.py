rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random

game_choice=[rock, paper, scissors]

user_choice= int(input("What's your choice? Type '0' for rock, '1' for paper and '2' for scissors \n"))
computer_choice= random.randint(0,2)
print(f"Computer chose: {computer_choice}")
print(game_choice[computer_choice])

print(f"User chose: {user_choice}")
print(game_choice[user_choice])

if(user_choice>=3 or user_choice<0):
    print("Invalid inout, You lost!")
else: 
    if(user_choice==0 and computer_choice==2):
        print("You won")

    elif(user_choice==0 and computer_choice==1):
        print("You lost!")
    elif(user_choice==1 and computer_choice==2):
        print("You lost")
    elif(user_choice==2 and computer_choice==0):
        print("You won")
    elif(user_choice>computer_choice):
        print("You won")
    elif(user_choice==computer_choice):
        print("It's a draw")
    else:
        print("Mistake hai kuch!")






















