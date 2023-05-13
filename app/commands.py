import csv
import datetime as dt


def help_menu():
    print("List of commands: ['help', 'book', 'my_bookings', 'change']")


# File parameter so the function can be tested easily
def book_room(username: str, room: str, date: dt.date, csv_file):
    date_string = date.strftime('%Y-%m-%d')
    with open(csv_file, 'r') as r_file:
        reader = csv.DictReader(r_file)
        bookings = list(reader)
        bookings_dates = [booking['date'] for booking in bookings]
        if date_string in bookings_dates:
            print("Sorry, that room has already been booked on that date.")
        else:
            r_file.close()
            with open(csv_file, 'a', newline='') as w_file:
                writer = csv.writer(w_file)
                writer.writerow([username, room, date_string])
                print(f"Success! Room: {room} booked for {date_string}.")


def check_bookings(username: str, csv_file):
    pass


def change_username():
    pass


def change_password():
    pass


def shut_down():
    pass
