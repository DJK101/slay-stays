import csv
import datetime as dt
import sys

keywords = ['help', 'quit', 'book', 'my_bookings', 'change']


def help_menu():
    print("List of commands:", keywords)


# File parameter so the function can be tested easily
def book_room(username: str, room: str, date: dt.date, csv_file):
    date_string = date.strftime('%Y-%m-%d')
    with open(csv_file, 'r') as r_file:
        reader = csv.DictReader(r_file)
        bookings = list(reader)
        bookings_dates = [booking['date'] for booking in bookings]
        bookings_rooms = [booking['room'] for booking in bookings]
        booking_available = True
        for i in range(0, len(bookings)):
            if bookings_rooms[i] == room and bookings_dates[i] == date_string:
                booking_available = False

        if booking_available:
            r_file.close()
            with open(csv_file, 'a', newline='') as w_file:
                writer = csv.writer(w_file)
                writer.writerow([username, room, date_string])
                print(f"Success! Room: {room} booked for {date_string}.")
        else:
            print("Sorry, that room has already been booked on that date.")


def check_bookings(username: str, csv_file):
    with open(csv_file) as file:
        reader = csv.DictReader(file)
        bookings = list(reader)
        user_bookings = []
        for booking in bookings:
            if booking['username'] == username:
                user_bookings.append(f"{booking['room']} booked for {booking['date']}")

        if len(user_bookings) > 0:
            print("Success! Here are your bookings:\n")
            for booking in user_bookings:
                print(booking + "\n")
        else:
            print("Sorry, no bookings could be found with your username.")
    pass


def change_username():
    pass


def change_password():
    pass


def shut_down():
    sys.exit()
