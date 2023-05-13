import datetime
import pytest
from app.Room import random_bool, is_sunny_outside, is_raining_outside, is_snowing_outside, is_tuesday, \
    is_wednesday, is_birthday, get_room, find_price, find_capacity, can_book_room
from freezegun import freeze_time
from datetime import datetime as dt


@pytest.mark.parametrize("name, capacity, price",
                         [('Deluxe', 2, 250), ('Superior', 2, 200), ('Standard', 2, 110), ('Economy', 1, 90)])
def test_get_room(name, capacity, price):
    room = get_room(name)
    assert room is not None if capacity or price else None


@pytest.mark.parametrize("price, capacity, name",
                         [(250, 2, 'Deluxe'), (200, 2, 'Superior'), (110, 2, 'Standard'), (90, 1, 'Economy')])
def test_find_price(price, capacity, name):
    price = find_price(price)
    assert price is not None if capacity or name else None


@pytest.mark.parametrize("capacity, price, name",
                         [(2, 250, 'Deluxe'), (2, 200, 'Superior'), (2, 110, 'Standard'), (1, 90, 'Economy')])
def test_find_capacity(capacity, price, name):
    capacity = find_capacity(capacity)
    assert capacity is not None if price or name else None


def test_random_bool():
    assert random_bool() in [True, False]


def test_is_sunny_outside():
    assert is_sunny_outside() in [True, False]


def test_is_raining_outside():
    assert is_raining_outside() in [True, False]


def test_is_snowing_outside():
    assert is_snowing_outside() in [True, False]


@pytest.fixture
def now():
    return datetime.datetime.now()


@pytest.mark.parametrize("date, expected", [('2022-06-08', False),
                                            ('2022-06-07', True),
                                            ('2022-06-09', False)])
def test_is_tuesday(date, expected):
    date = dt.strptime(date, '%Y-%m-%d')
    assert is_tuesday(date) == expected


@pytest.fixture
def now():
    return datetime.datetime.now()


@pytest.mark.parametrize("date, expected", [('2022-06-08', True),
                                            ('2022-06-07', False),
                                            ('2022-06-09', False)])
def test_is_wednesday(date, expected):
    date = dt.strptime(date, '%Y-%m-%d')
    assert is_wednesday(date) == expected


@freeze_time("2021-07-23")
def test_is_birthday():
    assert is_birthday()


# problem with this test, the second bool parameter is fixed in the test but randomly generated in the function,
#  so the test will randomly pass / fail
@pytest.mark.parametrize("room, result, expected", [
    ("Double", False, False), ("Double", True, True)])
def test_can_book_room(room, result, expected):
    assert can_book_room(room, result) == expected
