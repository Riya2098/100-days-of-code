#Step 1 
import random
from hangman_words import word_list
from hangman_art import logo, stages

end_of_game=False
indice = random.randint(0,len(word_list))
chosen_word= word_list[indice]
# chosen_word = random.choice(word_list)

lives=6

#Testing code
print(logo)
print(f'Pssst, the solution is {chosen_word}.')

display=[]
for i in chosen_word:
	display+= '_'

while (end_of_game==False):
	guess= input("Guess the letter: ").lower()
	if guess in chosen_word:
		for i in range (len(chosen_word)):
			if(guess==display[i]):
				print(f"You have already guessed {guess}")
			elif(guess==chosen_word[i]):
				display[i]=guess
		#Join all the elements in the list and turn it into a String.
		print(f"{' '.join(display)}")
		print(stages[lives])
	if guess not in chosen_word:
		print(f"You guessed {guess}, that's not in the word, You lose a life")
		lives-=1
		print(f"{' '.join(display)}")
		print(stages[lives])

	if(lives==0):
		print("You Lost the Game, Try again!")
		break

	if '_' not in display:
		end_of_game=True
		print("Congratulations, You Won!")
















