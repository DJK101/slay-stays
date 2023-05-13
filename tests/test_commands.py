import os
import pytest
from io import StringIO
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
                ['dj', 'suite', '2023-09-17']
            ]
        )
    yield csv_file


def test_book_room(bookings):
    with open(bookings) as file:
        bookings_before = list(csv.DictReader(file))
        cmds.book_room('amy', 'suite', '2025-06-18')
        bookings_after = list(csv.DictReader(file))
        assert len(bookings_before) + 1 == len(bookings_after)



def test_check_bookings():
    assert False


def test_change_username():
    assert False


def test_change_password():
    assert False
