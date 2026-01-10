fruit_stock = {
    "apple": {"stock": 56, "price": 0.99},
    "mango": {"stock": 42, "price": 1.99},
    "banana": {"stock": 48, "price": 11.99},
    "watermelon": {"stock": 12, "price": 7.99},
    "melon": {"stock": 18, "price": 11.99},
    "grapes": {"stock": 24, "price": 4.99},
    "pear": {"stock": 28, "price": 2.99},
    "strawberry": {"stock": 128, "price": 9.99}
}

cart = {
    "apple": {"quantity": 0, "price": 0},
    "mango": {"quantity": 0, "price": 0},
    "banana": {"quantity": 0, "price": 0},
    "watermelon": {"quantity": 0, "price": 0},
    "melon": {"quantity": 0, "price": 0},
    "grapes": {"quantity": 0, "price": 0},
    "pear": {"quantity": 0, "price": 0},
    "strawberry": {"quantity": 0, "price": 0}
}

# Show fruits in a table
print("Welcome to Fruit Shop of Borxx")
print("Available Fruits:\n")
print("Fruit         Stock   Price($)")
print("-------------------------------")

for fruit in fruit_stock:
    print(f"{fruit:<13}{fruit_stock[fruit]['stock']:<8}{fruit_stock[fruit]['price']}")

# Buying loop
while True:
    fruit_name = input("\nWhich fruit do you want to buy? (type 'done' to finish) ").lower()
    if fruit_name == "done":
        break

    if fruit_name in fruit_stock:
        how_many = int(input(f"How many {fruit_name}s do you want to buy? "))

        if how_many > 0 and how_many <= fruit_stock[fruit_name]["stock"]:
            cost = how_many * fruit_stock[fruit_name]["price"]
            fruit_stock[fruit_name]["stock"] -= how_many

            cart[fruit_name]["quantity"] += how_many
            cart[fruit_name]["price"] += cost

            print(f"You bought {how_many} {fruit_name}(s) for ${cost:.2f}")
            print(f"Remaining {fruit_name}s in stock: {fruit_stock[fruit_name]['stock']}")

            # show cart after each purchase
            print("\nYour Cart:")
            print("Fruit         Quantity   Price($)")
            print("---------------------------------")

            total = 0
            for fruit in cart:
                if cart[fruit]["quantity"] > 0:
                    print(f"{fruit:<13}{cart[fruit]['quantity']:<10}{cart[fruit]['price']:.2f}")
                    total += cart[fruit]["price"]

            print("---------------------------------")
            print(f"Current Total: ${total:.2f}")
        else:
            print("Invalid quantity. Check the stock or enter a positive number.")
    else:
        print("Sorry, we don't have that fruit.")

# Final bill
print("\nFinal Cart:")
print("Fruit         Quantity   Price($)")
print("---------------------------------")

total = 0
for fruit in cart:
    if cart[fruit]["quantity"] > 0:
        print(f"{fruit:<13}{cart[fruit]['quantity']:<10}{cart[fruit]['price']:.2f}")
        total += cart[fruit]["price"]

print("---------------------------------")
print(f"Total Bill: ${total:.2f}")
print("Thank you for shopping at Borxx!")
