import csv


# Returns index of username in the database. First user at index 0
def find_user(username: str, file) -> int:
    with open(file) as users:
        reader = csv.DictReader(users)
        users = list(reader)
        usernames = [user['username'] for user in users]
        try:
            return usernames.index(username)
        except ValueError:
            return -1


def delete_user(usersDelete: str, file):
    users = csv.DictReader(file)
    users = list(users)
    for i in range(0, len(users)):
        if users[i]['username'] == usersDelete:
            return True


def create_user(username: str, password: str, file):
    pass


def check_password(username: str, password: str, csv_file) -> bool:
    user_index = find_user(username, csv_file)
    with open(csv_file, 'r') as users:
        reader = csv.DictReader(users)
        users = list(reader)
        if users[user_index]['password'] == password:
            return True
        else:
            return False
