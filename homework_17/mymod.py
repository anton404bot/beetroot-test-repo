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
    
def test(path):
    f = open(path, 'rb')
    try:
        return f'\nThis file consists of {len(f.read())} characters \nand has {sum(1 for line in open(path))} lines.\n'
    except UnicodeDecodeError:
        print('I\'m ready only for text files (') 
        