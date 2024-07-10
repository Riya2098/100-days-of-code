MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

play=True
money_collected=0

def coin_value(quarters, dimes, nickels, pennies):
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    total_value= (float(quarters)*0.25)+(float(dimes)*0.10)+(float(nickels)*0.05)+(float(pennies)*0.01)
    print(f"Total value is: {total_value}")
    return total_value


def availability(ordered_item):
    if(ordered_item=='espresso'):
        MENU[ordered_item]['ingredients']['milk']=0
    available=MENU[ordered_item]['ingredients']
    if available['water']>=resources['water']:
        print("Sorry there is not enough water")
        return False

    elif available['milk']>=resources['milk']:
        print("Sorry there is not enough milk")
        # play=False
        return False

    elif available['coffee']>=resources['coffee']:
        print("Sorry there is not enough coffee")
        # play=False
        return False
    return True

def ifTransactionSuccessful(ordered_item,quarters,dimes,nickels,pennies):
    global money_collected
    final_income=coin_value(quarters,dimes,nickels,pennies)
    available_cost=MENU[ordered_item]['cost']
    available_ingredients=MENU[ordered_item]['ingredients']
    # print("Hello")
    if(available_cost<=final_income):
        # we can give the coffee
        # print("Hello")
        resources['water']-=available_ingredients['water']
        resources['milk']-=available_ingredients['milk']
        resources['coffee']-=available_ingredients['coffee']
        money_collected+=available_cost
        providing_change(ordered_item,final_income)
        print(f"Here is your {ordered_item}. Enjoy!")
    else:
        print(final_income)
        print("Sorry that's not enough money. Money refunded.")
        return False
    return True

def providing_change(user_input,final_income):
    available_cost=MENU[user_input]['cost']
    change=0
    if(available_cost<final_income):
        change=final_income- available_cost
        print(f"Here is ${change} dollars in change.")

while(play):
    user_input= input("What would you like? (espresso/latte/cappuccino):")
    if user_input=='report':
        for i in resources:
            print(f"{i}: {resources[i]}")
        print(f"Money: {money_collected}")
    elif user_input=='off':
        print("Goodbye!")
        play = False
    else:
        value= availability(user_input)
        if(value):
            print("Please insert coins.")
            quarters = input("how many quarters?: ")
            dimes = input("how many dimes?: ")
            nickels = input("how many nickels?:")
            pennies = input("how many pennies?:")
            final_income = coin_value(quarters,dimes,nickels,pennies)
            if(ifTransactionSuccessful(user_input,quarters,dimes,nickels,pennies)==False):
                play=False
        else:
            play=False
            