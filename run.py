import app.parser as parser
from app.login import login

current_user = login()

inp = input("Please enter a command ('help' to get a list of commands): ")
parser.parse_command(inp, current_user)

while True:
    inp = input("=> ")
    parser.parse_command(inp, current_user)
