import app.parser as parser

while True:
    inp = input("Please enter a command: ('help') to get a list of commands ")
    parser.parse_command(inp)
