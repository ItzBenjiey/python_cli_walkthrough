"""
work wants an inventory app that:
    stores data into a file
    uses the command line to list/add/update/delete: 
        "items" they have:
            id
            cond
            name
            ?checkedIn?
"""
next_id = 0
items = [1, 2, 3]
# TODO make a menu printout showiing options
from typing import ItemsView


def menu():
    print(""""
1. List All Items
2. Add New Item
3. Update Existing Item
4. Delete Item (By item id)
5. Exit
""")
# This lists all items
def list_items():
    for item in items:
        print(item)
    print("in list item function")
# Add New Item
def new_item():
    global next_id
    name = input("Name: ")
    cond = input("Condition: ")
    item_id = next_id
    next_id += 1




# Update Existing Item
def update_existing(itemId):
    pass

# Delete Item (By item id)
def delete_item(itemId):
    pass

# Make the menu questions that grab the data
while True:
    menu() 
    choice = input("> ")

    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    if choice == "5": # Exit
        exit()
    else:
        input("Invalid Input, give a number\n(Press Enter to Try Again)")



# make the file saving stuff
