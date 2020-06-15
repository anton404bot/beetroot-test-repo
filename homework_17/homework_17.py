print('\nTask 1')

'''Imports practice
Make a directory with 2 modules; 
make a function in one of them; 
then import this function in the other module 
and use that in your script of choice.'''

from for_import import get_largest as gl, convert_list 
import random
# get_largest returns the largest possible number from given nums
# convert_list converts list of generated numbers to one integer number

num = convert_list(random.randint(1, 9) for i in range(random.randint(6,9)))
print(gl(num))


print('\nTask 2')
 
'''The sys module.
The “sys.path” list is initialized from the PYTHONPATH environment variable. 
Is it possible to change it from within Python? 
If so, does it affect where Python looks for module files? 
Run some interactive tests to find it out.'''


print('\nTask 3')

import glob
import os
from mymod import count_lines, count_chars

def print_menu():
    print()
    print('1. Count lines')
    print('2. Count chars')
    print('0. Exit')
    print()

while True:
    command = input('Write 1 to find file or 0 to exit: ')
    if command == '1':
        search = input('Write filename: ')
        list_of_founds = (glob.glob(f'*{search}*'))
        if len(list_of_founds) > 1:
            print('You have to choose one from the list below: ')
            index = 0
            visual_list = ''
            l = []
            for i in list_of_founds:
                l.append({i : os.path.abspath(i)})
                visual_list += (f'\n{list_of_founds.index(i)+1}: {i} ({os.path.abspath(i)})')
            print(visual_list)

            choice = l[int(input('Write the num of the file you would like to work with: '))-1]
            filename = [*choice][0]
            filepath = choice.get(filename)
            print(f'\nYour choice - {filename}')
            print(f'It\'s ditectory - {choice.get(filename)}')

            print_menu()
            command = input('Write here num of your command: ')
            if command == '1':
                print(count_lines(filepath))
            elif command == '2':
                print(count_chars(filepath))
            elif command == '0':
                print('Bye!')
                break
        elif len(list_of_founds) == 1:
            print(f'\nLook What i have: \n{list_of_founds}')
            print_menu()
            filepath = os.path.abspath(list_of_founds[0])
            command = input('Write here num of your command: ')
            if command == '1':
                print(count_lines(filepath))
            elif command == '2':
                print(count_chars(filepath))
            elif command == '0':
                print('Bye!')
                break
        elif len(list_of_founds) < 1:
            print('I\'m not sure that such file exists on this computer at all (')
            pass
    elif command == '0':
        break    




