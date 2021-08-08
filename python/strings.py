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

# reverse string via negative optional step in slicing
print(string[::-1])
