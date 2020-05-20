print('\n')

# Task 1
class person:
    def __init__(self, firstname, lastname, age):
       self.firstname = firstname
       self.lastname = lastname
       self.age = age
    def talk(self):
        return('Hello, my name is ' + (f'{self.firstname} ').capitalize() + (f'{self.lastname}').capitalize() + f" and I'm {self.age} years old.")

anton = person('anton', 'tkachuk', 22)
print(anton.talk())


print('\n')

# Task 2
class dog:
    age_factor = 7
    def __init__(self, dogs_age):
        self.dogs_age = dogs_age
    def human_age(self):
        return(self.dogs_age * self.age_factor)
        
scooby = dog(9)
print("Scooby's age in human equivalent: " + f'{scooby.human_age()}.')
print('\n\n')


# Task 3 !В ПРОЦЕССЕ

channels = ['BBC', 'Discovery', 'CNN', 'National Geographic']

class TVController:
    def __init__(self, channels):
        self.channels = channels

    def first_channel(self):
        print(self.channels[0])

    def last_channel(self):
        print(self.channels[-1])

    def turn_channel(self, x):
        x = int(x)
        x -= 1
        print(self.channels[x])
        #print('Такого канала не знаю')

    def next_channel(self):
        pass

    def previous_channel(self):
        pass

    def current_channel(self):
        pass

    def is_exist(self, x):
        pass

def print_menu():
    print()
    print('1. ')
    print('2. ')
    
controller = TVController(channels)

command = input('Hi! Enter "ON", if you want to turn on the TV.').strip().lower()
if command == 'on': 
    controller.first_channel()
    controller.last_channel()
    controller.turn_channel()
    controller.next_channel()