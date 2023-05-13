import datetime as dt


def help_menu():
    print("List of commands: ['help', 'book', 'my_bookings', 'change']")


# File parameter so the function can be tested easily
def book_room(username: str, room: str, date: dt.date, file):
    print(username, room, date, file)
    pass


def check_bookings():
    pass


def change_username():
    pass


def change_password():
    pass


def shut_down():
    pass
