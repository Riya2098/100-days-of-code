import random
from artBlackJack import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards=[]
computer_cards=[]

def compsum():
	compcardsum=0
	for i in range(len(computer_cards)):
		compcardsum+=computer_cards[i]
	return compcardsum

def usersum():
	usercardsum=0;
	for i in range(len(user_cards)):
		usercardsum+=user_cards[i]
	return usercardsum

def userBlackjack():
	card= random.choice(cards)
	user_sum=0
	if(card==11 and user_sum>21):
		card=1
		user_cards.append(card)
	else:
		user_cards.append(card)
	for i in range(len(user_cards)):
		user_sum+=user_cards[i]
	return user_sum

def computerBlackjack():
	computer_first_card= random.choice(cards)
	computer_sum=0
	computer_cards.append(computer_first_card)
	for j in range(len(computer_cards)):
		computer_sum+=computer_cards[j]
	return computer_sum

def decision():
	computer_sum=compsum()
	user_sum=usersum()
	print(f"Your cards: {user_cards}, Your score: {user_sum}")
	print(f"Computer's final cards are: {computer_cards}, Computer's score: {computer_sum}")

	if(user_sum==21 and computer_sum==21):
		print("Computer wins, as it got a blackjack before you")
	elif(user_sum>21):
		print("You went over. You lose 😭")
	elif(computer_sum>21):
		print("Opponent went over. You win 😁")		
	elif user_sum<=21 and user_sum>computer_sum:
		print("You win 😃")
	elif(computer_sum<=21 and computer_sum>user_sum):
		print("You lose 😤")
	elif(computer_sum==user_sum):
		print("Draw")
	else:
		print("Check kar")
	
def anotherBetUser():
	user_choice=input("Type 'y' to get another card, type 'n' to pass: ")
	if(user_choice=='y'):
		# We get another card for the user
		user_sum=userBlackjack()
		if(user_sum>21):
			decision()
		else:
			print(f"Your cards: {user_cards}, current score: {user_sum}")
			print(f"Computer's first card is: {computer_cards[0]}")
			anotherBetUser()
	else:
		anotherBetComputer()

def anotherBetComputer():
		computer_sum=compsum()
		if(computer_sum<16):
			computerBlackjack()
		decision()

def play():
		# My cards and my initial score
		userBlackjack()
		userBlackjack()
		sumofuser=usersum()
		print(f"Your cards: {user_cards}, current score: {sumofuser}")

		# Computer's card
		computerBlackjack()
		computerBlackjack()
		computersum=compsum()

		print(f"Computer's first card is: {computer_cards[0]}")
		anotherBetUser()

playGame=True
while (playGame):
	print(logo)
	start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
	if(start=='y'):
		play()
		user_cards=[]
		computer_cards=[]
		user_sum=0
		computer_sum=0
	else:
		print("Byeee!")
		playGame=False


