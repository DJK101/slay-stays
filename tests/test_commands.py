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
                                     ['rosie', 'double', '2024-07-01'],
                                     ['john', 'single', '2024-11-05'],
                                     ['alex', 'penthouse', '2023-03-23'],
                                     ['fred', 'standard', '2023-09-17']])
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
        assert len(bookings_before) + 1 == len(bookings_after)  # Check a new line was added to the csv
        assert bookings_after[-1] == entries  # Checks booking was added to the end of the csv


@pytest.mark.parametrize("entries", [['amy', 'double', '2023-09-17'],
                                     ['rosie', 'suite', '2023-09-17'], ])
def test_book_room_not_booking_same_room_on_same_date(bookings, entries):
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


@pytest.mark.parametrize("username", ['dj', 'amy'])
def test_check_bookings_prints_bookings(capsys, bookings, username):
    cmds.check_bookings(username, bookings)
    out, err = capsys.readouterr()  # Capture the output to the terminal
    assert out.find('Success') != -1


@pytest.mark.parametrize("username", ['john', 'mark', 'eoin'])
def test_check_bookings_prints_error_if_no_bookings_found(capsys, bookings, username):
    cmds.check_bookings(username, bookings)
    out, err = capsys.readouterr()  # Capture the output to the terminal
    assert out.find('Sorry') != -1


@pytest.mark.parametrize("username, new_username", [('brenda', 'billy'), ('tiffany', 't-dawg'), ('blair', 'flair')])
def test_change_username(username, new_username):
    cmds.change_username(username, new_username)
    assert username == new_username


@pytest.mark.parametrize("username, new_username", [('stacey', 'stace'), ('yuri', 'connor'), ('eliza', 'elizabeth')])
def test_check_change_username_prints_success_msg(capsys, username, new_username):
    cmds.change_username(username, new_username)
    out, err = capsys.readouterr()  # Capture the output to the terminal
    assert out.find('Success') != -1

@pytest.mark.parametrize("username, new_username", [('brian', ''), ('gwen', 'gwen'), ('angelica', 'angel')])
def test_check_change_username_prints_error_msg(capsys, username, new_username):
    cmds.change_username(username, new_username)
    out, err = capsys.readouterr()  # Capture the output to the terminal
    assert out.find('Sorry') != -1

def test_change_password():
    assert False
