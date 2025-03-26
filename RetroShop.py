console_list = [
    ["PS3", 3, 130],
    ["DS", 5, 95],
    ["Wii", 10, 120],
    ["PSP", 12, 130],
    ["Ps vita", 9, 250]
]
shopping_cart = {} 


def delivery():
    print("Delivery info not implemented yet.")

def checkout():
    print("Checkout not implemented yet.")


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


def print_console_list():
    """
    Prints out all consoles in list
    """
    print("Student Summary:")
    for i in range(len(console_list)):
        print(f"{i + 1}. {console_list[i][0]} - {console_list[i][1]} in stock - ${console_list[i][2]}")


def order():
    """
    Allows user to select console in list and order it
    """
    loop = "yes"
    while loop == "yes":
        print_console_list()
        user_input = int_input_check("Choose a console via number its next to:\n> ")
        chosen_console = console_list[user_input - 1] # list start from 0 so make sure its right.
        if console_list[user_input - 1][1] <= 0: # Dont allow stock to go under 1
            print("Sorry, that console is out of stock.")
            loop = input("Continue ordering (yes)? \n> ").lower().strip()
            continue  # This will stop the function here
        console_list[user_input - 1][1] -= 1 # Remove 1 from stock
        print(f"You chose the {chosen_console[0]}") # see chosen console
        if chosen_console[0] in shopping_cart: # If the name is in the list then add 1 to the amount
            shopping_cart[chosen_console[0]] += 1    
        else: # If name isent set the value to 1
            shopping_cart[chosen_console[0]] = 1
        cart()
        loop = input("Add another item (yes)? \n> ").lower().strip()



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


def search():
    print_console_list()  # Shows the available consoles
    user_input = input("What would you like to search for? ").strip().lower()

    found = False
    for item in console_list:
        if item[0].lower() == user_input:
            print(f"{item[0]} is in stock with quantity {item[1]} at ${item[2]}.")
            found = True
            break

    if not found:
        print(f"{user_input} is not in the store list.")




def menu(): # Simple menu using if  else to choose options which call funcs
    while True:
        print("\n=== Retro game shop ===")
        print("1. List of consoles")
        print("2. Search list")
        print("3. Order console")
        print("4. Addresse/Pick up location")
        print("5. Review cart")
        print("6. Checkout")
        print("7. Quit")
        choice = input("> ")
        if choice == "1":
            print_console_list()
        elif choice == "2":
            search()
        elif choice == "3":
            order()
        elif choice == "4":
            delivery()
        elif choice == "5":
            cart()
        elif choice == "6":
            checkout()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid number.")


menu()