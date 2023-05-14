import pytest
import app.login as login
import csv
from unittest.mock import patch


@pytest.fixture
def file(tmp_path):
    csv_file = tmp_path / 'bookings_test.csv'
    with open(csv_file, 'w', newline='') as bookings:
        writer = csv.writer(bookings)
        writer.writerows(
            [
                ['username', 'password'],
                ['dj', '1234'],
                ['me', 'pwd'],
                ['amy', 'drummer']
            ]
        )
    yield csv_file


@pytest.fixture
def admin_password():
    return 'tracworx'


@pytest.mark.parametrize("test_input, expected", [('dj', 0), ('me', 1), ('amy', 2), ('john', -1)])
def test_find_user(file, test_input, expected):
    assert login.find_user(test_input, file) == expected


@pytest.mark.parametrize("username, password", [('mark', 'secret')])
def test_create_user_adds_user_to_csv(file, username, password):
    with open(file, 'r') as users:
        reader = csv.reader(users)
        users_before = list(reader)
        with patch('builtins.print') as mock_print:
            login.create_user(username, password, file)
            mock_print.assert_called_once_with(f"Success! Registered user {username} to Slay Stays.")
        users.seek(0)
        users_after = list(reader)
        assert len(users_before) + 1 == len(users_after)
        assert users_after[-1] == [username, password]


@pytest.mark.parametrize("username, password", [('dj', '1234')])
def test_create_user_wont_add_duplicate_usernames(file, username, password):
    with open(file, 'r') as users:
        reader = csv.reader(users)
        users_before = list(reader)
        with patch('builtins.print') as mock_print:
            login.create_user(username, password, file)
            mock_print.assert_called_once_with(f"Sorry, the username '{username}' is already taken.")
        users.seek(0)
        users_after = list(reader)
        assert len(users_before) == len(users_after)


@pytest.mark.parametrize("username, password", [('dj', '1234')])
def test_delete_user_removes_user_from_csv(file, admin_password, username, password):
    with open(file) as users:
        reader = csv.reader(users)
        users_before = list(reader)
        with patch('builtins.print') as mock_print:
            login.delete_user(username, admin_password, file)
            mock_print.assert_called_once_with(f"Success! Deleted user '{username}' from database.")
        users.seek(0)
        users_after = list(reader)
        removed_users = [user for user in users_before if user not in users_after]
        assert len(users_before) == len(users_after) + 1
        assert removed_users == [[username, password]]


@pytest.mark.parametrize("username", ['greg', '1', 'True', ''])
def test_delete_user_prints_error_when_username_missing(file, admin_password, username):
    with open(file) as users:
        reader = csv.reader(users)
        users_before = list(reader)
        with patch('builtins.print') as mock_print:
            login.delete_user(username, admin_password, file)
            mock_print.assert_called_once_with(f"Error! No user '{username}' was found.")
        users.seek(0)
        users_after = list(reader)
        assert users_before == users_after


@pytest.mark.parametrize("username, wrong_password", [('dj', 'fishy'), ('me', ''), ('amy', 'True')])
def test_delete_user_fails_when_admin_password_is_incorrect(file, username, wrong_password):
    with open(file) as users:
        reader = csv.reader(users)
        users_before = list(reader)
        with patch('builtins.print') as mock_print:
            login.delete_user(username, wrong_password, file)
            mock_print.assert_called_once_with("Error! The admin password entered was incorrect!")
        users.seek(0)
        users_after = list(reader)
        assert users_before == users_after


@pytest.mark.parametrize("username, password, expected",
                         [('dj', '1234', True),
                          ('billy', 'incorrect', False)])
def test_check_password(file, username, password, expected):
    assert login.check_password(username, password, file) == expected


@pytest.mark.parametrize("username, password", [('dj', '1234'),
                                                ('me', 'pwd'),
                                                ('amy', 'drummer')])
def test_login_returns_username_on_valid_login(file, username, password):
    with patch('builtins.input', side_effect=[username, password]):
        assert login.login(file) == username


@pytest.mark.parametrize("username, password", [('wrong', 'input')])
def test_login_never_returns_on_invalid_input(file, username, password):
    with patch('builtins.input', side_effect=[username, password]):
        assert login.login(file) is None


@pytest.mark.parametrize("usernames, password", [(['a', 'b', 'dj'], '1234')])
def test_login_allows_for_multiple_username_entries(file, usernames, password):
    for username in usernames:
        if username == usernames[-1]:
            with patch('builtins.input', side_effect=[username, password]):
                assert login.login(file) == username
        else:
            with patch('builtins.input', side_effect=username) as mock_input:
                mock_input.assert_called_once_with(
                    f"Sorry, the username {username} couldn't be found. Please try again:")


@pytest.mark.parametrize("username, passwords", [('dj', ['a', 'b', 'c', '1234'])])
def test_login_allows_for_multiple_username_entries(file, username, passwords):
    for password in passwords:
        if password == passwords[-1]:
            with patch('builtins.input', side_effect=[username, password]):
                assert login.login(file) == username
        else:
            with patch('builtins.input', side_effect=username) as mock_input:
                mock_input.assert_called_once_with(
                    f"Sorry, the username {username} couldn't be found. Please try again:")
