from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
menu_item = MenuItem
is_on = True


while is_on:
    drink = input(f"What would you like? {menu.get_items()} ").lower()
    if drink == "off":
        is_on = False
    elif drink == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(drink)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
