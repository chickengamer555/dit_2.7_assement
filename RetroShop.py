from datetime import datetime


"""
This program allows you to use an online retro game shop in python with said options below:
1. Order consoles
2: View menu of consoles
3: Search for specific consoles
4. View items in cart
5. Remove items in cart
6. Add extra stock of items in cart
7. Checkout system
8. Admin menu with features like adding new consoles or adding stock
"""


console_list = [
    ["PS3", 3, 130],
    ["DS", 5, 95],
    ["Wii", 10, 120],
    ["PSP", 12, 130],
    ["Ps vita", 9, 250],
    ["Xbox 360", 4, 130],
    ["GameCube", 7, 250],
    ["3DS", 6, 250],
    ["Dreamcast", 1, 300],
    ["NES", 3, 220],
    ["SNES", 2, 220]
]


shopping_cart = []


yes_answers = [
    "yes", "yeah", "yep", "yea", "yup", "yuh", "sure", "of course", "definitely",
    "absolutely", "affirmative", "indeed", "roger", "ok", "okay", "sure thing",
    "totally", "uh-huh", "aye", "ya", "certainly", "for sure", "you bet", "correct",
    "true", "right", "indubitably", "gladly", "why not", "very well", "uh huh",
    "for real", "hell yeah", "heck yes", "you know it", "yessir", "yeah buddy",
    "sure can", "can do", "no doubt", "surely", "sounds good", "that's right",
    "heck yeah", "yeppers", "abso-freakin-lutely", "count me in", "I’m down",
    "sign me up", "100%", "bet", "on it", "you already know", "fo sho", "legit",
    "true that", "say less", "clearly", "that’s a yes", "mmhmm", "with pleasure",
    "I suppose", "naturally", "why the heck not", "without a doubt", "yeah I guess",
    "if you say so", "you got it", "affirmative, captain", "aye aye", "hella yeah",
    "right on", "most assuredly", "yup yup", "you got that right", "no question",
    "by all means", "gladly", "willingly", "as you wish", "be my guest", "do it",
    "go ahead", "I concur", "I agree", "sounds like a plan", "I'm game", "just so",
    "naturally", "precisely", "positively", "sure enough", "verily", "very well",
    "without question", "yessiree", "yup yup", "you betcha", "you got it dude",
    "you know it brother", "you said it", "you're on", "alrighty", "aye aye captain",
    "bam", "booyah", "copy that", "da", "d'accord", "deal", "fair enough",
    "go for it", "good to go", "hell to the yes", "here here", "holla", "I do",
    "I shall", "I will", "I'm in", "indeedy", "it's a go", "ja", "k", "kewl",
    "mmkay", "most certainly", "oui", "right away", "rock on", "roger that",
    "sure thing boss", "that's correct", "that's for sure", "that's right",
    "totally tubular", "vamonos", "very true", "we have a deal", "word", "ye",
    "yea verily", "yeah man", "yeah mon", "yeah right", "yebo", "yepperoni",
    "yes indeedy", "yes please", "yes way", "yessum", "yis", "you bet your boots",
    "you bet your life", "you bet your sweet bippy", "you better believe it",
    "you got it partner", "you got that right", "you know that's right",
    "you may", "you're darn right", "you're right", "you're so right", "yup yup yup",
    "zactly"
]


no_answers = [
    "no", "nope", "nah", "nuh uh", "negative", "never", "not at all", "no way",
    "absolutely not", "by no means", "not really", "i don't think so", "uh-uh",
    "nay", "false", "incorrect", "no chance", "not happening", "out of the question",
    "hell no", "not in a million years", "nah fam", "don’t count on it", "lol no",
    "fat chance", "no sir", "I refuse", "ain’t gonna happen", "hard pass",
    "miss me with that", "no thanks", "I’m good", "I’d rather not", "no deal",
    "that’s a no from me", "hell naw", "denied", "nah bruh", "not interested",
    "ain’t it chief", "I’m gonna pass", "no shot", "dream on", "big nope",
    "double no", "over my dead body", "no can do", "nah dawg", "ain’t no way",
    "not likely", "don’t think so", "never ever", "you wish", "forget it",
    "no thank you", "stop right there", "negatory", "as if", "ugh no", "no freaking way",
    "not even once", "are you serious? no", "yeah no", "hard nope", "absolutely not, my dude",
    "not a chance", "not on your life", "not on your nelly", "no siree", "no way José",
    "not in this lifetime", "not on my watch", "over my dead body", "when pigs fly",
    "not in my house", "not now, not ever", "nothing doing", "no dice", "no joy",
    "no sirree bob", "no soap", "no way in hell", "nope nope nope", "not by a long shot",
    "not by any means", "not for all the tea in China", "not for love nor money",
    "not gonna happen", "not happening captain", "not in a million years",
    "not in the cards", "not on your tintype", "not within the realm of possibility",
    "nyet", "out of the question", "over my dead body", "think again", "uh uh",
    "veto", "we'll see", "yeah... no", "you must be joking", "you wish", "your loss",
    "zero chance"
]


def checkout():
    """
    This here is the checkout functions which will first show you your cart then ask if you want to continue to payment,
    if you say no or you dont have any items in shopping cart it will take you back to the menu.
    If you continue with yes it will allow you to enter a card number with forced checkers to make it so you have to enter a 16 digit number.
    This also does the same for wit cvv (forced 3 numbers) and exp date (forced 4 numbers) except with exp date you can only enter a valid date.
    I also use a function called blank checker for name which you can see comments on later. 
    Finally when its all done the cart is cleared, a message is sent and we go back to menu
    """
    cart()
    if not shopping_cart:
        print()
        return
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
                month = int(exp_date[:2])
                year = int("20" + exp_date[2:])
                if 1 <= month <= 12:
                    expiry_date = datetime(year, month, 1)
                    now = datetime.now().replace(day=1)
                    if expiry_date < now:
                        print("Card is expired")
                        continue
                    break
            print("Expiry date must be in MMYY format with a valid month (01 to 12).")
        blank_checker("Please enter a delivery adress",
                      "Error delivery adress cant be blank")
        shopping_cart.clear()
        print("Payment has cleared your package will be with you shortly")
        menu()


def int_input_check(text):
    """
    Keeps asking for input int untill a int is given, if a string is entered a error message is provied and the function restarts
    """
    while True:  # Error prevention
        try:
            value = int(input(text))
            return value
        except ValueError:
            print("Please enter a valid number.")


def blank_checker(text1, error):
    """
    Keeps asking for input untill a input is given, if a string that is blank is provied it will give a error message and restart
    """
    blank_check = input(f"{text1}\n> ").strip().lower()
    while blank_check == "":
        print(error)
        blank_check = input(f"{text1}\n> ").strip().lower()
    return blank_check


def yes_no_loop(text):
    """
    Keeps asking for an input untill a input that is in my yes or no list is given. 
    If input thats not in the lists are given then it will give a error message and restart.
    """
    loop = input(text).lower().strip()
    while loop not in yes_answers + no_answers:
        loop = input("Unepected input please enter yes or no to the previous question\n> ").lower().strip()
    return loop


def print_console_list():
    """
    Prints out consoles in a nice mannered fashion unless there are no consoles in my console list then it will give a error check and go back to menu
    """
    if not console_list:
        print("Sorry we have ran out of stock on everything")
        return()
    print("Console list:")
    for i in range(len(console_list)):
        print(f"{i + 1}. {console_list[i][0]} - {console_list[i][1]} in stock - ${console_list[i][2]}")


def order():
    """
    Prints out the list of consoles then uses console finder to allow the user to search for the console with a valdation message.
    After that the user enter the qaunity with a int checker, if the qauinty is less then 0 it will display a error message so they canr choose negative stock.
    If the qauinty they enter is higher then avalible stock it will give a error message and reask. Then uses yes no loop to see if they want gluten free milk.
    After that it will check if the item they have is in there cart or not. If it in the cart it will take that item in your cart 
    and add they amount of qauinty they chose to the stock. If it is not in shopping cart it will add the name, qauinty and price to your cart.
    Then it takes that qauinty you choose and minus it from the console in console list qauinty, if it goes below 0 it will remove it since there will be 0 stock.
    Then asks yes no loops weather to add another item. This keeps looping untill a user anwser is in no list.
    """
    if not console_list:
        return
    loop = "yes"
    while loop in yes_answers:
        print_console_list()
        found_console = console_finder("order")
        avalible_stock = found_console[1]
        print(f"You chose the {found_console[0]}")
        while True:
            qaunity = int_input_check("How many would you like to order?\n> ")
            if qaunity <= 0:
                print("Please enter a postive number")
            elif qaunity > avalible_stock:
                print(f"Sorry we only have {avalible_stock} in stock.")
            else:
                break
        gf_milk = yes_no_loop(
            "Would you like to add some gluten free milk on top of that?\n> "
        )
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
        cart()
        loop = yes_no_loop("Add another item (yes/no)? \n> ")
    menu()


def cart_finder(name):
    """
    Goes through the items in the cart untill if finds the item[0] or "name" that your looking for and 
    set that varible to "name" and then returns it for later usage 
    """
    for item in shopping_cart:
        if item[0].lower() == name.lower():
            return item
    return None


def console_finder(text, return_to_menu=False):
    """
    First if there are no items in console list it will return for error preventions.
    Then if there are items it will keep asking for a console via input. It will then search the enter console list 
    untill it can find the inputed console. If it can it will set that found console to the user input and return it for later.
    If it cant find the console itll give a error message and reask the question
    """
    if not console_list:
        print("Sorry we have ran out of stock on everything")
        return None
    while True:
        user_input = input(f"Type the name of the console you want to {text}:\n> ").strip().lower()
        for console in console_list:
            if console[0].lower() == user_input:
                return console
        print("Console could not be found in our list or is not in stock")


def cart():
    """
    First if there are no items in shopping cart it will return for error preventions. If there are items itll print out your cart nice and cleanly.
    """
    if not shopping_cart:
        print("Your shopping cart is empty.")
        return None
    total_price = 0
    print("Items in your cart:")
    for item in shopping_cart:
        name, qaunity, price = item
        print(f"- {name} x{qaunity} = ${item[2] * qaunity}")
        total_price += item[2] * qaunity
    print(f"Total: ${total_price}")


def cart_function():
    """
    Simple menu for all the cart functions that will keep asking you a option to choose untill you pick a proper option
    """
    if not shopping_cart:
        return
    while True:
        choice = input(
            "=== CART FUNCTIONS ===\n"
            "1. Remove from cart\n"
            "2. Add stock in cart\n"
            "3. Quit\n> "
        ).strip()
        if choice == "1":
            cart_remove()
        elif choice == "2":
            cart_stock()
        elif choice == "3":
            menu()
        else:
            print("Invalid option. Please choose a valid number.")


def cart_stock():
    """
    Firsts ask what console you want to add stock to then searchs for that consoles with cart finder. If that item is not in your cart it will
    give error prevention then reask. If the console is in the console list it will get the qauinty for the consoles and print a confiramtion message 
    with how much more stock you can add to your cart. It then will keep asking how much stock you want to add untill the user inputs a number that is in 
    stock value (cant add more then max) and isnt in the negatives. After that it will add that much qauinty to the chosen console in cart 
    and then minus that amount in the actaul consoles list. Finaly a confirmation message and then asking if they want to add more to which this will keep
    looping untill a anwser in no list is given. 

    """
    cart()
    loop = "yes"
    while loop in yes_answers:
        console_name = blank_checker("What item would you like to add stock to in your cart?", "Error: console cant be blank")
        found_console = cart_finder(console_name)
        if not found_console:
            print("That item is not in your cart")
            loop = yes_no_loop("Would you like to try a diffrent item? (yes/no)\n> ")
            continue
        for console in console_list:
            if console[0].lower() == found_console[0].lower():
                qauinty = console[1]
                break
        print(
            f"You chose the {found_console[0]}. You can add up to {qauinty} more"
        )
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
    """
    Asks for a item in cart then goes to search for said item with error previntion if it cant find the item in cart. If an item does exit
    it then will keep asking how much stock you want to remove untill the user inputs a number that is in stock value (cant add more then max) 
    and isnt in the negatives. Then after they enter a proper value it remove that amount from stock in cart and go find that console in console list
    then add the removed qauinty to that console in console list. 
    """
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
            for console in console_list:
                if console[0].lower() == cart_item[0].lower():
                    console[1] += qaunity
                break
            print(f"{cart_item[0]} has had {qaunity} stock removed from it.")
            cart_function()
            break


def add_new_console():
    """
    Very simple asks for a console to add with blank checker then price and qauinty with int checkers then adds those into the console list.
    Simple error preventions making sure price and stock must be postive numbers
    """
    console = blank_checker("What is the new console that we are stocking?", "Error no console was submited")
    while True:
        stock = int_input_check("How much stock will we have?\n> ")
        if stock <= 0:
            print("Sorry stock must be postive")
            continue
        break
    while True:
        price = int_input_check("What will our price be?\n> ")
        if price <= 0:
            print("Sorry stock must be postive")
            continue
        break
    console_list.append([console, stock, price])
    print(f"Console added: {console} Stock: {stock}, Price: ${price}")
    admin_menu()


def add_to_stock():
    """
    Simple prints the list of consoles and asks what console they want to add stock then gives confirmation message.
    Then asks for qauinty untill a postive value is given and that qaunity is added to the console in console list.
    Final confirmation message about the new stock
    """
    print_console_list()
    found_console = console_finder("add stock to")
    print(f"You chose the {found_console[0]}")
    while True:
        qaunity = int_input_check("How much stock would you like to add?\n> ")
        if qaunity <= 0:
            print("Please enter a postive number")
        else:
            break
    found_console[1] += qaunity
    print(f"{qaunity} units added to {found_console[0]}. New stock: {found_console[1]}")
    admin_menu()


def admin_menu():
    """    
    Simple menu for all the admin menu functions that will keep asking you a option to choose untill you pick a proper option
    """
    while True:
        choice = input(
            "=== ADMIN MENU ===\n"
            "1. Add to previous stock\n"
            "2. Add new console\n"
            "3. Quit\n> "
        )
        if choice == "1":
            add_to_stock()
        elif choice == "2":
            add_new_console()
        elif choice == "3":
            menu()
        else:
            print("Invalid option. Please choose a valid number.")


def menu():
    """    
    Simple menu for all the menu functions that will keep asking you a option to choose untill you pick a proper option.
    Adds a secret option for a admin menu that a password must be entered to grant acess to it.
    """
    while True:
        choice = input(
            "=== Retro game shop ===\n"
            "1. Order consoles\n"
            "2. Consoles in stock\n"
            "3. Search for a console\n"
            "4. Items in cart\n"
            "5. Checkout\n"
            "6. Quit\n> "
        ).strip().lower()
        if choice == "1":
            order()
        elif choice == "2":
            print_console_list()
        elif choice == "3":
            found_console = console_finder("search for", return_to_menu=True)
            if found_console:
                print(
                    f"{found_console[0]} was found. We currently have a stock of "
                    f"{found_console[1]}, and its price is set at ${found_console[2]}"
                )
        elif choice == "4":
            cart()
            if shopping_cart:
                loop = yes_no_loop("Would you like to access cart functions? (yes/no)\n> ")
                if loop in yes_answers:
                    cart_function()
                if loop in no_answers:
                    menu()
        elif choice == "5":
            checkout()
        elif choice == "6":
            print("Goodbye!")
            break
        elif choice == "admin menu":
            password = ["gluten free milk"]
            password_check = blank_checker(
                "Please enter the admin password to make sure your supposed to be here",
                "Error password cant be blank"
            )
            if password_check in password:
                admin_menu()
            if password_check not in password:
                print("You are not supposed to be here")
                menu()
        else:
            print("Invalid option. Please choose a valid number.")


if __name__ == "__main__":
    menu()
