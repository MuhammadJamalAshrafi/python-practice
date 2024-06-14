import json
import os

# convert dictionary to json
book_dict = {
    "tom": {"name": "tom", "address": "1 green street, NY", "phone": 23456},
    "john": {"name": "john", "address": "2 blue street, CA"},
}

book_json = json.dumps(book_dict)
print(book_json)


# convert json to dictionary

person_json = '{"name": "Bob", "languages": ["English", "French"]}'
person_dict = json.loads(person_json)
print(person_dict)
print(person_dict["languages"])


# writing json to a file

person_dict = {
    "name": "Bob",
    "languages": ["English", "French"],
    "married": True,
    "age": 32,
}

# Define the directory and file path
directory = "files"
file_path = os.path.join(directory, "person.txt")

# Create the json directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Write the json data to the file
with open(file_path, "w") as json_file:
    json.dump(person_dict, json_file)


# Python read json file

with open(file_path, "r") as json_file:
    person_dict = json.load(json_file)
    print(person_dict)
