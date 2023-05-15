import datetime
import pytest
import app.room as rm
from freezegun import freeze_time


@pytest.fixture
def now():
    return datetime.datetime.now()


@pytest.mark.parametrize("name, capacity, price",
                         [('Deluxe', 2, 250), ('Superior', 2, 200), ('Standard', 2, 110), ('Economy', 1, 90)])
def test_get_room(name, capacity, price):
    room = rm.get_room(name)
    assert room is not None if capacity or price else None


@pytest.mark.parametrize("price, capacity, name",
                         [(250, 2, 'Deluxe'), (200, 2, 'Superior'), (110, 2, 'Standard'), (90, 1, 'Economy')])
def test_find_price(price, capacity, name):
    price = rm.find_price(price)
    assert price is not None if capacity or name else None


@pytest.mark.parametrize("capacity, price, name",
                         [(2, 250, 'Deluxe'), (2, 200, 'Superior'), (2, 110, 'Standard'), (1, 90, 'Economy')])
def test_find_capacity(capacity, price, name):
    capacity = rm.find_capacity(capacity)
    assert capacity is not None if price or name else None


def test_random_bool():
    assert rm.random_bool() in [True, False]


def test_is_sunny_outside():
    assert rm.is_sunny_outside() in [True, False]


def test_is_raining_outside():
    assert rm.is_raining_outside() in [True, False]


def test_is_snowing_outside():
    assert rm.is_snowing_outside() in [True, False]


@freeze_time("2022-06-08")
def test_is_wednesday():
    assert rm.is_wednesday()


@freeze_time("2022-06-07")
def test_is_tuesday():
    assert rm.is_tuesday()


@freeze_time("2021-07-23")
def test_is_birthday():
    assert rm.is_birthday()


# problem with this test, the second bool parameter is fixed in the test but randomly generated in the function,
#  so the test will randomly pass / fail
@pytest.mark.parametrize("room, result, expected", [
    ("Double", False, False), ("Double", True, True)])
def test_can_book_room(room, result, expected):
    assert rm.can_book_room(room, result) == expected
