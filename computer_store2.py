# NOTES

# 4/11/24

# Made a new copy of this file in order to make some drastic changes.

# 4/10/24

# Despite specifically attempting to add the feature, the program still
# doesn't seem to be accepting the plural form of the products when ordering.
# Will continue debugging, problem seems to be at "Please enter the name of
# the product you would like to buy now".

# 4/9/24

# Left off around line 215. Working on getting the function that takes the
# desired product as input to accept either the singular and plural form of
# the device name.

# 4/8/24

# Left off around line 65 or so, dealing with a weird bug. I am trying to get
# 'laptops' to correct to 'Laptops' since it's the first item in my list, but
# my if statement that i wrote for that isn't catching it, quite strange...

# 4/5/24

# Left off at is_in_stock() function after attempting to purchase another
# product that was already sold out! 
# "UnboundLocalError: local variable 'user_quant' referenced before assignment"

##############################################################################

# Made this copy of the original program file for experimentation!

# sys.exit() terminates the program, exit status code is optional
from sys import exit

# Create a dictionary of products for sale at an electronics store, how 
# many of that item the store has in stock, and the price for each item; 
# please note that the prices are in dollars but I had to omit the $ signs;

electronics = {
        
        "laptop": {"Quantity": 100, "Price": 300, "Plural": "laptops"},
        
        "desktop": {"Quantity": 50, "Price": 500, "Plural": "desktops"},
        
        "router": {"Quantity": 30, "Price": 200, "Plural": "routers"},
        
        "switch": {"Quantity": 20, "Price": 100, "Plural": "switches"},
        
        "monitor": {"Quantity": 20, "Price": 75, "Plural": "monitors"},
        
        "mouse": {"Quantity": 20, "Price": 10, "Plural": "mice"},
        
        "hard drive": {"Quantity": 25, "Price": 100, "Plural": "hard drives"}

}

# Prompts the user for their desired product and returns the input
def enter_product():
    product = input("Please enter the name of the product you would like "
                    "to buy now: ")
    # Throughout this program, print() is sometimes used to enhance legibility
    print()
    product = product.lower()
    return product

# Creates a list of all of the electronics carried by the store, and then 
# joins them into string format, with each product separated by a comma
def print_electronics():
    # Create a list for the plural names of our electronics
    plural_electronics = []
    # Create some lists to get to the plural forms of our devices in stock
    singular_names = []
    # Iterate over singular device names in dictionary and append to items
    for device in electronics:
        singular_names.append(device)
    # Iterate over newly created list to get the device's plural name, we use
    # i in order to be able to capitalize the first letter of the first item
    for i in range(len(singular_names)):
        item = singular_names[i]
        plural_name = electronics[item]["Plural"]
        # Since 'laptops' is the first item, we want the 'l' to be capitalized
        if i == 0:
            # The capitalize() method capitalizes the first letter only and
            # converts all following letters to lower-case
            plural_name = plural_name.capitalize()
        # Create a new list that will store the plural names
        plural_electronics.append(plural_name)
    # Use join() method to turn our list into a string with ',' as separator
    joined_electronics = (', '.join(plural_electronics))
    # Now we inform the customer of everything they can buy at this store
    print(joined_electronics+'.')
    print()

# Prompt customer again after listing products that are in stock
def purchase_above_products(product):
    above_prods = input("Would you like to purchase one of the above "
                        "products? [Y/n]\n")
    # Use lower() to standardize user input, see below
    above_prods = above_prods.lower()

    if above_prods == 'y':
        # Go back to beginning of program
        beginning()
    elif above_prods == 'n':
        print()
        print(f"All right, no problem! Hopefully you can find what you are "
               "looking for at a different electronics store.\n")
        exit()
    else:
        print()
        print("Sorry, I didn't understand that. Why don't we start over?")
        beginning()

# This will run after user has made initial purchase
def make_another_purchase():
    # NOTE: with the input() statements, you must use \n instead of print()
    buy_more = input("Would you like to purchase anything else? [Y/n]\n")
    # Control for non-conforming user input by setting to lower-case
    buy_more = buy_more.lower()
    if buy_more == 'y':
        beginning()
    elif buy_more == 'n':
        print()
        print("OK, no problem! Thank you for shopping here.\n")
        exit()

# The below should maybe be its own function? 4/4/24
def transaction(product):
    # Define variable that will store current quantity of the product
    prod_quant = electronics[product]['Quantity']
    # Define variable that will store the price of the product, single unit
    prod_price = electronics[product]['Price']
    plural = electronics[product]['Plural']

    # If customer has already purchased all of the product in stock
    if prod_quant <= 0:
        print(f"Sorry, I'm afraid we are all sold out of {plural}.\n")
        make_another_purchase()

    # Check the value in the dictionary, which is the number of that 
    # product that the store has in stock
    elif prod_quant > 0:
        
        # Takes user input and casts it as an integer
        user_quant = input(f"We do have {plural}! We currently have "
                        f"{prod_quant} in stock. How many would you like? ")
        # Just to make output more legible
        print()
        # Cast user_quant as integer so we can perform calculations with it
        user_quant = int(user_quant)

    # Ensure customer doesn't want more of the product than we have in stock
    if user_quant <= prod_quant:
        total = (user_quant * prod_price)
        print(f"Great! That will be ${total}!\n")
        update_stock(prod_quant, user_quant, product)
        # DEBUG
        print(f'Updated {product} stock: {electronics[product]["Quantity"]}\n')
        make_another_purchase()
    
    elif user_quant > prod_quant:
        buy_max_amount = input("I'm sorry, like I said we only have "
                            f"{prod_quant} {plural} in stock, would you "
                            "like to buy that amount instead? [Y/n]\n")
        
        if buy_max_amount == 'y':
            # Update user's desired quantity to quantity currently in stock
            user_quant = prod_quant
            # Calculate price total
            total = (user_quant * prod_price) # Repeat code, look above
            print()
            print(f"Great! That will be ${total}.\n")
            update_stock(prod_quant, user_quant, product)
            # DEBUG
            print(f'Updated {product} stock: {prod_quant}\n')
            #print(f'Updated {product} stock: {electronics[product]["Quantity"]}\n')
            make_another_purchase()

        elif buy_max_amount == 'n':
            print()
            print("OK, no problem. Would you like to hear again what " 
                "products we have for sale? [Y/n]")
            
            # This variable just stores their response to the question
            hear_again = input().lower()
            print()

            if hear_again == 'y':
                print_electronics()
                beginning()
            
            elif hear_again == 'n':
                print("OK, no problem! Hopefully you can find what you're "
                    "looking for at a different store.\n")

# If product is in our dictionary, then we check whether it is in stock
def is_in_stock(product):        
    # If user has provided a valid singular product name
    if product in electronics:
        # Call function that will process transaction
        transaction(product)

    # Else if user has provided a valid plural product name
    elif product not in electronics:                
        # Create a list to store all plural names of products
        plural_names = []
        # Assign dictionary keys that store plural product names to variable
        plural_product = electronics[product]['Plural']
        print(f'plural_product: {plural_product}\n')
        # Iterate over singular product names and...
        for product in electronics:
            print(f'product in electronics: {product}\n')
            # add their plural names to list
            plural_names.append(plural_product)
        # If user has provided a valid plural product name
        if product in plural_names:
            transaction(product)

# Call this function only after making a sale to update dictionary/inventory
def update_stock(prod_quant, user_quant, product):
    # New product quantity in stock after selling some of them to user
    new_prod_quant = (prod_quant - user_quant)
    # Update dictionary to reflect new quantity in stock
    electronics[product]["Quantity"] = new_prod_quant

# You can encapsulate your entire program, or portions of it, inside of a
# function definition in order to restart the program as needed; this is
# similar to the main() function in C
def beginning():
    # I sometimes use print() statements to enhance legibility in the terminal
    print()

    # Call function that asks customer what product they want, capture output
    product = enter_product()

    # If the product entered is a valid singular product name...
    if product in electronics:
        # then we move onto the next step of checking if it's in stock
        is_in_stock(product)
    
    # Else if the product entered is not a valid singular product name, 
    # then we check whether it is a valid plural product name
    elif product not in electronics:
        # Create a list to store all of the plural product names
        plural_names = []
        # Iterate over outer dictionary keys to get singular product names
        for product in electronics:
            # Create variable to store the value of the inner "Plural" key
            plural_product = electronics[product]["Plural"]
            # Add the plural product name to list
            plural_names.append(plural_product)
        # If the user entered a valid plural product name
        if product in plural_names:
            # is_in_stock() accepts either singular or plural product names
            is_in_stock(product)
        
        # Else if product is not a valid singular or plural product name
        elif product not in plural_names:
            print(f"Sorry, we don't carry that product. These are the products "
               "we do carry:\n")
            # Print the electronics we have in stock, the current stock is dynamic
            print_electronics()
            # Prompt the user whether they want to purchase something now
            purchase_above_products(product)

# This is the first functional call that initiates the program
beginning()