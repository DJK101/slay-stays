import app.commands as commands
from app.commands import keywords


def parse_command(command: str):
    # Remove trailing whitespace and convert to all lowercase
    command = command.strip().lower()
    if command == keywords[0]:
        commands.help_menu()
