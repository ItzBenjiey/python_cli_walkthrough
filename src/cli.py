"""
Work wants an inventory app that:
    Stores Data into a file
    Uses the command line to list/add/update/delete:
        "Items" they have:
            id
            name
            cond
"""
from models.item import Item    # And Import Statement to make code code from other files available

next_id = 0
items = []  # this will be used to store items

def menu():     # prints menu options for user
    print("""
1. List All Items
2. Add New Item
3. Update Existing Item
4. Delete Item (By item id)
5. Exit
""")


def list_items():       # writes all items to terminal 
    for item in items:
        print(item)

# Add New Item
def new_item():         # gets user input for all need fields for an Item
    global next_id      # Allow us access to the next_id number, To 

    name = input("Name: ")
    cond = input("Condition: ")
    item_id = next_id       # Uses the global counter to give a unique ID to each "Item"

    next_id += 1        # Updates Id with new value so next one is 1 more

    # This is the Class -> Item from the other file we imported
    tmp = Item(item_id, name, cond) #Builds An Item/Stores it in tmp

    items.append(tmp)  # Adds Item to global items array


# Update Existing Item
def update_existing(itemId):
    pass

# Delete Item (By item id)
def delete_item(itemId):
    pass

# Make the menu questions that grab the data 
def main():         #starts the program off, holds the loop until exit.
    while True:
        menu()      #prints the Options to the Terminal
        choice = input("> ")    # Takes use choice

        # The conditional options: hands off the work to the functions above
        if choice == "1":
            list_items()
        elif choice == "2":
            new_item()
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5": # Exit
            exit()
        else:           # USer gave us bad input we let them know to looop again
            input("Invalid Input!\n(Press Enter to try again)")


# Make the File Saving stuff

if __name__ == "__main__":
    main()