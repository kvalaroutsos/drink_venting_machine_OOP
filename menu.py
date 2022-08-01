from money_machine import MoneyMachine
currency=MoneyMachine()

class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, chocolate, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
            'chocolate':chocolate,
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=20, chocolate=0, cost=2.0),
            MenuItem(name="espresso", water=50, milk=0, coffee=15, chocolate=0,cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=20, chocolate=0,cost=2.2),
            MenuItem(name="chocolate", water=250, milk=50, coffee=0,chocolate=25, cost=2.5),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}-{item.cost}{currency.CURRENCY}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
