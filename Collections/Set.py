set1 = {2, 3, 5, 4, 6, 8, 9}
set2 = {1, 3, 6, 7, 10, 9, 11}

print(f"This is set1: {set1}")
print(f"This is set 2: {set2}")

print()

# Union of the two sets
union = set1.union(set2)
print(f"The union of the two sets is: {union}")

print()

# Intersection of the sets
intersection = set1.intersection(set2)
print(f"The intersection of the two sets is: {intersection}")

print()

# Symmetric difference (deletes the values present in both sets)
s_diff = set1.symmetric_difference(set2)
print(f"The Symmetric difference of the two sets is: {s_diff}")

print()

# Difference ()
diff = set1.difference(set2)
print(f"The difference of the two sets is: {diff}")