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
