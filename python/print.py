import time

SECONDS = .25
RANGE = 10
print('\033[? 25l', end='') #hide cursor

for i in range(RANGE):
    print(f'{int((i+1)/RANGE*100)}%\r', end='') # \r (carriage return) moves the cursor to the first position on the same line.
    time.sleep(SECONDS)

print('\x1b[2K', end='') #delete previous line.

for i in range(RANGE):
    print(f'{int((i+1)/RANGE*100)}%\r', end='') #setting flush to true completely disregards buffering and output is immediate
    time.sleep(SECONDS)


print('\033[? 25h', end='') #unhide cursor
