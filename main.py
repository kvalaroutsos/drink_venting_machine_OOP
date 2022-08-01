from menu import Menu, MenuItem
from drink_maker import DrinkMaker
from money_machine import MoneyMachine


money_machine=MoneyMachine()
drink_maker=DrinkMaker()
menu=Menu()
is_on=True


money_machine.report()
drink_maker.report()

while is_on:
    options = menu.get_items()
    choice = input(f'What would you like to drink? ({options})')
    if choice =='off':
        is_on =False
    elif choice =='report':
        drink_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
        if drink_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                drink_maker.make_drink(drink)
