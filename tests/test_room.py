import datetime
import pytest
import app.room as rm
from freezegun import freeze_time
from unittest.mock import patch


@pytest.fixture
def now():
    return datetime.datetime.now()


@pytest.mark.parametrize("name, capacity, price",
                         [('deluxe', 2, 250), ('superior', 2, 200), ('standard', 2, 110), ('economy', 1, 90)])
def test_get_room(name, capacity, price):
    room = rm.get_room(name)
    assert room is not None if capacity or price else None


@pytest.mark.parametrize("price, capacity, name",
                         [(250, 2, 'deluxe'), (200, 2, 'superior'), (110, 2, 'standard'), (90, 1, 'economy')])
def test_find_price(price, capacity, name):
    price = rm.find_price(price)
    assert price is not None if capacity or name else None


@pytest.mark.parametrize("capacity, price, name",
                         [(2, 250, 'deluxe'), (2, 200, 'superior'), (2, 110, 'standard'), (1, 90, 'economy')])
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


def test_can_book_room(mocker):
    # mocker.patch('app.room.is_sunny_outside', return_value=True)
    # expected = True
    # actual = rm.is_sunny_outside()
    # assert expected == actual

    with patch('app.room.is_sunny_outside', return_value=True):
        assert rm.is_sunny_outside() == True
    with patch('app.room.is_sunny_outside', return_value=False):
        assert rm.is_sunny_outside() == False
    with patch('app.room.is_tuesday', return_value=True):
        assert rm.is_tuesday() == True
    with patch('app.room.is_tuesday', return_value=False):
        assert rm.is_tuesday() == False
    with patch('app.room.is_birthday', return_value=True):
        assert rm.is_birthday() == True
    with patch('app.room.is_birthday', return_value=False):
        assert rm.is_birthday() == False
