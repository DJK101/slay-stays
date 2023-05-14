import app.commands as cmds
from app.commands import keywords


def parse_command(command: str, username: str):
    # Remove trailing whitespace and convert to all lowercase
    command = command.strip().lower()
    if command == keywords[0]:
        cmds.help_menu()
    elif command == keywords[1]:
        cmds.shut_down()
    elif command == keywords[2]:
        cmds.register_user()
    else:
        print(f"Sorry, the statement {command} is not a recognised entry.")
