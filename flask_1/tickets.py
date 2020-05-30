
class Ticket:
    status = None

    def __init__(self, event, datetime, circle, raw, seat, price):
        self.event = event
        self.datetime = datetime
        self.circle = circle
        self.raw = raw
        self.seat = seat
        self.price = price

    def __eq__(self, other):
        return self.event == other.event and self.circle == other.circle and self.raw == other.raw and self.seat == other.seat and self.price == other.price

    def __str__(self):
        return f'{self.event} ({self.datetime}) circle: {self.circle}, {self.raw} raw, {self.seat} seat, {self.price} UAH.'

    def __repr__(self):
        return f'{self.event} ({self.datetime}) circle:{self.circle}, {self.raw} raw, {self.seat} seat, {self.price} UAH.'


class Visitor():
    name = str
    email = str
    
    def __init__(self, name, email, event):
        self.event = event.event
        self.datetime = event.datetime
        self.circle = event.circle
        self.raw = event.raw
        self.seat = event.seat
        self.price = event.price
        self.name = name
        self.email = email
        self.code = hash((self.name, self.email, self.event, event.datetime, event.circle, event.raw, event.seat, event.price))
        print(f'Your personal code is {self.code}')

    def __hash__(self):
        print('The hash is:')
        return hash((self.name, self.email, self.event, event.datetime, event.circle, event.raw, event.seat, event.price))

    def __str__(self):
        return f'Dear {self.name}, check your email {self.email} to get your ticket on {event.event} ({event.datetime}) circle: {event.circle}, {event.raw} raw, {event.seat} seat, {event.price} UAH.'

    def __repr__(self):
        return f'Dear {self.name}, check your email {self.email} to get your ticket on {event.event} ({event.datetime}) circle: {event.circle}, {event.raw} raw, {event.seat} seat, {event.price} UAH.'


def print_menu():
    print('1. Create event')
    print('2. Show available event')
    print('3. Show the hash of the event')
    print('4. Buy ticket')
    print('6. Activate ')
    print('7. Check status')
    print('0. Break')


while True:
    command = input('Write your command: ')
    if command == '0':
        break
    elif command == '1':
        event = Ticket('krovostok', '22:12:2022 22:00', 'parterre', '5', '44', '890')
        print(f'Ticket on {event.event} was created!')
        #event = input('Write the name of your event: ')
        #event = Ticket(event, input('Write date and time in format dd.mm.yyyy hh:mm:'), input('Enter here the circle (parterre/1/2/3): '), input('Number of row: '), input('Number of seat: '), input('Price: '))
    elif command == '2':
        print(event)
    elif command == '3':  
        print(visitor.__hash__())
    elif command == '4':
        visitor = Visitor('Ivan the Terrible', 'ivantheterrible@jabber.com', event)
        print(f'\nCongratulation! Your ticket with security code {visitor.code} is purchased!')
        print(visitor)
    elif command == '6':
        event.status = 'activated'
        print('Activated!')
    elif command == '7':
        if event.status == None:
            print('The ticket is not activated.')
        elif event.status == 'activated':
            print('The ticket already activated!')