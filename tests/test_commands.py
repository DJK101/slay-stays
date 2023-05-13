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


def test_book_room(bookings):
    with open(bookings) as file:
        reader = csv.reader(file)
        bookings_before = list(reader)
        file.seek(0)  # Set reader to read from beginning of csv file
        entries = ['amy', 'suite', dt.strptime('2023-09-17', '%Y-%m-%d')]
        cmds.book_room(entries[0], entries[1], entries[2], file)
        bookings_after = list(reader)
        assert len(bookings_before) + 1 == len(bookings_after)
        assert bookings_after[-1] == entries


def test_check_bookings():
    assert False


def test_change_username():
    assert False


def test_change_password():
    assert False
