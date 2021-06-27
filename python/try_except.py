def divisionFunction(num1, num2):
    return num1 / num2

# try something, then catch the errors
# catches specific errors
try:
    num1 = input("num1: ")
    num2 = input("num2: ")
    print(divisionFunction(num1, num2))
except ZeroDivisionError as err:
    print(err)
except TypeError as err:
    print(err)
