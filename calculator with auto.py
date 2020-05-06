import random 
from datetime import timedelta, datetime
import calc_funcs

stripzero = lambda x: (x).rstrip('0').rstrip('.')
striptuple = lambda x: (x).replace(",", "").replace("(", "").replace(")", "").replace("'", "")

name = (input("\n\n\n\nПривет! Давай познакомимся. Как тебя зовут? \nВведи, пожалуйста, своё имя сюда: ").capitalize())
print('\nОчень приятно, ', name, '. Меня зовут Калькулятор. Давай посчитаем что-то.')
print("""
      Для начала тебе следует выбрать одну из следующих операций:
      1: Сложение
      2: Вычитание
      3: Умножение
      4: Деление
      5: Целочисленное деление
      6: Степень числа
      7: Остаток от деления
      8: Факториал
      9: Революционер
      10: Дата и время смерти""")
print("Выбрал?")

while True:
    operation = (input("""\nТы можешь написать:
    0, чтобы попрощаться с калькулятором;
    Название операции, или её номер, чтобы произвести оную;
    Ну и просто ввести выражение, а я попробую решить его сходу.  \n\n""").lower().strip())
    if operation == "0": 
        print(f'Рад был тебя видеть, {name}!') 
        break

    if "-" in operation or "+" in operation or "/" in operation or "*" in operation:
        end = ""
        for j in operation:
            if j in ("-", "+", "*", ".", "/", "%"):
                end += str(j)
            elif j.isdigit() == True:
                end += str(j)
            elif j.isalpha() == True:
                continue
            elif j == " ":
                continue
        if end == "":
            print("Цифр нет:(")   
        else:
            result = str(calc_funcs.auto(end))
            result = striptuple(result)
            print (result)

    elif operation in ("сложение", "вычитание", "умножение", "деление", "целочисленное деление", "остаток от деления", "1", "2", "3", "4", "5", "7"):
        result = None
        while result == None:
            num1 = (input("Введи первое число: ")) 
            num1_bez_tochki = num1.replace(".", "", 1)
            if num1_bez_tochki.isdigit() == False:
                print("Пожалуйста, я же калькулятор и воспринимаю только цифры: ")
            else:
                num1_part = num1.split('.')
                if len(num1_part) == 2 and num1_part[0].isdigit() and num1_part[1].isdigit():
                    num1 = float(num1)
                else:                     
                    num1 = float(num1)    
                while result == None:
                    num2 = (input("Введи второе число: "))
                    num2_bez_tochki = num2.replace(".", "", 1)
                    if num2_bez_tochki.isdigit() == False:
                        print("Пожалуйста, я же калькулятор, напиши цифрами: ") 
                    else:
                        num2_part = num2.split('.')
                        if len(num2_part) == 2 and num2_part[0].isdigit() and num2_part[1].isdigit():
                            num2 = float(num2)      
                        else:                       
                            num2 = float(num2)      
                        
                        if operation == "сложение" or operation == "1".strip().rstrip(":"):
                            print(stripzero(f'{num1}'),stripzero(f'+ {num2}'),stripzero(f'= {num1 + num2}'))
                            result = (f'{num1 + num2}') 
                        
                        elif operation == "вычитание" or operation == "2".strip().rstrip(":"):
                            print(stripzero(f'{num1}'),stripzero(f'- {num2}'),stripzero(f'= {num1 - num2}'))
                            result = (f'{num1 - num2}')
                            
                        elif operation == "умножение" or operation == "3".strip().rstrip(":"):
                            print(stripzero(f'{num1}'),stripzero(f'* {num2}'),stripzero(f'= {num1 * num2}'))
                            result = (f'{num1 * num2}')
                            
                        elif operation == "деление" or operation =="4".strip().rstrip(":"):
                            if num2 != 0:
                                print(stripzero(f'{num1}'),stripzero(f'/ {num2}'),stripzero(f'= {num1 / num2}'))
                                result = (f'{num1 / num2}') 
                            else:
                                print("На ноль не делим!")
                                
                        elif operation == "целочисленное деление" or operation == "5".strip().rstrip(":"):
                            print(stripzero(f'{num1}'),stripzero(f'// {num2}'),stripzero(f'= {num1 / num2}'))
                            result = (f'{num1 // num2}')
    
                        elif operation == "остаток от деления" or operation == "7".strip().rstrip(":"):
                            print(stripzero(f'{num1}'),stripzero(f'% {num2}'),stripzero(f'= {num1 % num2}'))
                            result = (f'{num1 % num2}')
                           
    elif operation == ("степень числа").lower().strip() or operation == "6".strip().rstrip(":"):
        result = None
        while result == None:
            num1 = input("Введи число, которое будем возводить в степень: ")
            num1_bez_tochki = num1.replace(".", "", 1)
            if num1_bez_tochki.isdigit() == False:
                print("Пожалуйста, я же калькулятор, напиши цифрами: ")
            else:
                num1_part = num1.split(".")
                if len(num1_part) == 2 and num1_part[0].isdigit() and num1_part[1].isdigit():
                    num1 = float(num1)
                else:
                    num1 = float(num1)
                result = None
                while result == None:         
                    num2 = input("Введи число, собственно, степени: ")
                    num2_bez_tochki = num2.replace(".", "", 1)
                    if num2_bez_tochki.isdigit() == False:
                        print("Пожалуйста, я же калькулятор, напиши цифрами: ")
                    else:
                        num2_part = num2.split(".")
                        if len(num2_part) == 2 and num2_part[0].isdigit() and num2_part[1].isdigit():
                            num2 = float(num2)
                        else:
                            num2 = float(num2)
                        print(stripzero(f'{num1}'),stripzero(f'** {num2}'),stripzero(f'= {num1 ** num2}'))
                        result = (f'{num1 ** num2}')
                    
    elif operation == ("революционер").lower().strip() or operation == "9".strip().rstrip(":"):
            print(f'{name},ты революционер на ', random.randrange(0, 100),"%.")
            
    elif operation == ("факториал").lower().strip() or operation == "8".strip().rstrip(":"):
        result = None
        while result == None:
            num = input(f'Здесь уже всё проще, {name}. Введи число, факториал которого хочешь увидеть: ')
            num_bez_tochki = num.replace(".", "", 1)
            if num_bez_tochki.isdigit() == False:
                print("Не забывай, что я калькулятор и могу считать только числа: ")
            else:
                num_part = num.split(".")
                if len(num_part) == 2 and num_part[0].isdigit() and num[1].isdigit():
                    num1 = float(num)
                else:
                    num1 = float(num)
                factorial = 1
                while num1 > 1:
                    factorial *= num1
                    num1 -= 1
                print(stripzero(f'\nФакториал числа {num}'),stripzero(f' =  {factorial}'))
                result = factorial
                
    elif operation == ("дата и время смерти").lower().strip() or operation == "10".strip().rstrip(":"):
        min_year = datetime.now().year
        max_year = (min_year + 111)
        start = datetime(min_year, 1, 1, 00, 00, 00)
        years = max_year - min_year+1
        end = start + timedelta(days=365 * years)
        for i in range(1):
            random_date = start + (end - start) * random.random()
            print(random_date.strftime("%d-%m-%Y   %H:%M:%S"))

            left = (f'В таком случае тебе осталось {(random_date - start)/365} years').replace("days", "лет/года").replace(",",".")
            print(left[:-22])
        
    else:
        print("\nТаких операций я не знаю :(")
        
    