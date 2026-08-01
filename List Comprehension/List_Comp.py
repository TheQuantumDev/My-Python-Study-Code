# List Comprehension = A concise way to make list in python
#                      compact and easy to read than traditional loops
# syntax = [expression for value in iterable if condition]

# Traditional loop style
doubles = []

for i in range(1, 11):
    doubles.append(i * 2)

print(doubles)

# List Comprehension style
triples = [i * 3 for i in range(1, 11)]
print(triples)

# Working with the condition
nums = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in nums if num >= 0]
negative_nums = [num for num in nums if num < 0]

print(positive_nums)
print(negative_nums)