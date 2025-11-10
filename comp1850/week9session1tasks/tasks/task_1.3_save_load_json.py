"""
Task 1.3: Saving and Loading JSON Files

Goal: Learn to save JSON data to a file and load it back.
"""

import json

# Data to save
data = {
    "userId": 102,
    "name": "Bob Brown",
    "email": "bob.brown@example.co.uk",
    "isActive": True
}

# TODO: Save the data to a file named "user.json" using json.dump()
with open("user.json", "w") as json_file:
    json.dump(data, json_file)
# TODO: Load the data back from "user.json" using json.load() and print it
with open("user.json", "r") as json_file:
    loaded_data = json.load(json_file)
    print(loaded_data)