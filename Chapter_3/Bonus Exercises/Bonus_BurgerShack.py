# BONUS EXERCISE - BURGER SHACK

# Welcome User "Burger Shack"
# TYPES OF BURGERS to show 
def user_choice_menu():
    print("**************** NEWLY OPENED IN RAK BRANCH ***********")
    print("\n\n----------🍔 Welcome to Burger Shack! 🍔 --------\n")
    print("Choose your burger?\n")
    print("1. Beef Burger - 🥩 \n")
    print("2. Chicken Burger - 🍗 \n")
    print("3. Vegetarian Burger - 🥬 \n")

# User will choice 1-3 in types of burger
def user_select_burger():
    select = int(input("Choose a burger (1-3): "))
    types_burgers = ["Beef Burger", "Chicken Burger", "Vegetarian Burger"]
    return types_burgers[select - 1]

# User will select toppings of their choice
def select_toppings():
    toppings = ["Cheese - 🧀", "Peanut Butter - 🥜 ", "Avocado - 🥑\n"]
    print("\nChoose your toppings (separate using commas):\n")
    print(", ".join(toppings))
    selected_toppings = input().split(', ')
    return selected_toppings

# User will choose condiments of their choice
def choose_condiments():
    condiments = ["\nKetchup - 🥫 ", "Mayonnaise - 🧴 ", "BBQ Sauce - 🍖\n"]
    print("\nChoose condiments (separate with commas):\n")
    print(", ".join(condiments))
    selected_condiments = input().split(', ')
    return selected_condiments

# User will choose sides of their choice
def choose_sides():
    sides = ["\nFries - 🍟 ", "Drink - 🥤 \n"]
    print("\nChoose sides (separate with commas):\n")
    print(", ".join(sides))
    selected_sides = input().split(', ')
    return selected_sides

# This will calculate the total price based on the condiments, sides and toppings and it will be added 
# returning to the total price
def calculate_total_price(burger, toppings, condiments, sides):
    burger_price = 5.00  # base price for any burger
    topping_price = len(toppings) * 0.50
    condiment_price = len(condiments) * 0.25
    side_price = len(sides) * 1.50
    total_price = burger_price + topping_price + condiment_price + side_price
    return total_price

# This to show the user how much is the total cost of the burgers and upgrades
# You will enter your payment
# Change will be given
# If insufficient fund it will tell user not enough funds 
def process_payment(total_price):
    print(f"Your total is ${total_price:.2f}")
    payment = float(input("Enter the payment amount: $"))
    change = payment - total_price
    if change >= 0:
        print(f"Thank you for your payment! Your change is ${change:.2f}", "Have a nice day! :) ")
    else:
        print("Insufficient payment. Please provide enough money.")

# Defined main func() to run the other functions we made a while ago
def main():
    user_choice_menu()
    selected_burger = user_select_burger()
    selected_toppings = select_toppings()
    selected_condiments = choose_condiments()
    selected_sides = choose_sides()

    total_price = calculate_total_price(selected_burger, selected_toppings,
                                        selected_condiments, selected_sides)

    process_payment(total_price)
    
# Run the main code
if __name__ == "__main__":
    main()