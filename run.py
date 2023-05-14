import app.parser as parser

current_user = 'dj'

inp = input("Please enter a command ('help' to get a list of commands): ")
parser.parse_command(inp, current_user)

while True:
    inp = input("=> ")
    parser.parse_command(inp, current_user)
