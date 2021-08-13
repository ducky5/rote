x = 0

# raise an exception
if x < 0:
    raise Exception('x should be positive')

print("-------------------------------------------------------")

# assert a rule(error-text not required)
# syntax: assert condition, message
assert (x<=0), 'x should be negative or 0'

print("-------------------------------------------------------")

# catching errors and making exceptions
try:
    y = x / 0
except ZeroDivisionError as e:
    print('error:', e)

print("-------------------------------------------------------")

# catch multiple errors, only one error is caught(the first one to err)
try:
    kdkfjdkfjfk
    y = x + ''
except NameError as e:
    print('error:', e)
except TypeError as e:
    print('error:', e)

print("-------------------------------------------------------")

# with else statement if no errors are detected
try:
    x += 1
except ValueError:
    print('error')
except ZeroDivisionError:
    print('error')
except TypeError:
    print('error')
else:
    print('no errors were found!')
finally: # used for cleaning up(closing files, releasing resources)
    print('cleaning up...')

print("-------------------------------------------------------")

# in a function because return cannot be used in global scope
def before_return():
    try:
        jjfdkfjdkf
    except NameError as e:
        print('error:', e)
        return None
    finally: # this clause runs before the return statement above... useful!
        print('runs before return!')

before_return()

print("-------------------------------------------------------")

# create custom Error class derived from base class
class NotAnIntegerError(Exception):
    pass

def get_int(x):
    if not isinstance(x, int): # isinstance(value, type)
        raise NotAnIntegerError('Not an integer')

try:
    get_int('')
except NotAnIntegerError as e:
    print('custom error:', e)

print("-------------------------------------------------------")

# create custom Error class but with more than pass in it
class ValueNotAStringError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def get_str(x):
    if not isinstance(x, str):
        raise ValueNotAStringError('value is not a string', x)

try:
    get_str(2)
except ValueNotAStringError as e:
    print('custom error:', e.message)
    print('     value:', e.value)
