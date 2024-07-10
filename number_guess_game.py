import random
from logoGuessgame import logo
answer= random.randint(1,100)
play=True

def decision():
	global answer
	global play
	if(difficulty=='easy'):
		attempts=10
	else:
		attempts=5
	print(f"You have {attempts} attempts remaining to guess the number.")
	while(attempts>0 and play==True):
		number= int(input("Make a guess: "))
		if(number<answer):
			attempts-=1
			if(attempts>=1):
				print("Too low")
				print("Guess again!")
				print(f"You have {attempts} attempts remaining to guess the number.")
		elif (number>answer):
			attempts-=1
			if(attempts>=1):
				print("Too high")
				print("Guess again!")
				print(f"You have {attempts} attempts remaining to guess the number.")
		elif(number==answer):
			print("Correct answer!")
			play=False
	if(attempts==0):
		print("You've run out of guesses, you lose.")
		print(f"The number was {answer}")

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
# print(f"Pssst, the correct answer is {answer}")

difficulty= input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if(difficulty=='easy'):
	decision()
elif(difficulty=='hard'):
	decision()
else:
	print("Invalid input!")
