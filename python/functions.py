# map(func, iterable) standardlib function
# applies func to each item in the iterable

# square numbers
squared_numbers = map(lambda x: x ** 2, range(10))
print(list(squared_numbers)) # list() because map() returns an object

# add two lists
# the way it works: 1 + 4 then 2 + 5 then 3 + 9 -> [5, 7, 9]
list_sum = map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])
print(list(list_sum))

# filter(func, iterable) standardlib function
# filters out the iterable using func

# filter out odd numbers
even_numbers = filter(lambda x: x % 2 == 0, range(11))
print(list(even_numbers))

# reduce(func, iterable, initializer optional) standardlib function (needs to be imported)
# reduces iterable to single value
from functools import reduce

# sum all numbers in the list
sum_all_lists = reduce(lambda x, y: x + y, [1, 2, 3])
print(sum_all_lists, end='')

# equivalent to the sum() function from standardlib
print('<=>' + str(sum([1, 2, 3])))

# with initializer

sum_all_lists_and_200 = reduce(lambda x, y: x + y, [1, 2, 3], 200)
print(sum_all_lists_and_200, end='')

# equivalent to the sum() function again
print('<=>' + str(sum([1, 2, 3]) + 200))
