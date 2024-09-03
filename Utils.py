# import only system from os
from os import system, name

JSCORES_FILE_NAME = './Scores.json'
TSCORES_FILE_NAME = './Scores.txt'
BAD_RETURN_CODE = 0

def Screen_cleaner():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
