import csv
import datetime as dt
import os
import re
import sys
import app.login as login
from app.login import users_csv

# Fixes issue with tests executing code in different directory to program being run
cwd = os.getcwd()
if os.path.basename(cwd) != 'slay-stays':
    os.chdir('../')

print(os.getcwd())

bookings_csv = 'csv/bookings.csv'
keywords = ['help', 'quit', 'register', 'book', 'my_bookings', 'change_username']
rooms = ['double', 'single', 'family', 'suite', 'penthouse', 'presidential', 'deluxe', 'superior', 'standard',
         'economy']


def help_menu():
    print("List of commands:", keywords)


def register_user():
    print("Registration for Slay Stays:")
    username = input("Please enter a username: ")
    password = input("Please enter a password: ")
    login.create_user(username, password)


def book_room(username: str, csv_file=bookings_csv):
    print("List of available rooms: " + str(rooms))
    room = input("Please input the room you wish to book: ").lower()
    if room not in rooms:
        print("Error! The room entered could not be found.")
        return
    try:
        year = int(input("First, enter the YEAR of this booking (as an integer): "))
        month = int(input("Enter the MONTH of this booking (as an integer): "))
        day = int(input("Enter the DAY of this booking (as an integer): "))
    except ValueError:
        print("Error! The value entered could not be converted to an integer.")
        return
    date = dt.date(year, month, day)
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
            with open(csv_file, 'a', newline='\n') as w_file:
                writer = csv.writer(w_file)
                writer.writerow([username, room, date_string])
                print(f"Success! Room: {room} booked for {date_string}.")
        else:
            print("Sorry, that room has already been booked on that date.")


def print_bookings(username: str, csv_file=bookings_csv):
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


def is_valid_username(new_username):
    # returns true if username is valid.
    # valid usernames are between 2-16 characters long.
    # valid usernames only contain Alphanumeric characters and underscores.
    pattern = r"^[a-zA-Z0-9_]{2,16}$"
    if bool(re.match(pattern, new_username)):
        return True
    else:
        print("Sorry, usernames must be within 2-16 characters; "
              "and only contain letters, numbers, and underscores")
        return False


def change_username(old_username, users_csv_file=users_csv):
    new_username = input("Please enter your new username: ")
    with open(users_csv_file, mode='r') as users:
        reader = csv.DictReader(users)
        data = list(reader)

    for user in data:
        if user['username'] == old_username:
            if is_valid_username(new_username):
                user['username'] = new_username
                print(f"Success! User '{old_username}' has been updated to '{new_username}'.")
                login.set_current_user(new_username)

    with open(users_csv_file, mode='w', newline='') as csvfile:
        fieldnames = ['username', 'password']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def shut_down():
    sys.exit()
