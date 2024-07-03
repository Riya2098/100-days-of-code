from game_data import data
from highLowArt import logo, vs
import random

def generating_random_integers():
	random_index=random.randint(1,49)
	return random_index

def highLow(first_index, second_index):
	if(first_index!=second_index):
		name1= data[first_index]["name"]
		follower1=data[first_index]["follower_count"]
		occupation1 = data[first_index]["description"]
		country1= data[first_index]["country"]
		# print(f"Followers= {follower1}")
		print(f"Compare A: {name1}, a {occupation1}, from {country1}")
		print(vs)
		name2= data[second_index]["name"]
		follower2=data[second_index]["follower_count"]
		occupation2 = data[second_index]["description"]
		country2= data[second_index]["country"]
		# print(f"Followers= {follower2}")
		print(f"Against B: {name2}, a {occupation2}, from {country2}")
	else:
		highLow(first_index,second_index)


play_game=True
print(logo)
score=0
second_index=generating_random_integers()
while (play_game):
	first_index= second_index
	second_index=generating_random_integers()
	highLow(first_index,second_index)
	user_choice= input("Who has more followers? Type 'A' or 'B': ").lower()
	follower1=data[first_index]["follower_count"]
	follower2=data[second_index]["follower_count"]

	if(user_choice=='a' and follower1>follower2):
		print("Correct")
		score+=1
		print(f"Score is now: {score}")
	elif(user_choice=='b' and follower2>follower1):
		print("correct")
		score+=1
		print(f"Score is now: {score}")
	else:
		print(f"Sorry, that's wrong. Final score: {score}")
		play_game=False
