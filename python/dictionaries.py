# dictionary creation
wealth = {
    "Emma": 123234,
    "Karen": 21002,
    "Davis": 221023,
    "Jimmy": 2222222
}
# access ditionary data(no default value: returns error if key is not found)
print(wealth["Jimmy"])
# access dictionary data(default value: returns default value if key not found)
# default value is None if not specified
print(wealth.get("foreign-item"))
# default value is specified
print(wealth.get("foreign-item", "Not Found!"))
