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


def delete_user(username: str, admin_password: str, file):
    if admin_password != 'tracworx':
        print("Error! The admin password entered was incorrect!")
        return

    if find_user(username, file) == -1:  # -1 Indicates no matching user was found in the database
        print(f"Error! No user '{username}' was found.")
        return

    with open(file) as users:
        reader = csv.DictReader(users)
        users_list = list(reader)
        new_users_list = [user for user in users_list if user['username'] != username]

    with open(file, 'w', newline='') as users:
        writer = csv.DictWriter(users, ['username', 'password'])
        writer.writeheader()
        writer.writerows(new_users_list)

    print(f"Success! Deleted user '{username}' from database.")





def create_user(username: str, password: str, file):
    with open(file) as users:
        reader = csv.DictReader(users)
        usernames = [user['username'] for user in list(reader)]
        if username in usernames:
            print(f"Sorry, the username '{username}' is already taken.")
            return

    with open(file, 'a', newline='') as users:
        writer = csv.writer(users)
        writer.writerow([username, password])
        print(f"Success! Registered user {username} to Slay Stays.")


def check_password(username: str, password: str, csv_file) -> bool:
    user_index = find_user(username, csv_file)
    with open(csv_file, 'r') as users:
        reader = csv.DictReader(users)
        users = list(reader)
        if users[user_index]['password'] == password:
            return True
        else:
            return False
