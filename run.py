import app.parser as parser

inp = input("Please enter a command ('help' to get a list of commands): ")
parser.parse_command(inp)

while True:
    inp = input("=> ")
    parser.parse_command(inp)
