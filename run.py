import app.parser as parser
import app.login as login

login.set_current_user(login.login())

inp = input(f"Welcome {login.get_current_user()}, please enter a command ('help' to get a list of commands) => ")
parser.parse_command(inp, login.get_current_user())

while True:
    inp = input("=> ")
    parser.parse_command(inp, login.get_current_user())
