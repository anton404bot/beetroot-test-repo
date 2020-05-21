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


# Task 3 

class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.channel_number = 1

    def get_current_channel(self):
        return self.channels[self.channel_number - 1]

    def next_channel(self):
        if self.channel_number >= len(self.channels):
            self.channel_number = 1
        else:
            self.channel_number += 1
        return self.get_current_channel()

    def prev_channel(self):
        if self.channel_number == 1:
            self.channel_number = len(self.channels)
        else:
            self.channel_number -= 1
        return self.get_current_channel()

    def get_channel(self, index):
        if 0 < index <= len(self.channels):
            self.channel_number = index
        return self.get_current_channel()


channels = ['BBC', 'Discovery', 'CNN', 'National Geographic']

def print_menu():
    print()
    print('1. See current channel')
    print('2. Next channel')
    print('3. Previous channel')
    print('4. Turn definite channel by number')
    print('0. Turn off')

controller = TVController(channels)

command = input('Hi! Enter "ON", if you want to turn on the TV. ').strip().lower()
if command == 'on': 
    print('\nNow ' + controller.get_current_channel() + ' is playing.')
    print_menu()
    while True:
        command = input('Choose an option from the menu: ')
        print_menu()
        if command == '0':
            break
        elif command == '1':
            print('\nNow ' + controller.get_current_channel() + ' is playing.')
        elif command == '2':
            print('\nNow ' + controller.next_channel() + ' is playing.')
        elif command == '3':
            print('\nNow ' + controller.prev_channel() + ' is playing.')
        elif command == '4':
            while True:
                try:
                    index = int(input('\nEnter the number of the channel you would like to watch: '))
                    if index > len(channels):
                        print("\nI don't have so many channels( ")
                    elif index <= len(channels):
                        print(controller.get_channel(index))
                        break
                except ValueError:
                    print('\nPlease, don\'t do it.')
        else:
            print("I don't know what to do( ")