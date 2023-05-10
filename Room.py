class Hotel_Room:
    # name of room, no. of people, price per night
    def __init__(self, name, capacity, price):
        self.name = name
        self.capacity = capacity
        self.price = price


# list of available rooms the user can book
Available_Rooms = [
    Hotel_Room('Double', 2, 100),
    Hotel_Room('Single', 1, 80),
    Hotel_Room('Family', 4, 150),
    Hotel_Room('Suite', 2, 200),
    Hotel_Room('Penthouse', 6, 300),
    Hotel_Room('Presidential', 4, 500),
    Hotel_Room('Deluxe', 2, 250),
    Hotel_Room('Superior', 2, 200),
]
