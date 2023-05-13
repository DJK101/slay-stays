import datetime
import random
import csv


class Room:
    # name of the room, no. of people, price per night
    def __init__(self, name, capacity, price):
        self.name = name
        self.capacity = capacity
        self.price = price


# list of available rooms the user can book
Available_Rooms = [
    Room('Double', 2, 100),
    Room('Single', 1, 80),
    Room('Family', 4, 150),
    Room('Suite', 2, 200),
    Room('Penthouse', 6, 300),
    Room('Presidential', 4, 500),
    Room('Deluxe', 2, 250),
    Room('Superior', 2, 200),
    Room('Standard', 2, 110),
    Room('Economy', 1, 90),
]


# find room by name
def get_room(name):
    for room in Available_Rooms:
        if room.name == name:
            return room
    return None


# find room by price
def find_price(price):
    for room in Available_Rooms:
        if room.price == price:
            return room
    return None


# find room by capacity
def find_capacity(capacity):
    for room in Available_Rooms:
        if room.capacity == capacity:
            return room
    return None


def random_bool():
    return random.choice([True, False])


def is_sunny_outside():
    return random_bool()


def is_raining_outside():
    return random_bool()


def is_snowing_outside():
    return random_bool()


def is_tuesday():
    x = datetime.datetime.now()
    if x.strftime("%A") == "Tuesday":
        return True
    else:
        return False


def is_wednesday():
    x = datetime.datetime.now()
    if x.strftime("%A") == "Wednesday":
        return True
    else:
        return False


def is_birthday():
    now = datetime.date.today()
    birthdays = [datetime.date(now.year, 8, 30),
                 datetime.date(now.year, 7, 23),
                 datetime.date(now.year, 3, 2)]
    if now in birthdays:
        return True
    else:
        return False


def rooms_booked():
    bookings = []
    with open('bookings.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for i in reader:
            bookings.append(i)
        return bookings


def can_book_room(name, dt):
    if name == 'Double' and not is_sunny_outside():
        print("You cannot book this room because it's not sunny outside!")
        return False
    elif name == 'Single' and not is_raining_outside():
        print("You cannot book this room because it's not raining outside!")
        return False
    elif name == 'Family' and not is_snowing_outside():
        print("You cannot book this room because it's not snowing outside!")
        return False
    elif name == 'Suite' and not is_tuesday(dt):
        print("You can book this room because it's not a Tuesday!")
        return False
    elif name == 'Penthouse' and not is_wednesday(dt):
        print("You cannot book this room because it's not a Wednesday!")
        return False
    elif name == 'Presidential' and not is_birthday():
        print("You cannot book this room because it's not one of our birthdays!")
        return False
    elif name == 'Deluxe' and not is_birthday():
        print("You cannot book this room because it's not one of our birthdays!")
        return False
    elif name == 'Superior' and not is_birthday():
        print("You cannot book this room because it's not one of our birthdays!")
        return False
    elif name == 'Standard' and (not is_sunny_outside() or not is_tuesday(dt)):
        print("You cannot book this room because it's not a sunny Tuesday!")
        return False
    elif name == 'Economy' and (not is_raining_outside() or not is_wednesday(dt)):
        print("You cannot book this room because it's not a rainy Wednesday!")
        return False
    else:
        print("You can book this room!")
        return True
