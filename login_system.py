import csv


def find_user(username: str, file):
    users = csv.DictReader(file)
    users = list(users)
    for i in range(0, len(users)):
        if users[i]['username'] == username:
            return i


def delete_user(username: str, file):
    pass


def create_user(username: str, password: str, file):
    pass
