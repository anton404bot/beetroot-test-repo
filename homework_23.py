from typing import List, Tuple

import time
from functools import wraps

# We assume that all lists passed to functions are same length N
# answers
# 1 - n
# 2 - 1
# 3 - n^2
# 4 - n
# 5 - n^2
# 6 - log n

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        return func.__name__ + ': ' + (str(end - start)[:6] + ' seconds; ') + ' ' + str(result)
    return wrapper
    
 
@time_it    
def question1(first_list: List[int], second_list: List[int]):
    res: List[int] = []
    n_oper = 0
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
            n_oper += 1
    return f'operations: {n_oper}'


'''@time_it
def question2(n: int):
    oper_count = 0
	for _ in range(10):
		n **= 3
        oper_count += 1
	return oper_count

'''
@time_it
def question3(first_list: List[int], second_list: List[int]):
   temp: List[int] = first_list[:]
   n_oper = 0
   for el_second_list in second_list:
      flag = False
      for check in temp:
         if second_list == check:
            flag = True
            n_oper += 1
            break
      if not flag:
         temp.append(second_list)
         n_oper += 1
   return f'operations: {n_oper}'


@time_it
def question4(input_list: List[int]):
    n_oper = 0
    res: int = 0
    for el in input_list:
        if el > res:
            res = el
            n_oper += 1
    return f'operations: {n_oper}'


@time_it
def question5(n: int) -> List[Tuple[int, int]]:
    n_oper = 0
    res: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
            n_oper += 1
    return f'operations: {n_oper}'



@time_it
def question6(n: int):
    n_oper = 0
    while n > 1:
        n /= 2
        n_oper += 1
    return f'operations: {n_oper}'


range_1000 = [i for i in range (1000)]
range_5000 = [i for i in range (5000)]
range_10000 = [i for i in range (10000)]


print(question1(range_1000, range_1000))
print(question1(range_5000, range_5000))
print(question1(range_10000, range_10000))

print()
print(question3(range_1000, range_1000))
print(question3(range_5000, range_5000))
print(question3(range_10000, range_10000))

print()
print(question4(range_1000))
print(question4(range_5000))
print(question4(range_10000))

print()
print(question5(1000))
print(question5(5000))


print()
print(question6(1000))
print(question6(5000))
