# creating a set, does not allow duplicates(is mutable tho)
new_set = {1, 2, 3, 4, 1, 2, 3, 4}

print(new_set)

# another way to create a set(argument must be an iterable)
new_set = set('12341234')

print(new_set)

print("-------------------------------------------------------")

# create empty set
new_set = set()

# add elements
new_set.add(1)
new_set.add('Roger')

# remove elements(raises error if element does not exist)
new_set.remove(1)

# removes element if it exists(does not raise error if element does not exist)
new_set.discard('roger')

print(type(new_set), new_set)
