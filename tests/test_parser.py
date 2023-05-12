import pytest
from app.parser import parse_command


def test_parse_command(mocker):
    mocker.patch('commands.help')
    parse_command('help')
    assert commands.help.call_count == 1

