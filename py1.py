def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    else:
        return f"The result is {result}"

# Example usage
numerator = 10
denominator = 0

print(divide_numbers(numerator, denominator))
