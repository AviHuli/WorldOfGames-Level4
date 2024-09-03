import json
from os import path

filename = './Scores.json'
playerList = []
class Players(object):
    gName = ""
    name = ""
    score = 0
    numberOfGames = 0


def readFromJason():
    if path.isfile(filename) is False:
        raise Exception("File not found")

    with open(filename) as fp:
        playerList = json.load(fp)

    print(playerList)

def writeNameToJason(pName):
    # Check if file exists
    if path.isfile(filename) is False:
        raise Exception("File not found")

    # Read JSON file
    with open(filename) as fp:
        playerList = json.load(fp)
    size = len(playerList)
    print(size)
    if not playerList:
        Players.gName = "Memory Game"
        Players.name = pName
        Players.score = 0
        Players.numberOfGames = 0

        playerList.append(Players)
    else:
        print("not exist")

    print(playerList)
    with open(filename, 'w') as json_file:
        json.dump(playerList, json_file,
                  indent=4,
                  separators=(',', ': '))

    print('Successfully appended to the JSON file')