import pytest
import app.commands as commands
import app.parser as parser
from unittest.mock import patch


# NOTE: Only works for testing commands that require no inputs. Specialised tests are made otherwise
@pytest.mark.parametrize("function_name, command", [('help_menu', 'help'),
                                                    ('print_bookings', 'my_bookings'),
                                                    ])
def test_parse_command_to_call_simple_commands(mocker, function_name, command):
    command_function = mocker.spy(commands, function_name)
    parser.parse_command(command)
    assert command_function.call_count == 1


def test_parse_command_to_call_book_room(mocker):
    book_room_spy = mocker.spy(commands, 'book_room')
    with patch('builtins.input', return_value=''):  # Invalid input for book_room, function won't add values
        parser.parse_command('book')
    assert book_room_spy.call_count == 1


def test_calling_quit_closes_application():
    with patch('sys.exit') as mock_exit:
        parser.parse_command('quit')
        mock_exit.assert_called_once()


@pytest.mark.parametrize("invalid_command", ['something', 'wow', 'ugh'])
def test_parse_command_prints_error_to_invalid_command(invalid_command):
    with patch('builtins.print') as mock_print:
        parser.parse_command(invalid_command)
        mock_print.assert_called_once_with(f"Sorry, the statement '{invalid_command}' is not a recognised command.")
