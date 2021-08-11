from timeit import default_timer as timer

# NOTE:
    ### STRINGS ARE IMMUTABLE

string = "I am a string."
string_length = len(string) # store length of string in variable
print("string length:", string_length)

# convert string to lowercase
print("Lowercase:", string.lower())

# convert string to uppercase
print("Uppercase: ", string.upper())

# check if string is uppercase
print(f"is ({string}) uppercase?:", string.isupper())

# check if string is lowercase
print(f"is ({string}) lowercase?:", string.islower())

# return index of character
print("index(\"I\") =", string.index("I"))

# replace list of characters
print(string.replace("I am", "You are"))

print()

print(string)

print("-------------------------------------------------------")

# every second character
print('Hello there'[::2])

print()

# reverse string via negative optional step in slicing
print(string[::-1])

print("-------------------------------------------------------")

# removes whitespaces from beginning and end of string
string = '          Hi there        '
stripped_string = string.strip()
print(string, '\n', stripped_string)

print("-------------------------------------------------------")

# check if string starts with a certain character(s)
print(stripped_string.startswith('Hi'))

print()

# ends with something
print(stripped_string.endswith('there'))

print()

# find the start-index of string(returns -1 if non are found)
print(stripped_string.find('i'))

print("-------------------------------------------------------")

# count occurences
print(stripped_string.count('e'))

print()

# replace substring or character
print(string.replace(' ', '-'))

print("-------------------------------------------------------")

# split string and place each word as element in list(default limiter is space)
new_list = stripped_string.split()
print(new_list)

print()

# make list back into a string
new_string = ' '.join(new_list)
print(new_string)

print("-------------------------------------------------------")

# time comparison of for loop against .join()
a_list = ['a'] *1000000

# for loop method
start = timer()
a_string = ''
for i in a_list:
    a_string += i
stop = timer()

print(stop-start, 'for loop')

# the join() method
start = timer()
cleaner_method = ''.join(a_list)
stop = timer()

print(stop-start, 'join method')

# conclusion: the join method is much faster and an elegant one liner
