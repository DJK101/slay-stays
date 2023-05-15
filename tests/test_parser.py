import pytest
import app.commands as commands
from app.parser import parse_command
from unittest.mock import patch


# NOTE: Only works for testing commands that require no inputs. Specialised tests are made otherwise
@pytest.mark.parametrize("function_name, command", [('help_menu', 'help'),
                                                    ('print_bookings', 'my_bookings'),
                                                    ])
def test_parse_command_to_call_simple_commands(mocker, function_name, command):
    command_function = mocker.spy(commands, function_name)
    parse_command(command)
    assert command_function.call_count == 1


@pytest.mark.parametrize("function_name, command", [('book_room', 'book'),
                                                    ])
def test_parse_command_to_call_book_room(mocker, function_name, command):
    command_function = mocker.spy(commands, function_name)
    with patch('builtins.input', side_effect=['single', 2025, 8, 16]):
        parse_command(command)
    assert command_function.call_count == 1


def test_calling_quit_closes_application():
    with patch('sys.exit') as mock_exit:
        parse_command('quit')
        mock_exit.assert_called_once()


@pytest.mark.parametrize("invalid_command", ['something', 'wow', 'ugh'])
def test_parse_command_prints_error_to_invalid_command(invalid_command):
    with patch('builtins.print') as mock_print:
        parse_command(invalid_command)
        mock_print.assert_called_once_with(f"Sorry, the statement '{invalid_command}' is not a recognised command.")
