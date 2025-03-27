console_list = [
    ["PS3", 3, 130],
    ["DS", 5, 95],
    ["Wii", 10, 120],
    ["PSP", 12, 130],
    ["Ps vita", 9, 250]
]
shopping_cart = {} 

yes_answers = [
    "yes", "yeah", "yep", "yea", "yup", "yuh", "sure", "of course", "definitely", 
    "absolutely", "affirmative", "indeed", "roger", "ok", "okay", "sure thing", 
    "totally", "uh-huh", "aye", "ya", "certainly", "for sure", "you bet", "correct", 
    "true", "right", "indubitably", "gladly", "why not", "very well",
]

no_answers = [
    "no", "nope", "nah", "nuh-uh", "negative", "never", "not at all", "no way", 
    "absolutely not", "by no means", "not really", "i don't think so", "uh-uh", 
    "nay", "false", "incorrect", "no chance", "not happening", "out of the question",
    "hell no", "not in a million years"
]


def checkout():
    cart()


def yes_no_loop(text):
    loop = input(text).lower().strip()
    while loop not in yes_answers + no_answers:
        loop = input("Unepected input please enter yes or no to the previous question\n> ").lower().strip()
    return loop


def print_console_list():
    """
    Prints out all consoles in list
    """
    print("Console list:")
    for i in range(len(console_list)):
        print(f"{i + 1}. {console_list[i][0]} - {console_list[i][1]} in stock - ${console_list[i][2]}")


def order():
    """
    Allows user to select a console by typing its name and order it
    """
    loop = "yes"
    while loop in yes_answers:
        print_console_list()
        user_input = input("Type the name of the console you want to order:\n> ").strip().lower()
        found_console = None # Checks if console is found
        for console in console_list: # Loops through whole list
            if console[0].lower() == user_input: # scans through list for the console
                found_console = console # gets what the user typed and puts it into console 
                break
        if not found_console: # If there isent a console use error prevention 
            print("Console not found, check the name and try again")
            continue
        if found_console[1] <= 0: # if the console has less then 0 stock use error prevention so stock cant go -
            print("Sorry, that console is out of stock.")
            loop = input("Continue ordering (yes)? \n> ").lower().strip()
            continue
        found_console[1] -= 1 # removes 1 stock
        print(f"You chose the {found_console[0]}")  # confirmation message
        gf_milk = yes_no_loop("Would you like to add some gluten free milk on top of that?\n> ")
        if gf_milk in yes_answers:
            print(f"Gluten free milk added to your {found_console[0]}")
        if found_console[0] in shopping_cart: # updates shopping cart
            shopping_cart[found_console[0]] += 1    
        else:
            shopping_cart[found_console[0]] = 1
        cart() # calls the cart
        loop = yes_no_loop("Add another item (yes/no)? \n> ")





def cart():
    """
    Shows all items in cart with quantity and total price
    """
    if not shopping_cart:
        print("Your shopping cart is empty.")
        return
    total_price = 0 # Starting price blank
    print("Items in your cart:")
    for name, quantity in shopping_cart.items(): # Loops through each diffrent console and its qauintity in cart
        for item in console_list: # Looks for each item in list and if it finds one that matchs gets the price for it
            if item[0] == name:
                price = item[2]
                break
        print(f"- {name} x{quantity} = ${price * quantity}") # Prints the price 
        total_price += price * quantity
    print(f"Total: ${total_price}")



def cart_function():
    if not shopping_cart:
        return
    cart()
    loop = "yes"
    while loop in yes_answers:
        loop = yes_no_loop("Would you like to remove an item or add a item in your shopping cart (yes/no)?\n> ")
        while True:
            cart_question = input("""
=== Cart functions ===                             
1. Remove
2. Add
3. Quit\n>
""").lower().strip()
            if cart_question == "1" or cart_question == "remove":
                print("remove")
            if cart_question == "2" or cart_question == "add":
                print("remove")
            if cart_question == "3" or cart_question == "quit":
                menu()

            
            


def menu(): # Simple menu using if  else to choose options which call funcs
    while True:
        choice = input("""
=== Retro game shop ===
1. List of consoles
2.
3. Order console
4.
5. Review cart
6. Checkout
7. Quit\n>
""")
        if choice == "1":
            print_console_list()
        elif choice == "2":
            break
        elif choice == "3":
            order()
        elif choice == "4":
            break
        elif choice == "5":
            cart()
            cart_function()
        elif choice == "6":
            checkout()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid number.")


menu()