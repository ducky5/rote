import sys, timeit
# tuple creation, tuples are immutable(the parenthesis aren't necessary)
meta_data = ("male", "18")
print(meta_data)

# following is so that the one item long tuple is recognized as a tuple
data = (1,)
print(type(data))

print("-------------------------------------------------------")

# create tuple from iterable
data = tuple('iterable')
print(data, type(data))

print(data[0:4])

# count elements
print(data.count('e'))

# find index of element
print(data[data.index('r'):].index('e'))

print("-------------------------------------------------------")

# convert tuple to list(can work vice versa)
data = list(data)

print(data)

print("-------------------------------------------------------")
data = ('Yassir', 18)
# unpacking(same number of variables as number of elements in iterable)
name, age = data

print(data, name, age)

# using the star operator for unpacking multiple elements
data = (1, 2, 3, 4, 5, 6)

i, *i2 = data # i gets the first element in iterable, then i2 gets the rest

print(data, i, i2)

print("-------------------------------------------------------")

# size in memory comparison of tuple and list

list = [1, 2, 3, 4, 5]
tuple = (1, 2, 3, 4, 5)


print(f'size of tuple: {tuple}', sys.getsizeof(tuple))
print(f'size of list: {list}', sys.getsizeof(list))

print("-------------------------------------------------------")

print(timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000))
