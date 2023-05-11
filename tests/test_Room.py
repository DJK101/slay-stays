from app.Room import is_djs_birthday, random_bool, is_sunny_outside, is_raining_outside, is_snowing_outside, is_tuesday, \
    is_wednesday, is_my_birthday, is_rosies_birthday, find_room, find_price, find_capacity


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
    for i in range(0, 100):
        assert random_bool() in [True, False]


def test_is_sunny_outside():
    for i in range(0, 100):
        assert is_sunny_outside() in [True, False]


def test_is_raining_outside():
    for i in range(0, 100):
        assert is_raining_outside() in [True, False]


def test_is_snowing_outside():
    for i in range(0, 100):
        assert is_snowing_outside() in [True, False]


def test_is_tuesday():
    assert is_tuesday() in [True, False]


def test_is_wednesday():
    assert is_wednesday() in [True, False]


def test_is_my_birthday():
    assert is_my_birthday() in [True, False]


def test_is_rosies_birthday():
    assert is_rosies_birthday() in [True, False]


def test_is_djs_birthday():
    assert is_djs_birthday() in [True, False]
