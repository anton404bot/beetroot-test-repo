#TASK 1

class Person:
    def __init__(self, name, age, color_of_eyes, motherlanguage):
        self.name = name
        self.age = age
        self.color_of_eyes = color_of_eyes
        self.motherlanguage = motherlanguage

    def __repr__(self):
        return ('\n' + self.name.capitalize() + ': ' + self.age + ', Color of eyes - ' + self.color_of_eyes + ', Motherlanguage - ' + self.motherlanguage + '.')


class Student(Person):
    course = '1'

    def __repr__(self):
        return ('\n' + self.name + ': ' + self.age + ', Color of eyes - ' + self.color_of_eyes + ', Motherlanguage - ' + self.motherlanguage + ', Course: ' + self.course + '.')


student = Student('Anton Tkachuk', '22', 'grey', 'russian')
student.course = '4'


class Teacher(Person):
    speciality = 'math'
    working_hours_per_day = '8'
    
    def __repr__(self):
        return ('\n' + self.name + ': ' + self.age + ', Color of eyes - ' + self.color_of_eyes + ', Motherlanguage - ' + self.motherlanguage + ', Speciality: ' + self.speciality + ', Working hours per day: ' + self.working_hours_per_day + '.')


teacher = Teacher('Vasyl Demianovych', '66', 'red', 'ukrainian')

print(student)
print(teacher)


#TASK 2

'''
Mathematician

Implement a class Mathematician which is a helper class for doing math operations on lists

The class doesn't take any attributes and only has methods:

square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without positive numbers
filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'


class Mathematician:

    pass

m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

'''

class Mathematician:
    def square_nums(self, x):
        result_list = []
        for i in x:
            i = i*i
            result_list.append(i)
        return result_list


    def remove_positives(self, x):
        result_list = []
        for i in x:
            if i > 0:
                continue
            elif i <= 0:
                result_list.append(i)
        return result_list

    def filter_leaps(self, x):
        result_list = []
        for i in x:
            if i % 400 == 0 or i % 100 == 0 or i % 4 == 0:
                result_list.append(i)
            else: continue
        return result_list

m = Mathematician()

print()

print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([-9, 3, 4, -8, -8.7, 99]))
print(m.filter_leaps([2000, 2002, 1640, 1555, 1996]))


'''Product Store

Write a class Product that has three attributes:

type
name
price
Then create a class ProductStore, which will have some Products and will operate with all products in the store. All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.

Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement additional classes to operate on a certain type of product, etc.

Also, the ProductStore class must have the following methods:

add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers (type or name). The discount must be specified in percentage
sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error. It also increments income if the sell_product method succeeds.
get_income() - returns amount of many earned by ProductStore instance.
get_all_products() - returns information about all available products in the store.
get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
```

class Product:

    pass

class ProductStore:

pass

p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product(Food, 'Ramen, 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.sell(‘Ramen’, 10)

assert s.get_product_info(‘Ramen’) == (‘Ramen’, 290)

'''

class Product():
    my_type = ''
    name = ''
    price = 0

    def __init__(self, my_type, name, price):
        if type(my_type) != str:
            raise ValueError('Type of category should be a string!')
        if type(name) != str:
            raise ValueError('Type of')
        if type(price) != int and type(price) != float:
            raise ValueError('Price should have a numeral characters!')

        self.my_type = my_type
        self.name = name
        self.price = price

        def __repr__(self):
            return f'{self.name} = {self.price}'
    
        

class ProductStore:
    amount = 0
    profit = 0
    storage = []

    def add(self, product, amount):
        x = {}
        x['product'] = product
        x['amount'] = amount
        product.price *= 1.3
        self.storage.append(x)

    def set_discount(self, identifier, percent, identifier_name):
        if type(percent) != int and type(percent) != float:
            raise ValueError('Percent should be a numeral!')
        identifier_name = identifier_name.lower()
        if identifier_name == 'type':
            for i in self.storage:
                my_product = i['product']
                if my_product.my_type == identifier:
                    my_product.price = my_product.price * (1 - (percent / 100))
        elif identifier_name == 'name':
            for i in self.storage:
                my_product = i['product']
                if my_product.name == identifier:
                    my_product.price = my_product.price * (1 - (percent / 100))
        else:
            raise ValueError('Identifier name should be a "type" or "name".')

    def sell_product(self, product_name, amount):
        for i in self.storage:
            my_product = i['product']
            if my_product.name == product_name:
                if amount > i['amount']:
                    raise CustomException('We don\'t have such amount og product')
                else:
                    i['amount'] -= amount
                    self.profit += (amount * my_product.price)
    
    def get_income(self):
        return f'{self.profit} $'

    def get_all_product(self):
        return self.storage

    def product_info(self, product):
        for i in self.storage:
            my_product = i['product']
            if my_product.name == product.name:
                my_tuple = product.name, i['amount']
                return my_tuple


class CustomException(Exception):
    message = ''

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'{self.message}'

    def __repr__(self):
        return f'{self.message}'


'''Task 4

Custom exception

Create your custom exception named `CustomException`, you can inherit from base Exception class, but extend its functionality to log every error message to a file named `logs.txt`. Tips: Use __init__ method to extend functionality for saving messages to file

```

class CustomException(Exception):

def __init__(self, msg):
'''

try:
    first_product = Product("fruit", "apple", 10)
    second_product = Product("fruit", "watermelone", 45)
    store = ProductStore()
    store.add(first_product, 200)
    store.add(second_product, 50)
    print(store.get_all_product())
    store.sell_product("apple", 12)
    store.sell_product("watermelone", 30)
    print(store.get_all_product())
    print(store.get_income())
    store.set_discount("fruit", 50, "type")
    print(store.get_all_product())
    print(store.product_info(first_product))
except ValueError as e:
    print(e)
except CustomException as e:
    print(e)