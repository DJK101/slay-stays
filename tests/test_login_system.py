import pytest
from io import StringIO
import app.login_system as login
import csv


@pytest.fixture
def users(tmp_path):
    csv_file = tmp_path / 'bookings_test.csv'
    with open(csv_file, 'w', newline='') as bookings:
        writer = csv.writer(bookings)
        writer.writerows(
            [
                ['username', 'room', 'date'],
                ['dj', 'suite', '2023-09-17'],
                ['amy', 'double', '2023-09-17'],
            ]
        )
    yield csv_file


@pytest.mark.parametrize("test_input, expected", [('dj', 0), ('me', 1), ('amy', 2), ('john', -1)])
def test_find_user(users, test_input, expected):
    assert login.find_user(test_input, users) == expected


def test_create_user(users):
    assert False


@pytest.mark.parametrize("test_input, expected", [('dj', True), ('me', True), ('amy', True)])
def test_delete_user(users, test_input, expected):
    assert login.delete_user(test_input, users) == expected


def test_check_password(users):
    assert login.check_password('dj', '100', users)
