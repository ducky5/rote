# using pathlib is better than the usual open() etc...(pythonic)
import pathlib

file_path = pathlib.Path('human.txt')

# the with statement ensures that setup and teardown is always done
# it is used for resource management
with file_path.open('w') as file: # open file in write mode
    file.write('Hello, Human!')

# writing a custom context manager

# class based context manager
class prev_next_years:
    def __init__(self, year):
        self.year = year
    def __enter__(self): # setup
        print(f'previous year: {self.year-1}')
        return f'current year: {self.year}'
    # teardown
    def __exit__(self, *args, **kwargs): # *args, **kwargs can be used when you can't remember exc_type, exc_value, exc_tb
        print(f'next year: {self.year+1}')
        print(*args, **kwargs, sep='\n\n')

print('------------------------------------------------------------------------')
print('Class-based context manager, no errors', end='\n'*2)
# this with block does not produce an error
with prev_next_years(2022) as session:
    print(session)

# class based context manager with exception handling
class prev_next_years_exc(prev_next_years):
    def __exit__(self, exc_type, exc_value, exc_tb):
        print(f'next year: {self.year+1}')
        if isinstance(exc_value, IndexError):
            print(f'Exception occured in your with block: {exc_type}')
            print(f'Exception message: {exc_value}')
            return True # makes it possible for the program to continue executing past the with block(False or not returning makes the program stop)
        return False # this line will execute if there was no IndexError, always good to be explicit

print('------------------------------------------------------------------------')
print('Class-based(derived) context manager, exception handling', end='\n'*2)

with prev_next_years_exc(2022) as session:
    print(session)
    session[100]

print('------------------------------------------------------------------------')
print('Class-based context manager, errors shown but not handled', end='\n'*2)

# this one does produce an error
with prev_next_years(2022) as session: # sessions holds the return value of __enter__
    print(session)
    session[100] # this line produces an exception, that exception is shown by the .__exit__ method, if there are any errors then they are shown as indicated, otherwise it returns None
# the following line will not execute because the previous with block produces but does not handle exceptions
print('A'*100)
