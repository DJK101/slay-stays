import datetime
import csv


class Hotel_Room:
    # name of the room, no. of people, price per night
    def __init__(self, name, capacity, price):
        self.name = name
        self.capacity = capacity
        self.price = price


# list of available rooms the user can book
Available_Rooms = [
    # can only book if it's sunny
    Hotel_Room('Double', 2, 100),
    # can only book if its raining
    Hotel_Room('Single', 1, 80),
    # can only book if its snowing
    Hotel_Room('Family', 4, 150),
    # can only book if it's a tuesday
    Hotel_Room('Suite', 2, 200),
    # can only book if it's a wednesday
    Hotel_Room('Penthouse', 6, 300),
    # can only book if its
    Hotel_Room('Presidential', 4, 500),
    Hotel_Room('Deluxe', 2, 250),
    Hotel_Room('Superior', 2, 200),
    Hotel_Room('Standard', 2, 110),
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


def is_sunny_outside():
    return True


def is_raining_outside():
    return False


def is_snowing_outside():
    return False


def is_tuesday():
    return False


def is_wednesday():
    return False
