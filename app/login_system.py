import csv


def find_user(username: str, file):
    users = csv.DictReader(file)
    users = list(users)
    for i in range(0, len(users)):
        if users[i]['username'] == username:
            return i


def delete_user(usersDelete: str, file):
    users = csv.DictReader(file)
    users = list(users)
    for i in range(0, len(users)):
        if users[i]['username'] == usersDelete:
            return True


def create_user(username: str, password: str, file):
    pass


def check_password(username: str, password: str, csv_file) -> bool:
    pass
