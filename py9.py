def error_handler():
    try:
        result = 10 / 0  
        my_list = [1, 2, 3]
        print(my_list[5])  
        my_dict = {'key': 'value'}
        print(my_dict['nonexistent_key']) 
    except ZeroDivisionError as e:
        print(f"Error: Division by zero is not allowed. Details: {e}")
    except IndexError as e:
        print(f"Error: List index out of range. Details: {e}")
    except KeyError as e:
        print(f"Error: Key not found in dictionary. Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred. Details: {e}")


error_handler()

