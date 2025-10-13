# Step 1: Create an empty list for the shopping list.
# optional: see if there is an existing shopping list file and load that
# hint: use try/except to check if the file exists, or import os and use os.path.exists()

# Step 2: Define a function to add an item to the list.
# Prompt the user for the item name and add it to the list.

# Step 3: Define a function to remove an item from the list.
# Prompt the user for the item name to remove and delete it from the list if it exists.
# hint: use list.remove() or check if item is in list first

# Step 4: Define a function to write the current shopping list to a file called 'shopping_list.txt'.
# hint: use 'w' mode to overwrite the file each time with the current list
# hint: don't forget \n for new lines

# Step 5: create the main program loop with a small menu system which lets the user:
# - Call the functions to add or remove items.
# - After each action, write the updated shopping list to 'shopping_list.txt'.
# - Add a way of exiting the program
# hint: use a while loop with a menu and user choice
shopping_list=[]
def add_item():
    item=input("Enter the item to add:")
    shopping_list.append(item)
def remove_item():
    item=input("Enter the item to remove:")
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        print(f"{item} not found in the shopping list.")
def write_list_to_file():
    with open('shopping_list.txt','w') as outfile:
        for item in shopping_list:
            outfile.write(f"{item}\n")
while True:
    print("Menu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. Exit")
    choice=input("Enter your choice (1-3):")
    if choice=='1':
        add_item()
        write_list_to_file()
    elif choice=='2':
        remove_item()
        write_list_to_file()
    elif choice=='3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")