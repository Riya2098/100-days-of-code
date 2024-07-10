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

#Write your code below this line 👇

import random

computer_choice= random.randint(0,2)
user_choice=int(input("What's your choice? Type '0' for rock, '1' for paper and '2' for scissors \n"))


print(computer_choice)
print(user_choice)

if(computer_choice==0):
    if(user_choice==0):
        print("User's choice is rock")
        print(rock)
        print("Computer's choice is rock")
        print(rock)
        print("It's a draw")
    elif(user_choice==1):
        print("User's choice is paper")
        print(paper)
        print("Computer's choice is rock")
        print(rock)
        print("You Won :)")
    elif(user_choice==2):
        print("User's choice is scissors")
        print(scissors)
        print("Computer's choice is rock")
        print(rock)
        print("You Lost :(")
    else:
        print("Choice invalid")

elif(computer_choice==1):
    if(user_choice==0):
        print("User's choice is rock")
        print(rock)
        print("Computer's choice is paper")
        print(paper)
        print("You Lost :(")
    elif(user_choice==1):
        print("User's choice is paper")
        print(paper)
        print("Computer's choice is paper")
        print(paper)
    elif(user_choice==2):
        print("User's choice is scissors")
        print(scissors)
        print("Computer's choice is paper")
        print(paper)
        print("You Won :)")
    else:
        print("Choice invalid")
elif(computer_choice==2):
    if(user_choice==0):
        print("User's choice is rock")
        print(rock)
        print("Computer's choice is scissors")
        print(scissors)
        print("You Won :)")
    elif(user_choice==1):
        print("User's choice is paper")
        print(paper)
        print("Computer's choice is scissors")
        print(scissors)
        print("You lost :(")
    elif(user_choice==2):
        print("User's choice is scissors")
        print(scissors)
        print("Computer's choice is scissors")
        print(paper)
        print("It's a draw")
    else:
        print("Choice invalid")
else:
    print("Invalid input, please choose the correct number")













