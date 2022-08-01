class DrinkMaker:
    """Models the machine that makes the drinks"""
    def __init__(self):
        self.resources = {
            "water": 2000,
            "milk": 400,
            "coffee": 400,
            "chocolate":300,
        }

    def report(self):
        """Prints a report of all current resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Chocolate: {self.resources['chocolate']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_drink(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} . Enjoy!")
