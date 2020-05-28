print("\nTask 1")

def oops():
    raise IndexError

def ooops():
    try:
        oops()
    except:
        return("Здесь ошибка по индексам.")
        raise IndexError

print(ooops())



print("\nTask 2")

stripzero = lambda x: (x).rstrip("0").rstrip(".")

def check(a, b):
    try:
        a = float(a)
        b = float(b)
        a**2/b
    except ValueError:
        return print("Вводить можно только числа!")
    except ZeroDivisionError:
        return print("Делить на ноль не лучшая затея!")
    else:
        return print (stripzero(f'{a}'), stripzero(f'** {2}'), stripzero(f' / {b}'), stripzero(f' = {a**2/b}'))


while True:
    print("\nЧтобы остановить программу, введи 'break'")
    a = input("\nВведи первое число: ")
    if a == "break":
        break
    b = input("Введи второе число: ")
    if b == "break":
        break
    check(a, b)
