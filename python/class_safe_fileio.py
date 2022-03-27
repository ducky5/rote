import pathlib

class FileHandler:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
    def __enter__(self): #setup
        print(f'\nopening file (mode={self.mode})...')
        self.file_obj = pathlib.Path(self.file_path).open(mode=self.mode)
        print('file opened.')
        return self.file_obj
    def __exit__(self, *args, **kwargs): #teardown
        if self.file_obj:
            print('closing file...')
            self.file_obj.close()
            print('file closed.')

#
with FileHandler('./data/write_file.txt', 'w') as file:
    file.write(input('write to file: '))

#
with FileHandler('./data/write_file.txt', 'r') as file:
    if file.readable():
        # came up with this trick on my own :)
        print(file.read().join(['"']*2)) # using the join() feature to surround text with double quotes
