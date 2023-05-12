import app.commands as commands


def parse_command(command: str):
    # Remove trailing whitespace and convert to all lowercase
    command = command.strip().lower()
    if command == 'help':
        commands.help_menu()
