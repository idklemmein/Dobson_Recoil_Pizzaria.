# pandas is imported to create and manipulate a DataFrame, which is used to store and calculate the order details such as items, quantities, prices, and total costs.
import pandas
# functions go here


# Checks that user has a valid response (e.g. yes/no, cash/credit) based on the list of options
def string_checker(question, valid_ans):
    while True:
        error = f"Enter a valid response from {valid_ans}"
        user_response = input(question).lower()
        if user_response in valid_ans or user_response in [item[0] for item in valid_ans]:
            return valid_ans[[item[0] for item in valid_ans].index(user_response)] if user_response in [item[0] for item in valid_ans] else user_response
        print(error)

# Prints welcome message
def welcome_message():
    print("                   <--- Welcome to the Dobson Recoil Pizzeria --->")
    print("In our pizza place, you will order and eat quality pizzas, made with premium ingredients")
    print("Keep in mind, on our special anniversary event every 3rd pizza is on a 50% discount!! (toppings are not included in the discount)")

# Shows history of the pizzeria
def history():
    print('''
    Dopson Recoil Pizzeria, established in 2003 in Auckland, New Zealand, was the brainchild of culinary enthusiasts Quinntopleson Dopson and Stefan Recoil.
    They aimed to blend traditional Italian pizza-making techniques with local New Zealand ingredients.
    Over the years, the pizzeria became renowned for its unique flavor combinations and community-oriented atmosphere.
    Its signature wood-fired pizzas and commitment to quality earned it a loyal following, making Dobson Recoil Pizzeria a beloved staple in Mount Maunganui's dining scene.
    ''')


# Gather Customer Information
def get_customer_info():
    name = validate_name("Please enter your name: ")
    phone = validate_phone("Please enter your phone number (max 14 digits): ")
    return name, phone

# Validates that the name contains only letters and is not blank
def validate_name(question):
    while True:
        response = input(question).strip()
        if response == "":
            print("Sorry, this field cannot be blank")
        elif all(letters.isalpha() or letters.isspace() for letters in response):
            return response
        else:
            print("Invalid input. Please enter letters only.")




# Validates that the phone number contains only digits and is no more than 14 digits long
def validate_phone(question):
    while True:
        response = input(question).strip()
        if response.isdigit() and len(response) <= 14:
            return response
        else:
            print("Invalid input. Please enter digits only, with a maximum of 14 digits.")

# Validates that the address is not blank and contains only letters, digits, and spaces
def validate_address(question):
    while True:
        response = input(question).strip()
        if response == "":
            print("Sorry, this field cannot be blank.")
        elif all(char.isalnum() or char.isspace() for char in response):
            return response
        else:
            print("Invalid input. Please enter letters, numbers, and spaces only.")

# Set maximum number of pizzas/toppings below
MAX_PIZZAS = 5
# List created to show menu
pizzas = ["Meat Lovers Pizza","Margherita Pizza", "Pepperoni Pizza", "Hawaiian Pizza", "Vegetarian Pizza",
          "Supreme Pizza", "Seafood Pizza","Gluten-free Pizza", "Cheese pizza", "Lamb Kebab Pizza"]
# regular pizza prices
reg_prices = [21,15, 18, 22,17, 23, 24, 18, 15, 15]
# large pizza prices
large_prices = [23, 18, 22, 25, 22.50, 27, 27, 22.50, 18, 18]


pizza_dict2 = {
    "Pizzas": pizzas,
    "Regular": reg_prices,
    "Large": large_prices
}


display_menu = pandas.DataFrame(pizza_dict2)
display_menu.index +=1
# list to display the toppings menu if the user would like toppings
topping_options = ["Feta Cheese", "Pepperoni", "Mushrooms", "Green Peppers", "Black Olives", "Italian Sausage", "Red Onions", "Spinach", "Bacon", "Tomatoes"]

# A list to hold the topping prices
topping_prices = [2, 1.5, 1.5, 2.5, 2.3, 3, 2, 1, 3, 4]

toppings_menu_dict = {
    "Toppings": topping_options,
    "Price": topping_prices
}

topping_menu = pandas.DataFrame(toppings_menu_dict)
topping_menu.index +=1

# List to hold pizza details/ the pizza I.D
pizza_dict = {
    1: "Meat Lovers Pizza",
    2: "Margherita Pizza",
    3: "Pepperoni Pizza",
    4: "Hawaiian Pizza",
    5: "Vegetarian Pizza",
    6: "Supreme Pizza",
    7: "Seafood Pizza",
    8: "Gluten-free Pizza",
    9: "Cheese pizza",
    10: "Lamb Kebab Pizza"
}
# List to hold topping details/ the topping I.D
topping_dict = {
    1: "Feta Cheese",
    2: "Pepperoni",
    3: "Mushrooms",
    4: "Green Peppers",
    5: "Black Olives",
    6: "Italian Sausage",
    7: "Red Onions",
    8: "Spinach",
    9: "Bacon",
    10: "Tomatoes"
}

# Prices for pizzas
pizza_prices = {
    1: [21, 23],
    2: [15, 18],
    3: [18, 22],
    4: [22, 25],
    5: [17, 22.50],
    6: [23, 27],
    7: [24, 27],
    8: [18, 22.50],
    9: [15, 18],
    10: [15, 18]
}

# prices for toppings
topping_prices = {
    1: [2],
    2: [1.5],
    3: [1.5],
    4: [2.5],
    5: [2.3],
    6: [3],
    7: [2],
    8: [1],
    9: [3],
    10: [4]
}

# Checks that user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("Sorry, this can't be blank. Please try again.")
        else:
            return response

# Checks if user enters a number between a low and high range. Returns a valid number
def num_check(question, low, high):
    while True:
        to_check = input(question)
        if to_check == "xxx":
            return to_check
        try:
            response = int(to_check)
            if response >= low and response <= high:
                return response
            else:
                print(f"Please enter a number between {low} and {high}.")
        except ValueError:
            print("Please enter an integer.")

# Main routine for ordering pizza
def order_pizza():
    order = []
    item_list = []
    quantity_list = []
    price_list = []

    pizza_count = 0  # Counter to track the number of pizzas ordered


    while len(order) < MAX_PIZZAS:
        pizza_num = num_check("Enter the number of the pizza you would like to order (1-10) or 'xxx' to finish: ", 1, 10)
        if pizza_num == "xxx":
            break
        elif pizza_num in pizza_dict:
            quantity = num_check(f"How many of {pizza_dict[pizza_num]} would you like to order? ", 1, 5)
            size = string_checker("Would you like a regular or large pizza? (r/l): ", ["r", "l"])
            for _ in range(quantity):
                pizza_count += 1
                price = pizza_prices[pizza_num][0] if size == "r" else pizza_prices[pizza_num][1]

                # Apply 50% discount to every third pizza
                if pizza_count % 3 == 0:
                    price *= 0.5

                order.append((pizza_dict[pizza_num], size))
                item_list.append(pizza_dict[pizza_num])
                quantity_list.append(1)
                price_list.append(price)
        else:
            print("Invalid pizza number, please choose a valid number between 1 and 10.")
    return order, item_list, quantity_list, price_list

# Function to order toppings
def order_toppings(item_list, quantity_list, price_list, num_pizzas):
    toppings = []
    for i in range(num_pizzas):
        print(f"\nToppings for Pizza {i + 1}:")
        while True:
            topping_num = num_check(
                "Enter the number of a topping you would like to add (1-10) or 'xxx' to finish toppings: ", 1, 10)
            if topping_num == "xxx":
                break
            elif topping_num in topping_dict:
                topping_price = topping_prices[topping_num][0]  # Get the correct price for the topping
                toppings.append(topping_dict[topping_num])
                item_list.append(f"Topping for Pizza {i + 1}: {topping_dict[topping_num]}")
                quantity_list.append(1)
                price_list.append(topping_price)
            else:
                print("Invalid topping number, please choose a valid number between 1 and 10.")
    return toppings


# Function to calculate total price
def calculate_price(prices, delivery_surcharge):
    total_price = sum(prices)
    total_price += delivery_surcharge
    return total_price

# Function to process payment
def process_payment(total_price):
    print(f"Your total is ${total_price:.2f}.")
    payment_method = string_checker("Would you like to pay by cash or credit? ", ["cash", "credit"])
    if payment_method == "cash":
        print("Please have your cash ready upon delivery or pickup.")
    else:
        # 5% surcharge added if credit is selected
        surcharge = total_price * 0.05
        print(f"There is a 5% surcharge which is ${surcharge:.2f}, The total price is: ${total_price + surcharge}")
        print("Please swipe your card when the delivery arrives or at the counter upon pickup.")

# Function to print the order summary
def print_order_summary(expense_frame, delivery_surcharge, sub_total, pizza_count):
    print("\n********* Order Summary *********")
    print(expense_frame)
    print(f"\nSubtotal: ${sub_total:.2f}")
    if delivery_surcharge > 0:
        print(f"Delivery Surcharge: ${delivery_surcharge:.2f}")
    print(f"Total: ${sub_total + delivery_surcharge:.2f}")
    if pizza_count >= 3:
        print("\nNote: Your total includes a 50% discount on every 3rd pizza ordered!")
    print("*********************************")



# Main routine
def main():
    welcome_message()

    yes_no = ["yes", "no"]
    pick_del = ["delivery", "pick up"]

    want_history = string_checker("\nWould you like to learn about the history of Dobson Recoil Pizzeria? ", yes_no)
    if want_history == "yes":
        history()

    name, phone = get_customer_info()

    want_order = string_checker(f"Hello, {name}, would you like to order delivery or pick up? ", pick_del)
    delivery_surcharge = 0
    if want_order == "delivery":
        address = validate_address("Please enter your address ")
        print("A $5 surcharge will be applied to your order!")
        delivery_surcharge = 5
    elif want_order == "pick up":
        print("Our address is:")
        print("565 Maunganui Road, Mount Maunganui 3116.")
        print("See you soon!\n")

    # Automatically display the pizza menu after choosing delivery or pick up

    print()
    print(display_menu)
    print()

    order, item_list, quantity_list, price_list = order_pizza()

    if order:
        print("\nYour pizza order is:")
        for item in order:
            print(f"- {item[0]} ({'Regular' if item[1] == 'r' else 'Large'})")

        add_toppings = string_checker("\nWould you like to add toppings to your pizza(s)? ", yes_no)
        if add_toppings == "yes":
            # show_toppings_menu()
            print(topping_menu)
            toppings = order_toppings(item_list, quantity_list, price_list, len(order))
        else:
            print("No toppings added.")

        # Create DataFrame
        variable_dict = {
            'Item': item_list,
            'Quantity': quantity_list,
            'Price': price_list
        }
        expense_frame = pandas.DataFrame(variable_dict)
        expense_frame = expense_frame.set_index('Item')

        # Calculate cost of each component
        expense_frame['Cost'] = expense_frame['Price']

        # Find sub-total
        sub_total = expense_frame['Cost'].sum()

        # Print the final order summary, including pizza count
        pizza_count = len(order)
        print_order_summary(expense_frame, delivery_surcharge, sub_total, pizza_count)

        total_price = calculate_price(price_list, delivery_surcharge)
        process_payment(total_price)
        print("Thank you for ordering from Dobson Recoil Pizzeria! Your order will be ready soon.")
    else:
        print("Thank you! Have a nice day.")

if __name__ == "__main__":
    main()