import csv
import datetime as dt


def help_menu():
    print("List of commands: ['help', 'book', 'my_bookings', 'change']")


# File parameter so the function can be tested easily
def book_room(username: str, room: str, date: dt.date, csv_file):
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        date_string = date.strftime('%Y-%m-%d')
        writer.writerow([username, room, date_string])
    pass


def check_bookings():
    pass


def change_username():
    pass


def change_password():
    pass


def shut_down():
    pass
