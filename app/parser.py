import app.commands as commands
from app.commands import keywords


def parse_command(command: str):
    # Remove trailing whitespace and convert to all lowercase
    command = command.strip().lower()
    if command == keywords[0]:
        commands.help_menu()
    elif command == keywords[1]:
        commands.shut_down()
    elif command == keywords[2]:
        pass
