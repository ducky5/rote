from itertools import product, permutations, combinations, \
combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator

# lists all combinations(I'm unsure about this section)
a = [0, 1]
b = [3, 7]

prod = product(a, b, repeat=2)

print(list(prod))

print("-------------------------------------------------------")

# lists all possible permutations
a = [0, 1, 2]

# permutations(iterable, elements per permutation(from left))
perm = permutations(a, 2)

print(list(perm))

print("-------------------------------------------------------")

# lists all combinations
b = [1, 2, 3, 4]

comb = combinations(b, 2)

print(list(comb))

print()

# with repeating elements as well
comb_wr = combinations_with_replacement(b, 2)

print(list(comb_wr))

print("-------------------------------------------------------")

# compute accumulated operations

# default is addition
acc = accumulate(b)

print(b)
print(list(acc))

print()

# for multiplication
acc = accumulate(b, func=operator.mul)

print(b)
print(list(acc))

print()

# always append the list's max number
c = [1, 2, 3, 8, 4, 5]
acc = accumulate(c, func=max)

print(c)
print(list(acc))

print("-------------------------------------------------------")

def is_even(x):
    return x % 2 == 0

# group by
list_of_numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8]

group_obj = groupby(list_of_numbers, key=is_even)

for key, value in group_obj:
    print(key, list(value))

print("-------------------------------------------------------")

# infinite loop with the count function
for i in count(5):
    print(i)
    if i == 10:
        break

print("-------------------------------------------------------")

# cycle infinitely through iterable

for i in cycle(list_of_numbers):
    print(i)
    if i == i:
        break

print("-------------------------------------------------------")

# repeat something infinitely: repeat(to-repeat, how-many-times)
for i in repeat('infinity', 3):
    print(i)
