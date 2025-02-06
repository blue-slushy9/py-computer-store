# You can encapsulate your entire program, or portions of it, inside of a
# function definition in order to restart the program as needed

def beginning():
    # sys.exit() terminates the program, exit status code is optional
    from sys import exit

    # Create a dictionary of products for sale at an electronics store, how 
    # many of that item the store has in stock, and the price for each item; 
    # please note that the prices are in dollars but I had to omit the $ signs;

    electronics = {
            
            "laptop": {"Quantity": 100, "Price": 300},
            
            "desktop": {"Quantity": 50, "Price": 500},
            
            "router": {"Quantity": 30, "Price": 200},
            
            "switch": {"Quantity": 20, "Price": 100},
            
            "monitor": {"Quantity": 20, "Price": 75},
            
            "mouse": {"Quantity": 20, "Price": 10},
            
            "hard drive": {"Quantity": 25, "Price": 100}

    }

    # Ask the customer what product they want, how many, give them the total 
    # for their order, and then update the inventory

    # Throughout this program, I use many print() statements to enhance 
    # legibility in the terminal, e.g. below
    print()

    # Prompts the user for their desired product and returns the input
    def enter_product():
        #print("Please enter the name of the product you would like to buy now: ")
        product = input("Please enter the name of the product you would like "
                        "to buy now: ")
        #print()
        return product
    # Call function, capture output
    product = enter_product()

    if product not in electronics:
        print(f"\nSorry, we don't carry {product}s at this time. These are the "
                "products we do carry: \n")


    # Creates a list of all of the electronics carried by the store, and then 
    # joins them into string format, with each product separated by a comma
    def print_electronics():

        # Create a list for all of our electronics
        electronics_list = []
        
        # electronics is the dictionary, this iterates over its keys
        for item in electronics:
            electronics_list.append(item)
        
        joined_electronics = (', '.join(electronics_list))
        # Now we inform the customer of what they can buy at this "store"
        print(f'{joined_electronics}\n')

    # Call the function        
    print_electronics()

    # Define function that prompts customer after listing products in stock 
    def purchase_above_prod():

        above_prods = input("Would you like to purchase one of the above\n"
                            "products? [Y/n]\n")
        above_prods = above_prods.lower()
        #return above_prods
        
        #above_prods = input().lower()
        #print()
        #above_prods = above_prods()

        if above_prods == 'y':
            product = enter_product()    
        elif above_prods == 'n':
            print(f"All right, no problem! Hopefully you can find {product}s\n"
                    "at a different electronics store!\n")
            exit()
        else:
            print("Sorry, I didn't understand that. Why don't we start over?\n")
            beginning()

    def if_product_avail():
        
        if product in electronics: 
            
            # Define variable that will store the quantity available of the product the 
            # user wants;
            prod_quant = electronics[product]['Quantity']
        
            # Define variable that will store the price of the product the
            # user wants
            prod_price = electronics[product]['Price']

            # Check the value in the dictionary, which is the number of that 
            # product that the store has in stock
            if prod_quant > 0:
                print(f"We do have {product}s! How many would you like?")
                print()
                quantity = int(input())
                print()
            
            total = (quantity * prod_price)
           
            # New product quantity in stock after selling some of them to user
            new_prod_quant = (prod_quant - quantity)

            if quantity == 1:
                print(f"Great! We do have 1 {product} available. That will be ${prod_price}.")
                print()

            elif quantity <= prod_quant:
                total = (quantity * prod_price)
                print(f"Great! We do have {quantity} {product}s available. That will be ${total}!")
                print()
            
            elif quantity > prod_quant:
                print(f"I'm sorry, we only have {prod_quant} {product}s in stock,\n" 
                        "would you like to buy that amount instead? [Y/n]")
                print()

                buy_max_amount = input().lower()
                print()
                
                if buy_max_amount == 'y':
                    quantity = prod_quant             
                    print(f"Great! That will be ${total}!")
                    print()
                    new_prod_quant = (prod_quant - quantity)
                    print(f"This is how many {product}s we have left after the sale:")
                    print()
                    print(new_prod_quant)
                    print()

                elif buy_max_amount == 'n':
                    print("OK, no problem. Would you like to know what other\n"
                            "products we have for sale again?")
                    print()

                    hear_again = input().lower()
                    print()

                    if hear_again == 'y':
                        create_electronics_list()
                        product = enter_product()
                        print()
                    
                    elif hear_again == 'n':
                        print(f"OK, no problem! Hopefully you can find what\n"
                                "you're looking for at a different store.")
                        print()
        
        #print(f"This is how many {product}s we have left after the sale:")
        #print()
        #print(new_prod_quant)

    # In the case that the product entered by the user is not in the inventory;
    #else:

    print()
    if_product_avail()
beginning()
