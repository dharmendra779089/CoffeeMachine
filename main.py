# Coffee Machine Program

MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    }
}

resources = {
    "water": 500,
    "milk": 250,
    "coffee": 100,
    "money": 0.0
}

def print_report():
    """Prints current resources."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")

def check_resources(order_ingredients):
    """Checks if there are enough resources."""
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    return round(quarters + dimes + nickels + pennies, 2)

def is_transaction_successful(payment, drink_cost):
    """Return True if the payment is accepted, or False if insufficient."""
    if payment >= drink_cost:
        change = round(payment - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        resources["money"] += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

# Main loop
machine_on = True
while machine_on:
    choice = input("What would you like? ('espresso' 'latte' 'cappuccino'): ").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print_report()
    elif choice in MENU:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid selection.")
