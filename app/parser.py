import app.commands as commands

keywords = ['help', 'book', 'my_bookings', 'change']


def parse_command(command: str):
    # Remove trailing whitespace and convert to all lowercase
    command = command.strip().lower()
    if command == keywords[0]:
        commands.help_menu()
