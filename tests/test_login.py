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
def test_delete_user_removes_user_from_csv(file, username, password):
    admin_password = 'tracworx'
    with open(file) as users:
        reader = csv.reader(users)
        users_before = list(reader)
        with patch('builtins.print') as mock_print:
            login.delete_user(username, admin_password, file)
            mock_print.assert_called_once_with(f"Success! Deleted user '{username}' from database.")
        users.seek(0)
        users_after = list(reader)
        assert len(users_before) == len(users_after) + 1
        assert set(users_before) - set(users_after) == [username, password]


@pytest.mark.parametrize("username, password, expected",
                         [('dj', '1234', True),
                          ('billy', 'incorrect', False)])
def test_check_password(file, username, password, expected):
    assert login.check_password(username, password, file) == expected
