#Simple calculator app

def get_numbers():
    #Returns a tuple of numbers
    a = input("Please give me a number:\t")
    b = input("And one more number:\t")
    return (a,b)

def add_numbers(a,b):
    return a+b

def subtract_numbers(a,b):
    return a-b

def multiply_numbers(a,b):
    return a*b

def divide_numbers(a,b):
    if b==0:
        print("Cannot divide by zero.")
        return 0
    return a/b