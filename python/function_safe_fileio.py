from contextlib import contextmanager
import pathlib

@contextmanager
def fileHandler(file_path, mode):
    print(f'\nopening file (mode={mode})...')
    file_obj = pathlib.Path(file_path).open(mode=mode)
    print(f'file {file_obj.name} opened.')
    try:
        yield file_obj
    finally:
        if file_obj:
            print(f'closing file...')
            file_obj.close()
            print(f'file {file_obj.name} closed.')

#
with fileHandler('./data/write_filev2.txt', 'w') as file:
    file.write('A'*99999999)

with fileHandler('./data/write_filev2.txt', 'r') as file:
    if file.readable():
        # print(file.read().join(['"']*2))
        pass
