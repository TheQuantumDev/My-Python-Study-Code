# *args = allows u to pass multiple non-key arguments, they are tuples in nature
# **kwargs = allows u to pass multiple keywords arguments, they are dicts in nature
# * = unpacking operator

def sum(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(sum(1, 2, 3, 4, 5))

def show_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_address(
    street="46B Old Odukpani",
    city="Calabar Municipality", 
    state="CrossRiver",
    country="Nigeria", 
)