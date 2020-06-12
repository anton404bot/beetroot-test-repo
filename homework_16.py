'''
Task 1

Create your own implementation of a built-in function enumerate, 
named `with_index`, which takes two parameters: `iterable` and `self.start`, 
default is 0. Tips: see the documentation for the enumerate function
'''

import random

print('\nTASK1')

class With_index:
    def __init__(self, iterable, start=0):
        self.iterable = iterable
        self.start = start
    
    def __str__(self):
        result = ''
        for i in range(len(self.iterable[self.start:])):
            result += (f'\n{i} {self.iterable[i]}')
        return result
        
    def __repr__(self):
        result = ''
        for i in range(len(self.iterable[self.start:])):
             result += (f'\n{i} {self.iterable[i]}')
        return result   


indexation = With_index([random.randint(1, 99) for i in range(random.randint(4, 14))], random.randint(0, 8))
print(indexation)

'''
Task 2

Create your own implementation of a built-in function range, 
named in_range(), which takes three parameters: `start`, `end`, 
and optional step. Tips: See the documentation for `range` function
'''
print('\nTASK2')

class In_range:

    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        self.num = self.start
        return self
    
    def __next__(self):
        if (self.num >= self.end):
            raise StopIteration
        self.num += self.step
        return self.num


in_range = In_range(1, 11, 1)

print_range_iter = iter(in_range)
print(in_range.start)
while True:
    next_iter = next(print_range_iter)
    if next_iter >= in_range.end:
        break
    else:
        print (next_iter)
    



'''
Task 3

Create your own implementation of an iterable, 
which could be used inside for-in loop. 
Also, add logic for retrieving elements using square brackets syntax.
'''

print('\nTASK3')
    
class Iterable:
    def __init__(self, iterable):
        self.__iter = iterable
    
    def __iter__(self):
        return iter(self.__iter)

    def __getitem__(self, index):
        return self.__iter[index]

simple = Iterable([x for x in range(random.randint(9, 11))])

for item in simple:
    print(item)
        
    