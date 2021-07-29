from replit import clear


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
    "money": 0,
}


def ask_drink():
    answer = input("What would you like? (espresso/latte/cappuccino) or 'Off'/'report': ").lower()
    return answer


def off():
    return print("Goodbye!")


def report(resources_request):
    water = resources_request.get("water")
    milk = resources_request.get("milk")
    coffee = resources_request.get("coffee")
    money = resources_request.get("money", 0)
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


def check_resources(resources_request, drink):
    drink = drink.get("ingredients")
    for item in drink:
        if resources_request[item] >= drink[item]:
            return True
        else:
            print("Sorry there is not enough coffee.")
            a = input("Do you want add components? y/n ").lower()
            if a == "y":
                add_component(all_resources=resources)


def process_coins():
    money = 0
    quarters = int(input("How many quarters 0.25$?: "))
    money += quarters * 0.25
    print(money)
    dimes = int(input("How many dimes 0.1$?: "))
    money += dimes * 0.10
    print(money)
    nickles = int(input("How many nickles 0.05$?: "))
    money += nickles * 0.05
    print(money)
    pennies = int(input("How many pennies 0.01$?: "))
    money += pennies * 0.01
    print(money)
    return money


def check_transaction(pay, drink):
    if pay > drink.get("cost"):
        change = pay - drink.get("cost")
        change = round(change, 2)
        print(f"Here your change {change}$")
        return True
    elif pay == drink.get("cost"):
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink, all_resources):
    drink_ing = drink.get("ingredients")
    for item in drink_ing:
        all_resources[item] -= drink_ing[item]
    all_resources["money"] += drink["cost"]


def add_component(all_resources):
    component = input("What component add? water(ml)/milk(ml)/coffee(g) ").lower()
    points = int(input("How many? "))
    if component == "water":
        all_resources["water"] += points
    elif component == "milk":
        all_resources["milk"] += points
    elif component == "coffee":
        all_resources["coffee"] += points
    else:
        print("Incorrect answer")


def coffee_machine():
    running = True
    while running:
        drink = ask_drink()
        str_drink = drink
        if drink == "espresso" or drink == "latte" or drink == "cappuccino":
            drink = MENU.get(drink)
            if check_resources(resources_request=resources, drink=drink):
                print(f"{drink['cost']}$ for {str_drink}")
                money = process_coins()
                if check_transaction(pay=money, drink=drink):
                    make_coffee(drink=drink, all_resources=resources)
                    print(f"“Here is your {str_drink}. Enjoy!")
                else:
                    print()
            else:
                print()
        elif drink == "off":
            off()
            running = False
        elif drink == "report":
            report(resources_request=resources)


coffee_machine()
