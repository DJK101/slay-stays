import pytest
from io import StringIO
import app.commands as cmds


@pytest.fixture()
def bookings():
    return StringIO(
        "username,room,date\n"
        "dj,double,2025-01-01\n"
        "amy,single,2023-10-05\n"
        "rosie,economy,2024-11-11\n"
    )


def test_book_room():
    assert False


def test_check_bookings():
    assert False


def test_change_username():
    assert False


def test_change_password():
    assert False
