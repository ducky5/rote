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

# empty set
new_set.clear()
print(new_set)

print("-------------------------------------------------------")

new_set = {1, 2, 3, 4, 5, 6}

# remove arbitrary element and return it
print(new_set.pop())

print(new_set)

print("-------------------------------------------------------")

# union of two sets with no duplication
set_1 = {2, 4, 8, 5, 1}
set_2 = {0, 3, 1, 7, 6, 5}

print(set_1, set_2)

print()

u = set_2.union(set_1)

print(u)

print()

# intersection of two sets(the common elements)

i = set_1.intersection(set_2)

print(i)

print()

# what is in set_1 but not in set_2?
diff = set_1.difference(set_2)

print(diff)

print()

# all non mutual elements

sym_diff = set_2.symmetric_difference(set_1)

print(sym_diff)

# update set(argument must be iterable)
sym_diff.update({1, 59})

print(sym_diff)

print()

# keeps only intersection elements
set_1.intersection_update(set_2)

print(set_1)

# keeps only what's in sym_diff but not in set_2
sym_diff.difference_update(set_2)

print(sym_diff)

print()

# keeps only non mutual elements in set_1
set_1 = {1, 2, 3, 4}
set_2 = {1, 2, 3, 4, 5, 6}

set_1.symmetric_difference_update(set_2)

print(set_1)
