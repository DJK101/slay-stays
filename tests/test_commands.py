from datetime import datetime as dt
import pytest
from unittest.mock import patch
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
                ['amy', 'double', '2023-09-17'],
            ]
        )
    yield csv_file


@pytest.mark.parametrize("entries", [['amy', 'suite', '2023-09-10'],
                                     ['rosie', 'double', '2024-07-01']])
def test_book_room_adds_to_csv(bookings, entries):
    with open(bookings) as file:
        reader = csv.reader(file)
        bookings_before = list(reader)
        date = dt.strptime(entries[2], '%Y-%m-%d')  # Convert string to datetime object for function
        with patch('builtins.print') as mock_print:
            cmds.book_room(entries[0], entries[1], date, bookings)  # Function being tested
            mock_print.assert_called_once_with(f"Success! Room: {entries[1]} booked for {entries[2]}.")
        file.seek(0)  # Set reader to read from beginning of csv file
        bookings_after = list(reader)
        assert len(bookings_before) + 1 == len(bookings_after)  # Check a newline was added to the csv
        assert bookings_after[-1] == entries  # Checks said line was the correct one


@pytest.mark.parametrize("entries", [['amy', 'double', '2023-09-17'],
                                     ['rosie', 'suite', '2023-09-17']])
def test_book_room_not_booking_on_same_date(mocker, bookings, entries):
    with open(bookings) as file:
        reader = csv.reader(file)
        bookings_before = list(reader)
        file.seek(0)  # Set reader to read from beginning of csv file
        date = dt.strptime(entries[2], '%Y-%m-%d')
        with patch('builtins.print') as mock_print:
            cmds.book_room(entries[0], entries[1], date, bookings)
            mock_print.assert_called_once_with("Sorry, that room has already been booked on that date.")
        bookings_after = list(reader)
        assert len(bookings_before) == len(bookings_after)
        assert bookings_after[-1] == ['amy', 'double', '2023-09-17']


def test_check_bookings(bookings):
    assert False


def test_change_username():
    assert False


def test_change_password():
    assert False
