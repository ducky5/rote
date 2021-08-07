# NOTE:
    ##### LISTS ALLOW DUPLICATIONS

# list creation
even = [2, 2, 4, 6, 8, 10]
odd = [3, 5, 7, 9, 11]
continents = ["Africa", "Asia", "Australia", "Europe"]
# length of list
print(len(continents))
# last element is index -1
print("last element in even is:", even[-1])
# from here(inclusive):to here(exclusive)
print(even[1:2]) # print 2
print(even[2:]) # print the rest of elements from index 2(inclusive)
# merge two lists
even.extend(odd)
print(even, odd)
# append list
even.append("even and odd")
print(even)
# insert element into list: list.insert(INDEX, ELEMENT)
odd.insert(0, 1)
print(odd)
# remove element from list
odd.remove(11)
print(odd)
# clear list(remove all elements from it)
odd.clear()
print(odd)
# remove last element in list
even.pop()
print(even)
# print index of element
print(even.index(4))
# count number of occurences in list
print(even.count(2))
# sort list in ascending order
even.sort()
print(even)
# reverse list
continents.reverse()
print(continents)
# create a list copy
locations = continents.copy()
print(locations)

print("-------------------------------------------------------")
# create empty list
new_list = list()
new_list.append(0)
print(new_list)
print("-------------------------------------------------------")
# insert at specific index
new_list.insert(0, 2)
print(new_list)
print("-------------------------------------------------------")
# pop an item off the list but save the removed item to another variable
popped_item = new_list.pop()
print(popped_item)
print(new_list)
print("-------------------------------------------------------")
# operate on list without changing original list
numbers = [3, 300, 99, 3, -2, -3, -5, 1]
sorted = sorted(numbers)

print(numbers, sorted)
print("-------------------------------------------------------")
# create list with many equal items
names = ['Yassir'] * 2
print(names)
print("-------------------------------------------------------")
# concatenate lists
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]

print(list_1 + list_2 + list_3)

# save it to a variable and adding another list
concatenated = list_1 + list_2 + list_3 + [10]
print(concatenated)

# access parts of list
print(concatenated[2:3])

# start from beginning of list
print(concatenated[:3])

# goes all the way to the end
print(concatenated[2:])

# step length(my own way of describing it), the :: is the step length operator
print(concatenated[2::5])

# a trick to reverse list
print(concatenated[::-1])

print("-------------------------------------------------------")

# another way to make a copy of list
copy = list(concatenated)
copy.append(11)

print(copy, concatenated)

# another is slicing
copy = concatenated[:]
copy.append(12)

print(copy, concatenated)

print("-------------------------------------------------------")

# list comprehension
numbers = [1, 2, 3, 4, 5]
squared_version = [num*num for num in numbers]

print(numbers, squared_version)
