from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Generation objects of every class

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

flag = True
while flag:
    choice = input("What would you like? (espresso/latte/cappucino): ")
    if choice == "off":
        flag = False
    elif choice == "report":
        coffeeMaker.report()
        moneyMachine.report()
    else:
        if coffeeMaker.is_resource_sufficient(menuItem.name):
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickels = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))
            cost = quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01
            if moneyMachine.make_payment(cost):
                menuItem = MenuItem(choice,  ,cost)
                menuItem.cost += cost
                coffeeMaker.make_coffee(menuItem.name)
                money_refunded = round(cost - menuItem.cost, 2)
                print(f"Here is your {menuItem.name}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there are not enough resources")