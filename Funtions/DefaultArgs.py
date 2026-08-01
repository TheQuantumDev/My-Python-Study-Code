# Default arguments are default values for a parameter. You can still override them
def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(1000))
print(net_price(1000, 0.1))
print(net_price(1000, 0.1, 0))