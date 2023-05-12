import pytest
import app.commands as commands
from app.parser import parse_command


def test_parse_command(mocker):
    mocker.patch('commands.help')
    help_menu = mocker.commands.help_menu()
    assert help_menu.call_count == 1
