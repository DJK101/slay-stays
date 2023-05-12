import datetime
import pytest
from app.Room import random_bool, is_sunny_outside, is_raining_outside, is_snowing_outside, is_tuesday, \
    is_wednesday, is_birthday, find_room, find_price, find_capacity
from freezegun import freeze_time
from datetime import datetime as dt


def test_find_room():
    room = find_room('Double')
    assert room is not None
    assert room.capacity == 2
    assert room.price == 100

    room = find_room('Room that does not exist')
    assert room is None


def test_find_price():
    price = find_price(100)
    assert price is not None
    assert price.capacity == 2
    assert price.name == 'Double'

    price = find_price(100000)
    assert price is None


def test_find_capacity():
    capacity = find_capacity(2)
    assert capacity is not None
    assert capacity.price == 100
    assert capacity.name == 'Double'

    capacity = find_price(100000)
    assert capacity is None


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
