my_list = [1, 2, 3]

try:
    print(my_list[5])  # Trying to access an invalid index
except IndexError:
    print("IndexError: That index does not exist.")
