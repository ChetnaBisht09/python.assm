user_input = input("Enter a number: ")
try:
    number = int(user_input)
    print("You entered:", number)
except ValueError:
    print("ValueError: Please enter a valid number.")

