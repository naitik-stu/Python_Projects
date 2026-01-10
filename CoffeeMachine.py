menu = {
    "espresso": {
        "water": 50,
        "milk": 0,
        "coffee": 18,
        "cost": 2.0,
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "cost": 2.5,
    },
    "cappuccino": {
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "cost": 3.0,
    },

}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

def is_resource_available(order):
    for x in ["water", "milk", "coffee"]:
        if resources[x] < menu[order][x]:
            return False
    return True

def count_money(order):
    quarter = int(input("How many quarters: ")) * 0.25
    dime = int(input("How many dimes: ")) * 0.10
    nickel = int(input("How many nickels: ")) * 0.05
    penny = int(input("How many pennies: ")) * 0.01

    total_received = quarter + dime + nickel + penny
    cost = menu[order]["cost"]

    if total_received > cost:
        condition = 1
        change = round(total_received - cost, 2)
    elif total_received == cost:
        condition = 2
        change = 0
    else:
        condition = 3
        change = 0

    return condition, change

def make_coffee(order):
    for x in ["water", "milk", "coffee"]:
        resources[x] -= menu[order][x]
    resources["money"] += menu[order]["cost"]


run_machine = True

while run_machine == True:
    order = input("What would you like? (espresso/latte/cappuccino): \n")

    if order == "report":
        print(f"water : {resources['water']}ml\nmilk : {resources["milk"]}ml\ncoffee : {resources["coffee"]}g")

    elif order == "off":
        print("Turning off the coffee machine")
        run_machine = False

    elif order == "refill":
        resources["coffee"] = 100
        resources["milk"] = 200
        resources["water"] = 300

    elif order in ["espresso", "latte", "cappuccino"]:
        if not is_resource_available(order):
            print(f"The machine does not have enough resources to make a {order}")
        else:
            condition, change = count_money(order)
            if condition == 1:
                make_coffee(order)
                print(f"\nHere is your {order}!! and change which is ${change}\n")
            elif condition == 2:
                make_coffee(order)
                print(f"\nHere is your {order}!! \n")
            elif condition == 3:
                print(f"You did not give enough coins")
        

