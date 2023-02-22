from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
from menu import Menu


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


while True:
    print(menu.get_item())
    choice = input("What woud you like?.\n")

    if choice == 'exit':
        break
    elif choice == 'report':
        money_machine.report()
        coffee_maker.report()
    
    elif choice not in [item.name for item in menu.menu]:
        continue
    else:
        coffee = menu.find_order(choice)
        if coffee_maker.is_resource_sufficient(coffee) and\
            money_machine.make_payment(coffee.cost):
            
            coffee_maker.make_coffee(coffee)


