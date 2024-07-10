from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# allItmes=MenuItem()
menuitems=Menu()
coffeemaker=CoffeeMaker()
moneymachine=MoneyMachine()


play=True

while(play):
	orderedItem=input("What would you like? (espresso/latte/cappuccino/): ")
	if(orderedItem=='report'):
		coffeemaker.report()
		moneymachine.report()
	
	drink=menuitems.find_drink(orderedItem)
	coins=moneymachine.process_coins()

	if(moneymachine.make_payment(coins)):
		if(menuitems.find_drink(orderedItem)):
			if(coffeemaker.is_resource_sufficient(drink)):
				coffeemaker.make_coffee(drink)
				play=True

		











