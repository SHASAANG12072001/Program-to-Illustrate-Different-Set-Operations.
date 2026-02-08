# Define two sets
E = {0, 2, 4, 6, 8}
N = {1, 2, 3, 4, 5}

# Perform set operations
union_set = E.union(N)
intersection_set = E.intersection(N)
difference_set = E.difference(N)
symmetric_difference_set = E.symmetric_difference(N)

# Display results
print("Union of E and N is", union_set)
print("Intersection of E and N is", intersection_set)
print("Difference of E and N is", difference_set)
print("Symmetric difference of E and N is", symmetric_difference_set)

OUTPUT :
Union of E and N is {0, 1, 2, 3, 4, 5, 6, 8}
Intersection of E and N is {2, 4}
Difference of E and N is {0, 8, 6}
Symmetric difference of E and N is {0, 1, 3, 5, 6, 8}
