
from artcalculator import logo

def add(n1, n2):
	return n1+n2

def subtract(n1,n2):
	if(n1>n2):
		return n1-n2
	else:
		return n2-n1

def multiply(n1,n2):
	return n1*n2

def divide(n1,n2):
	return n1/n2

operations={
"+":add,
"-":subtract,
"*":multiply,
"/":divide,
}


def calculator():
	print(logo)
	num1= float(input("What is the first number? :"))
	for symbol in operations:
		print(symbol)
	calc_continue=True
	while(calc_continue):
		operation_symbol= input("Pick another operation: ")
		num2=float(input("What's the next number?: "))
		calc_function = operations[operation_symbol]
		result= calc_function(num1, num2)
		print(f"{num1} {operation_symbol} {num2} = {result}")
		num1=result
		choice=input(f"Type 'y' to continue calculating with {num1} or type 'n' to exit and start new calculation: ")
		if(choice=='n'):
			calc_continue=False
			calculator()
	
calculator()
