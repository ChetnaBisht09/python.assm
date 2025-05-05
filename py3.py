my_dict = {"name": "Frank", "age": 50}

try:
    print(my_dict["gender"])
except KeyError:
    print("Key 'gender' not found")
    my_dict["gender"] = "Not specified"
    print(my_dict["gender"])