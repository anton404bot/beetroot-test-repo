import glob
import os

def count_lines(path):
    try:
        return f'\nThis file has {sum(1 for line in open(path))} lines.\n'
    except UnicodeDecodeError:
        print('I\'m ready only for text files (')

def count_chars(path):
    f = open(path, 'rb')
    return len(f.read())
    '''try:
        for line in open(path, 'r'):
            chars += 
            return f'\nThis file has {chars} characters.\n'
    except UnicodeDecodeError:
        print('I\'m ready only for text files (')'''

def test(name):
    'both'
    pass