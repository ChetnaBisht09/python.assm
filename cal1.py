# cal1.py

def add1(x, y):
    return x + y

def mul1(x, y):
    return x * y

def div1(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def mod1(x, y):
    return x % y

def pow1(x, y):
    return x ** y
