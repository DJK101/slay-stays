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


@pytest.fixture
def users(tmp_path):
    csv_file = tmp_path / 'users_test.csv'
    with open(csv_file, 'w', newline='') as users:
        writer = csv.writer(users)
        writer.writerows(
            [
                ['username', 'password'],
                ['dj', 'kachow'],
                ['rosie', 'herder'],
                ['blair', 'rowenah8club'],
                ['amy', 'mutmut4lyfe'],
            ]
        )
    yield csv_file


@pytest.mark.parametrize("username, room, date_str", [['amy', 'suite', '2023-09-10'],
                                                      ['rosie', 'double', '2024-07-01'],
                                                      ['john', 'single', '2024-11-05'],
                                                      ['alex', 'penthouse', '2023-03-23'],
                                                      ['fred', 'standard', '2023-09-17']])
def test_book_room_adds_to_csv(bookings, username, room, date_str):
    with open(bookings) as file:
        reader = csv.reader(file)
        bookings_before = list(reader)
        date = dt.strptime(date_str, '%Y-%m-%d')  # Convert string to datetime object for function
        with patch('builtins.print') as mock_print:
            with patch('builtins.input', side_effect=[room, date.year, date.month, date.day]):
                cmds.book_room(username, bookings)  # Function being tested
            mock_print.assert_called_with(f"Success! Room: {room} booked for {date_str}.")
        file.seek(0)  # Set reader to read from beginning of csv file
        bookings_after = list(reader)
        assert len(bookings_before) + 1 == len(bookings_after)  # Check a new line was added to the csv
        assert bookings_after[-1] == [username, room, date_str]  # Checks booking was added to the end of the csv


@pytest.mark.parametrize("username, room, date_str", [['amy', 'double', '2023-09-17'],
                                                      ['rosie', 'suite', '2023-09-17'], ])
def test_book_room_not_booking_same_room_on_same_date(bookings, username, room, date_str):
    with open(bookings) as file:
        reader = csv.reader(file)
        bookings_before = list(reader)
        file.seek(0)  # Set reader to read from beginning of csv file
        date = dt.strptime(date_str, '%Y-%m-%d')
        with patch('builtins.print') as mock_print:
            with patch('builtins.input', side_effect=[room, date.year, date.month, date.day]):
                cmds.book_room(username, bookings)
            mock_print.assert_called_with("Sorry, that room has already been booked on that date.")
        bookings_after = list(reader)
        assert len(bookings_before) == len(bookings_after)
        assert bookings_after[-1] == bookings_before[-1]


@pytest.mark.parametrize("username", ['dj', 'amy'])
def test_print_bookings_prints_bookings(capsys, bookings, username):
    cmds.print_bookings(username, bookings)
    out, err = capsys.readouterr()  # Capture the output to the terminal
    assert out.find('Success') != -1


@pytest.mark.parametrize("username", ['john', 'mark', 'eoin'])
def test_print_bookings_prints_error_if_no_bookings_found(capsys, bookings, username):
    cmds.print_bookings(username, bookings)
    out, err = capsys.readouterr()  # Capture the output to the terminal
    assert out.find('Sorry') != -1


@pytest.mark.parametrize("new_username, expected",
                         [('dj', True), ('_rosie_kennelly_', True), ('M1TSK11114EVA', True), ('', False),
                          ('a', False), ('nonphotosynthetic', False), ('$money*bags!', False)])
def test_is_valid_username(new_username, expected):
    assert cmds.is_valid_username(new_username) == expected


@pytest.mark.parametrize("new_username", ['!brian!', 'gw$-en', 'cringe_lord--£'])
def test_is_valid_username_prints_error_msg(capsys, new_username):
    cmds.is_valid_username(new_username)
    out, err = capsys.readouterr()  # Capture the output to the terminal
    assert out.find('Sorry') != -1


@pytest.mark.parametrize("old_username, new_username", [('dj', 'billy'), ('rosie', 'tdawg'), ('blair', 'flair')])
def test_change_username(users, old_username, new_username):
    with open(users) as file:
        reader = csv.DictReader(file)
        users_list = list(reader)
        usernames = [user['username'] for user in users_list]
        user_index = usernames.index(old_username)
        with patch('builtins.input', return_value=new_username):
            cmds.change_username(old_username, users)
        file.seek(0)
        next(reader)
        new_users_list = list(reader)
        assert new_users_list[user_index]['username'] == new_username


@pytest.mark.parametrize("old_username, new_username",
                         [('dj', 'stace'), ('amy', 'connor'), ('blair', 'elizabeth')])
def test_check_change_username_prints_success_msg(capsys, users, old_username, new_username):
    with patch('builtins.input', return_value=new_username):
        cmds.change_username(old_username, users)
    out, err = capsys.readouterr()
    assert out.find('Success') != -1


@pytest.mark.parametrize("new_username", ['', 'gwen!', 'angel£ica', 'ange)1l'])
def test_check_is_valid_username_prints_error_msg(capsys, new_username):
    cmds.is_valid_username(new_username)
    out, err = capsys.readouterr()  # Capture the output to the terminal
    assert out.find('Sorry') != -1


@pytest.mark.parametrize("username, password", [('johnny', 'safe')])
def test_register_user_passes_correct_inputs(username, password):
    with patch('builtins.input', side_effect=[username, password]):
        with patch('app.login.create_user') as mock_create_user:
            cmds.register_user()
            mock_create_user.assert_called_once_with(username, password)
