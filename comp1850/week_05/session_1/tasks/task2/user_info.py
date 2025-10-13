# Step 1: Prompt the user for their name, age, and favorite color.

# Step 2: Open a file called 'user_info.txt'

# Step 3: Write each piece of information to the file, each on a new line.

# hint: think about what mode to open in!
# hint: remember to add \n for new lines when writing to files
# hint: if you want multiple people to add info without overwriting, consider append mode 'a'

# you could extend this by using a loop to allow multiple people to enter their info in a row
name = input("Enter your name: ")
age = input("Enter your age: ")
favorite_color = input("Enter your favorite color: ")
with open('user info.txt', 'r') as infile:
    if infile.isalpha():
        with open('user info.txt', 'a') as outfile:
            outfile.writelines(["{name}\n", "{age}\n", "{favorite_color}\n"])
    else:
         with open('ueser info.txt', 'w') as outfile:
             outfile.writelines(["name\n", "age\n", "favorite_color\n"])