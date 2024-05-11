from Menu import Menu
from CoffeeMaker import CoffeeMaker
from MoneyMachine import MoneyMachine


menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

while 1:
    user_choice = input(f"What would you like? ({menu.get_items()}): ").lower()

    if user_choice == 'off':
        break
    elif user_choice == 'report':
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        if drink != None:
            if coffee_machine.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_machine.make_coffee(drink)

