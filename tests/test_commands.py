from datetime import datetime as dt
import pytest
import app.commands as cmds
import csv


@pytest.fixture
def bookings(tmp_path):
    csv_file = tmp_path / 'bookings_test.csv'
    with open(csv_file, 'w', newline='') as bookings:
        writer = csv.writer(bookings)
        writer.writerows(
            [
                ['username', 'room', 'date'],
                ['dj', 'suite', '2023-09-17'],
                ['amy', 'double', '2023-09-17']
            ]
        )
    yield csv_file


@pytest.mark.parametrize("entries", [['amy', 'suite', '2023-09-17'],
                                     ['rosie', 'double', '2024-07-01']])
def test_book_room_adds_to_csv(bookings, entries):
    with open(bookings) as file:
        reader = csv.reader(file)
        bookings_before = list(reader)
        file.seek(0)  # Set reader to read from beginning of csv file
        date = dt.strptime(entries[2], '%Y-%m-%d')  # Convert string to datetime object for function
        cmds.book_room(entries[0], entries[1], date, bookings)  # Function being tested
        bookings_after = list(reader)
        assert len(bookings_before) + 1 == len(bookings_after)  # Check a newline was added to the csv
        assert bookings_after[-1] == entries  # Checks said line was the correct one


def test_check_bookings():
    assert False


def test_change_username():
    assert False


def test_change_password():
    assert False
