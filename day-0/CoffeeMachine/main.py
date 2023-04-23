MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "profit": 0,
}


def total_sum(quarters, dimes, nickles, pennies):
    total_amount = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    return total_amount


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['profit']}")


def is_sufficient(coffee_select):
    if resources["water"] < MENU[coffee_select]["ingredients"]["water"]:
        print("Sorry there is not enough water")
        return False
    elif resources["milk"] < MENU[coffee_select]["ingredients"]["milk"]:
        print("Sorry there is not enough milk")
        return False
    elif resources["coffee"] < MENU[coffee_select]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee")
        return False
    else:
        return True


def check_transaction(total_amount):
    if total_amount > MENU[coffee_select]["cost"]:
        resources["profit"] += MENU[coffee_select]["cost"]
        change_money = total_amount - MENU[coffee_select]["cost"]
        # change_money = round(change_money, 2)
        print("Here is ${:0.2f} dollars in change.".format(change_money))
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(coffee_select):
    resources["water"] -= MENU[coffee_select]["ingredients"]["water"]
    resources["milk"] -= MENU[coffee_select]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee_select]["ingredients"]["coffee"]


flag = True

while flag:
    coffee_select = input("What would you like? (espresso/latte/cappuccino): ")

    if coffee_select == "report":
        report()
    elif coffee_select == "off":
        flag = False
    else:
        #After selection of the coffee we need to check if there is sufficient resource available for that coffee
        is_resource_sufficient = is_sufficient(coffee_select)

        if is_resource_sufficient:
            # Resolving amount to be paid for the selected coffee
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))

            total_amount = total_sum(quarters, dimes, nickles, pennies)

            is_transaction_successful = check_transaction(total_amount)
            if is_transaction_successful:
                make_coffee(coffee_select)
                print(f"Here is your {coffee_select}. Enjoy!")



























