import timeit
from functools import reduce

# lambda parameters: expression

multiply = lambda x,y: x * y

print(multiply(2, 2))

print("-------------------------------------------------------")

# usage of lambda functions for sorting a list of tuples
points = [(1, 2), (-1, 3), (5, -5), (10, 0)]

# NOTE: the key parameter accepts any function as argument and not just lambda
points_sorted = sorted(points, key=lambda x: x[0] + x[1])

print(points)
print(points_sorted)

print("-------------------------------------------------------")

# using lambda function for mapping an iterable with the map() function

# this lambda function returns a tuple
points_doubled_iterator = map(lambda x: (x[0]*2, x[1]*2), points)

print(list(points_doubled_iterator))

print()

# here is the same result using list comprehension instead
# this one is better because the converting step is not necessary since it's
# already a list
points_doubled_via_list_comprehension = [(x[0]*2, x[1]*2) for x in points]

print(points_doubled_via_list_comprehension)

print("-------------------------------------------------------")

# the filter() function and lambda
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))

# using list comps

even_numbers_list_comprehension = [i for i in numbers if i % 2 == 0]

print(even_numbers_list_comprehension)

print("-------------------------------------------------------")

# the reduce() function and lambda

sum_of_numbers = reduce(lambda x,y: x+y, numbers)
print(sum_of_numbers)

print("-------------------------------------------------------")

# map() vs LIST comprehension (speed comparison)

print('map():', timeit.timeit(stmt='map(lambda x: (x[0]*2, x[1]*2), \
[(1, 2), (-1, 3), (5, -5), (10, 0)])', number=1000000))

print('list comps:', timeit.timeit(stmt='[(x[0]*2, x[1]*2) for x in \
[(1, 2), (-1, 3), (5, -5), (10, 0)]]', number=1000000))

# CONCLUSION: list comps is slower

print("-------------------------------------------------------")

# filter() vs LIST comprehension (speed comparison)

print('filter():', timeit.timeit(stmt='filter(lambda x: x % 2 == 0, \
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])', number=1000000))
print('list comps:', timeit.timeit(stmt='[i for i in \
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] if i % 2 == 0]', number=1000000))

# CONCLUSION: list comps is slower
