from artbid import logo

the_list=[]

def bidding_game(theName, initialAmount):
	vague_list={}
	vague_list["Name"]=theName
	vague_list["Amount"]=initialAmount

	the_list.append(vague_list)

def highest_bidder():
	highest=0
	finalname=""
	for i in range(len(the_list)):
		price= the_list[i]['Amount']
		name=the_list[i]['Name']
		if(highest<price):
			highest=price
			finalname=name
	print(f"The winner is {finalname} with a bid of ${highest}")

game_restart=True
print(logo)
while(game_restart):
	print("Welcome to the secret auction program. ")
	name= input("What is your name?: ")
	bid_amount=int(input("What's your bid?: $"))
	bidding_game(name, bid_amount)
	restart= input("Are there any other bidders? Type 'yes' or 'no': ")
	if(restart=='no'):
		highest_bidder()
		game_restart=False