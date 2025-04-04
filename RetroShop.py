console_list = [
    ["PS3", 3, 130],
    ["DS", 5, 95],
    ["Wii", 10, 120],
    ["PSP", 12, 130],
    ["Ps vita", 9, 250]
]

shopping_cart = [
    ["PS3", 3, 130]
]

yes_answers = [
    "yes", "yeah", "yep", "yea", "yup", "yuh", "sure", "of course", "definitely", 
    "absolutely", "affirmative", "indeed", "roger", "ok", "okay", "sure thing", 
    "totally", "uh-huh", "aye", "ya", "certainly", "for sure", "you bet", "correct", 
    "true", "right", "indubitably", "gladly", "why not", "very well",
]

no_answers = [
    "no", "nope", "nah", "nuh uh", "negative", "never", "not at all", "no way", 
    "absolutely not", "by no means", "not really", "i don't think so", "uh-uh", 
    "nay", "false", "incorrect", "no chance", "not happening", "out of the question",
    "hell no", "not in a million years"
]


def checkout():
    cart()
    checkout_confirm = yes_no_loop("Would you like to continue to payment?\n> ")
    if checkout_confirm in yes_answers:
        while True:
            card_number = input("Card number?\n> ").strip().replace(" ", "")
            if card_number.isdigit() and len(card_number) == 16:
                break
            print("Please enter a valid card number thats 16 digits.")        
        while True:
            cvv = input("CVV?\n> ").strip().replace(" ", "")
            if cvv.isdigit() and len(cvv) == 3:
                break
            print("CVV must be exactly 3 digits.")
        blank_checker("Card holders name?", "Name cant be blank")
        while True:
            exp_date = input("Expiry date (MMYY)?\n> ").strip()
            if exp_date.isdigit() and len(exp_date) == 4:
                break
            print("Expiry date must be 4 digits (MMYY).")
        blank_checker("Please enter a delivery adress", "Error delivery adress cant be blank")
        shopping_cart.clear()
        print("Payment has cleared your package will be with you shortly")
        menu()


def int_input_check(text):
    """
    Asks for number with chosen text and value error built in
    """
    while True: # Error prevention
        try:
            value = int(input(text))
            return value # Returns the value of what they entered
        except ValueError:
            print("Please enter a valid number.")


def blank_checker(text1, error):
    blank_check = input(f"{text1}\n> ").strip().lower()
    while blank_check.strip() == "":
        print(error)
        blank_check = input(f"{text1}\n> ")
    return blank_check


def yes_no_loop(text):
    loop = input(text).lower().strip()
    while loop not in yes_answers + no_answers:
        loop = input("Unepected input please enter yes or no to the previous question\n> ").lower().strip()
    return loop


def print_console_list():
    if not console_list:
        print("Sorry we have ran out of stock on everything")
        menu()
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
        found_console = console_finder("order")
        avalible_stock = found_console[1]
        print(f"You chose the {found_console[0]}")  # confirmation message
        if avalible_stock <= 0: # if the console has less then 0 stock use error prevention so stock cant go -
            loop = yes_no_loop("Sorry, that console is out of stock would you like to contuine?\n> ")
            if loop in yes_answers:
                continue  # This will stop the function here
            if loop not in yes_answers:
                menu()
        while True:
            qaunity = int_input_check("How many would you like to order?\n> ")
            if qaunity <= 0:
                print("Please enter a postive number")
            elif qaunity > avalible_stock:
                print(f"Sorry we only have {avalible_stock} in stock. Please try again")
            else:
                break
        gf_milk = yes_no_loop("Would you like to add some gluten free milk on top of that?\n> ")
        if gf_milk in yes_answers:
            print(f"Gluten free milk added to your {found_console[0]}")
        cart_item = cart_finder(found_console[0])
        if cart_item:
            cart_item[1] += qaunity
        else:
            shopping_cart.append([found_console[0], qaunity, found_console[2]])
        found_console[1] -= qaunity
        if found_console[1] <= 0:
            console_list.remove(found_console)
        cart() # calls the cart
        loop = yes_no_loop("Add another item (yes/no)? \n> ")


def cart_finder(name):
    for item in shopping_cart:
        if item[0].lower() == name.lower():
            return item
    return None


def console_finder(text, return_to_menu = False):
    while True:
        user_input = input(f"Type the name of the console you want to {text}:\n> ").strip().lower()
        for console in console_list: # Loops through whole list
            if console[0].lower() == user_input: # scans through list for the console
                found_console = console # gets what the user typed and puts it into console 
                return found_console
        print("Console could not be found in our list or is not in stock")
        if return_to_menu:
            menu()
        

def cart():
    """
    Shows all items in cart with quantity and total price
    """
    if not shopping_cart:
        print("Your shopping cart is empty.")
        menu()
    total_price = 0 # Starting price blank
    print("Items in your cart:")
    for item in shopping_cart: # Loops through each diffrent console and its qauintity in cart
        name, qaunity, price = item
        price = item[2]
        print(f"- {name} x{qaunity} = ${price * qaunity}")
        total_price += price * qaunity
    print(f"Total: ${total_price}")



def cart_function():
    while True:
        choice = input("""
=== CART FUNCTIONS ===
1. Remove from cart
2. Add stock in cart
3. Quit\n> """).strip()
        if choice == "1":
            cart_remove()
        elif choice == "2":
            cart_stock()
        elif choice == "3":
            menu()
        else:
            print("Invalid option. Please choose a valid number.")
            

def cart_stock():
    cart()
    loop = "yes"
    while loop in yes_answers:
        console_name = blank_checker("What item would you like to add stock to in your cart?", "Error: console cant be blank")
        found_console = cart_finder(console_name)
        for console in console_list:
            if console[0].lower() == found_console[0].lower():
                qauinty = console[1]
                break
        else:
            print(f"There is no stock left for {found_console[0]}")
            loop = yes_no_loop("Would you still like to add to stock (yes/no)?\n> ", "Console name cant be blanked")
            continue
        print(f"You chose the {found_console[0]}. You can add up to {qauinty} more")
        while True:
            qaunity = int_input_check("How much stock would you like to add?\n> ")
            if qaunity <= 0:
                print("Please enter a positive number.")
            elif qaunity > qauinty:
                print(f"Sorry, you can only add up to {qauinty}.")
            else:
                break
        found_console[1] += qaunity
        console[1] -= qaunity
        print(f"{qaunity} units added to {found_console[0]}. New quantity in cart: {found_console[1]}")
        loop = yes_no_loop("Add more stock (yes/no)? \n> ")
    cart_function()


def cart_remove():
    cart()
    while True:
        item_name = input("What item would you like to remove from cart?\n> ").strip()
        cart_item = cart_finder(item_name)
        if cart_item:
            break
        else:
            print("Item not found in cart please try again.")
    while True:
        qaunity = int_input_check("How many would you like to remove?\n> ")
        if qaunity <= 0:
            print("Please enter a postive number")
        elif qaunity > cart_item[1]:
            print(f"Sorry you only have {cart_item[1]} in your cart. Please try again")
        else:
            cart_item[1] -= qaunity
            print(f"{cart_item[0]} has had {qaunity} stock removed from it.")
            cart_function()
            break


def add_new_console():
    console = blank_checker("What is the new console that we are stocking?", "Error no console was submited")
    stock = int_input_check("How much stock will we have?\n> ")
    price = int_input_check("What will our price be?\n> ")
    console_list.append([console, stock, price]) # Adds in all the data added 
    print(f"Console added: {console} Stock: {stock}, Price: ${price}") # Prints out what was added    
    admin_menu()           
            

def add_to_stock():
    loop = "yes"
    while loop in yes_answers:
        print_console_list()
        found_console = console_finder("add stock to")
        print(f"You chose the {found_console[0]}")  # confirmation message
        while True:
                qaunity = int_input_check("How much stock would you like to add?\n> ")
                if qaunity <= 0:
                    print("Please enter a postive number")
                else:
                    break
        found_console[1] += qaunity
        print(f"{qaunity} units added to {found_console[0]}. New stock: {found_console[1]}")
        loop = yes_no_loop("Add stock to another item (yes/no)? \n> ")
    admin_menu()



def admin_menu():
    while True:
        choice = input("""
=== ADMIN MENU ===
1. Add to previous stock
2. Add new console
3. Quit\n> """)
        if choice == "1":
            add_to_stock()
        elif choice == "2":
            add_new_console()
        elif choice == "3":
            menu()
        else:
            print("Invalid option. Please choose a valid number.")


def menu(): # Simple menu using if  else to choose options which call funcs
    while True:
        choice = input("""
=== Retro game shop ===
1. Order consoles
2. Consoles in stock
3. Search for a console
4.
5. Items in cart
6. Checkout
7. Quit\n> """).strip().lower()
        if choice == "1":
            order()
        elif choice == "2":
            print_console_list()
        elif choice == "3":
            found_console = console_finder("search for", return_to_menu = True)
            print(f"{found_console[0]} was found. We currently have a stock of {found_console[1]}, and its price is set at ${found_console[2]}")
        elif choice == "4":
            menu()
        elif choice == "5":
            cart()
            loop = yes_no_loop("Would you like to access cart functions\n> ")
            if loop in yes_answers:
                cart_function()
            if loop in no_answers:
                menu()
        elif choice == "6":
            checkout()
        elif choice == "7":
            print("Goodbye!")
            break
        elif choice == "admin menu":
            password = ["gluten free milk"]
            password_check = blank_checker("Please enter the admin password to make sure your supposed to be here", "Error password cant be blank")
        if password_check in password:
            admin_menu()
        if password_check not in password:
            print("You are not supposed to be here")
            menu()
        else:
            print("Invalid option. Please choose a valid number.")


menu()