
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n$ "))

#we got the value, now we need to ask for a tip
tip=int(input("How much tip would you like to give? 10, 12, or 15? \n$ "))

roundtip= round(tip/100,2)
roundtip+=1

finalbill=bill*roundtip

people=int(input("How many people to split the bill? \n"))
finalbill=round(finalbill/people,2)

print(f"Each person should pay: ${finalbill}")

