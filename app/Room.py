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
    # can only book if it's sunny
    Room('Double', 2, 100),
    # can only book if its raining
    Room('Single', 1, 80),
    # can only book if its snowing
    Room('Family', 4, 150),
    # can only book if it's a tuesday
    Room('Suite', 2, 200),
    # can only book if it's a wednesday
    Room('Penthouse', 6, 300),
    # can only book if it's my birthday
    Room('Presidential', 4, 500),
    # can only book if it's Rosie's birthday
    Room('Deluxe', 2, 250),
    # can only book if it's DJ's birthday
    Room('Superior', 2, 200),
    # can only book if it's a sunny Tuesday
    Room('Standard', 2, 110),
    # can only book if it's a rainy Wednesday
    Room('Economy', 1, 90),
]


# find room by name
def find_room(name):
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


def is_my_birthday():
    MyBirthday = datetime.date(2005, 8, 30)
    today = datetime.date.today()
    if MyBirthday == today:
        return True
    else:
        return False


def is_rosies_birthday():
    RBirthday = datetime.date(2004, 3, 2)
    today = datetime.date.today()
    if RBirthday == today:
        return True
    else:
        return False


def is_djs_birthday():
    DJBirthday = datetime.date(2003, 7, 23)
    today = datetime.date.today()
    if DJBirthday == today:
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
