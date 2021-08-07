# NOTE:
    ### DICTIONARIES ARE MUTABLE
    ### DICTS ONLY SUPPORT IMMUTABLE KEYS 

# dictionary creation
wealth = {
    "Emma": 123234,
    "Karen": 21002,
    "Davis": 221023,
    "Jimmy": 2222222
}
print(wealth)
# access ditionary data(no default value: returns error if key is not found)
print(wealth["Jimmy"])
# access dictionary data(default value: returns default value if key not found)
# default value is None if not specified
print(wealth.get("foreign-item"))
# default value is specified
print(wealth.get("foreign-item", "Not Found!"))

print("-------------------------------------------------------")


# using the dict function to create a dictionary
new_dict = dict(name="Yassir", age=18, gender="male")

print(new_dict)

# change an value in dict
new_dict['name'] = "Eeya"
new_dict['gender'] = "female"
new_dict['age'] = 17

print(new_dict)

# create new key/value pair
new_dict['nationality'] = 'moroccan'

print(new_dict)

print("-------------------------------------------------------")

# delete key/value pair from dict
del new_dict['nationality']

print(new_dict)

# another way to delete key/value pair
new_dict.pop('name')
print(new_dict)

# remove the last key/value pair
new_dict.popitem()
print(new_dict)

print("-------------------------------------------------------")
new_dict = dict(item='computer', price=899.99)

# loop through the keys in dict
for key in new_dict:
    print(key)

print()

# same thing
for key in new_dict.keys():
    print(key)

print()

# loop through the values in dict
for value in new_dict.values():
    print(value)

print()

# loop through both
for key, value in new_dict.items():
    print(key, value)

print("-------------------------------------------------------")

# make dict copy
dict_copy = new_dict.copy()
dict_copy['is_good'] = True
print(dict_copy, new_dict)

print()

# another way is
dict_copy = dict(new_dict)
dict_copy['is_bad'] = False
print(dict_copy, new_dict)

print("-------------------------------------------------------")

# merge two dicts(original dict is overwritten)
dict_1 = dict(username='m4si', password='haha2', ip='0.0.0.0')
dict_2 = dict(username='m5si', password=None, ip=None)

dict_1.update(dict_2)
print(dict_1)
