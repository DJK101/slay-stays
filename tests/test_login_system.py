import pytest
from io import StringIO
import app.login_system as login


@pytest.fixture
def file():
    return StringIO(
        "username,password\n"
        "dj,100\n"
        "me,pwd\n"
        "amy,rocks\n"
    )


@pytest.mark.parametrize("test_input, expected", [('dj', 0), ('me', 1), ('amy', 2), ('john', -1)])
def test_find_user(file, test_input, expected):
    assert login.find_user(test_input, file) == expected


def test_create_user(file):
    assert False


@pytest.mark.parametrize("test_input, expected", [('dj', True), ('me', True), ('amy', True)])
def test_delete_user(file, test_input, expected):
    assert login.delete_user(test_input, file) == expected


def test_check_password(file):
    assert login.check_password('dj', '100', file)
