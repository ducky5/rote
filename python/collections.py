from collections import Counter, namedtuple, defaultdict, deque

# create dictionary with keys as the characters and the values as the number
# of occurences(any iterable can be used)
string = 'hahahaheheheiiii'

counter = Counter(string)

print(counter)

print()

# most common character(here only shows the 1st most common)
print(counter.most_common(1))

print()

# see all the elements
print(list(counter.elements()))

print("-------------------------------------------------------")

# make a tuple class using namedtuple
Point = namedtuple('Point', 'x, y, z')

pt = Point(1, 2, -5)

print(pt)

print("-------------------------------------------------------")

def callable_function():
    return 'called'

# have a default return value
d = defaultdict(callable_function) # any callable as argument

print(d['a'])

print("-------------------------------------------------------")

# a double-ended queue, elements can be added/removed from either ends
d = deque()

# add elements
d.append(1)
d.append(2)
d.append(3)
d.appendleft(0)

print(d)

print()

# extend deque
d.extend([9, 8, 7])

d.extendleft([900, 10])

print()

# remove elements
d.pop()
print(d)

d.popleft()

print(d)

print()

# rotate deque
# rotate elements to the right(positive integer) n places
d.rotate(3)
print(d)

print()

# rotate elements to the left(negative integer) n places
d.rotate(-3)
print(d)

print()

# clear the deque
d.clear()
print(d)
