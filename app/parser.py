import app.commands as commands


def parse_command(command: str):
    # Remove trailing whitespace if any
    command = command.strip()
    if command == 'help':
        commands.help_menu()
