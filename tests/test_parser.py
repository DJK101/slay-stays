import pytest
import app.commands as commands
from app.parser import parse_command


def test_parse_command_to_call_help_menu_command(mocker):
    help_menu = mocker.spy(commands, "help_menu")
    parse_command('help')
    assert help_menu.call_count == 1
