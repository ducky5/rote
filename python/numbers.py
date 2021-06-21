from math import *

number = -5

# str() converts to string
print("Number " + str(number))

# print absolute value
print("absolute value of", number, " is:", abs(number))

# pow(n, j): raise n to the power of j
print(f"{number} to the power of 2 is", pow(number, 2))

# return the highest number
print(max(4, 2, 5))

# return the lowest number
print(min(4, 2, number))

# round number: round(number, wanted digits after decimal point)
print(round(78.23495464, 2))

# returns highest integer less than or equal to argument
print(floor(2.2))

# rounds the number up
print(ceil(2.2))

# return the square root of a number
print(sqrt(1))
