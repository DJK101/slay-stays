import pytest
from io import StringIO
from app.login_system import find_user, delete_user, create_user


@pytest.fixture
def file():
    return StringIO(
        "username,password\n"
        "dj,100\n"
        "me,pwd\n"
        "amy,rocks\n"
    )


@pytest.mark.parametrize("test_input, expected", [('dj', 0), ('me', 1), ('amy', 2)])
def test_find_user(file, test_input, expected):
    assert find_user(test_input, file) == expected


def test_create_user(file):
    assert False


def test_delete_user(file):
    assert False


