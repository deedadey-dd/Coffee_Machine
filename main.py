#TODO 1. Create a List of Dictionaries that contain the menu.
menu = {
    "espresso":{
        "price": 1.50,
        "water": 50,
        "coffee": 18,
        "milk":0,
},
    "latte": {
        "price": 2.50,
        "water": 200,
        "coffee": 24,
        "milk": 150,
    },
    "cappuccino": {
        "price": 3.00,
        "water": 250,
        "coffee": 24,
        "milk": 100,
    },}

# print(menu["latte"]["milk"])
#TODO 2. Create a Dictionary that contains the resources.
ingredients = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
    "sales": 0
}
# print(ingredients["water"] - 20)
#TODO 3. Ask customer to choose their flavour
    #based on their choice, check if there is enough resources
        # and give reply if not
    # else go ahead to ask for payment
    # sum payments and check if it is greater or equal to the price
        #if not, give feedback
        # else go ahead and prepare the order
    # if payment was greater, deduct and give change.
water_remain = ingredients["water"]
milk_remain = ingredients["milk"]
coffee_remain = ingredients["coffee"]
sales = round(ingredients["sales"], 2)

# while ingredients["water"] > 51:
#
#     ingredients["water"] -= menu["espresso"]["water"]
#     water_remain = ingredients["water"]
#     print(f"Water Before subtraction: {water_remain}")
#     print(ingredients["water"])
# else:
#     print(f"Only {water_remain} left")


# Repeat from Here
while ingredients["water"] > 49 and ingredients["coffee"] > 17:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    water_remain = ingredients["water"]
    milk_remain = ingredients["milk"]
    coffee_remain = ingredients["coffee"]
    sales = round(ingredients["sales"], 2)

    if order == "report":
        print(f"Water: {water_remain}ml\nMilk: {milk_remain}ml\nCoffee: {coffee_remain}g\nSales: ${sales}")
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        if ingredients["water"] < menu[order]["water"]:
            print("Sorry there is not enough water.")
        elif ingredients["milk"] < menu[order]["milk"]:
            print("Sorry there is not enough milk.")
        elif ingredients["coffee"] < menu[order]["coffee"]:
            print("Sorry there is not enough coffee.")

        else:
            print("Please insert coins.")
            quarters = int(input("how many quarters?:"))
            dimes = int(input("how many dimes?:"))
            nickles = int(input("how many nickles?:"))
            pennies = int(input("how many pennies?:"))

            payment = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
            change = round((payment - menu[order]["price"]), 2)

            if payment < menu[order]["price"]:
                print(f"Sorry that's not enough money. ${payment} refunded.")

            elif payment > menu[order]["price"]:
                ingredients["water"] -= menu[order]["water"]
                ingredients["milk"] -= menu[order]["milk"]
                ingredients["coffee"] -= menu[order]["coffee"]
                ingredients["sales"] += menu[order]["price"]
                print(f"Here is your change of ${change}")
                print(f"... and Here is your {order} ☕️. Enjoy!")

            else:
                ingredients["water"] -= menu[order]["water"]
                ingredients["milk"] -= menu[order]["milk"]
                ingredients["coffee"] -= menu[order]["coffee"]
                ingredients["sales"] += menu[order]["price"]
                print(f"Here is your {order} ☕️. Enjoy!")
    else:
        print(f"Please check and enter the right menu.\n{order} is not on the menu")

else:
    print(f"Ingredients Available \nWater: {water_remain}ml\nMilk: {milk_remain}ml\nCoffe: {coffee_remain}g\nThe resources available cannot be used to prepare {order}")

