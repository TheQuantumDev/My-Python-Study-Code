# A decorator is a function that extends the behavior of another 
# function without modifying that base function. We pass the base 
# function as an argument to the decorator

# This is creating a decorator that can accept arguments and 
# keyword arguments
def add_spread(func):
    def wrapper(*args, **kwargs):
        print("*You added a spread🧈*")
        func(*args, **kwargs)
    return wrapper

def add_fruit(func):
    def wrapper(*args, **kwargs):
        print("*You added a fruit🍒*")
        func(*args, **kwargs)
    return wrapper

@add_spread
@add_fruit
def get_bread(flavor):
    print(f"Here is your {flavor} bread🍞")

get_bread("banana")