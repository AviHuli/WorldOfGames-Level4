import json
from Utils import *
from os import path
from flask import Flask



def loadData():
    if path.isfile(JSCORES_FILE_NAME) is False:
        raise Exception("File not found")
    else:
        with open(JSCORES_FILE_NAME) as json_file:
            data = json.load(json_file)
            return data
def updatePlayerDatatxt(score):
    with open(TSCORES_FILE_NAME, 'r') as file:
        data = file.read()
        if(len(data)) == 0:
            sr = score
        else:
            sr = score + int(data)

    with open(TSCORES_FILE_NAME, 'w') as file:
        file.write(str(sr))

def listPlayerScores():
    players = loadData()
    for each in range(len(players)):
        print("{} {} Achived Scores {}".format(each+1,players[each].get('pName'), players[each].get('score')))

def updatePlayerData(pName,gName,score):
    players = loadData()
    print(type(players))
    newScores = []
    if (len(players)) == 0:
        str = {"GameName": gName, "PlayerName": pName, gName.replace(" ", "") + "score": score}
        newScores.append(str)
        with open(JSCORES_FILE_NAME, 'w') as f:
            f.write(json.dumps(newScores))
    else:
       i = 0
       while i <len(players):
           each = players[i]
           if (len(players) == 1):
            if (gName == each['GameName']) and (pName == each['PlayerName']):
                #newScores.append(players)
                str = {"GameName": each['GameName'], "PlayerName": each['PlayerName'], gName.replace(" ", "") + "score": int(each[gName.replace(" ", "") + "score"]) + score}
                #print(each[gName.replace(" ", "") + "score"])
                newScores.append(str)
                with open(JSCORES_FILE_NAME, 'w') as f:
                 f.write(json.dumps(newScores))
                i=i+1
            else:
                str1 = {"GameName": each['GameName'], "PlayerName": each['PlayerName'], gName.replace(" ", "") + "score": each[gName.replace(" ", "") + "score"]}
                newScores.append(str1)
                str = {"GameName": gName, "PlayerName": pName, gName.replace(" ", "") + "score": score}
                newScores.append(str)
                with open(JSCORES_FILE_NAME, 'w') as f:
                 f.write(json.dumps(newScores))
                i = i + 1
           else:
            if (gName == each['GameName']) and (pName == each['PlayerName']):
                # newScores.append(players)
                str = {"GameName": each['GameName'], "PlayerName": each['PlayerName'], gName.replace(" ", "") + "score": int(each[gName.replace(" ", "") + "score"]) + score}
                # print(each[gName.replace(" ", "") + "score"])
                #print(players[i])
                players[i] = str
                #print(players[i])
                #newScores.append(players)
                with open(JSCORES_FILE_NAME, 'w') as f:
                 f.write(json.dumps(players))
                i = len(players)
            else:
                i = i + 1
                if i == len(players) :
                    str = {"GameName": gName, "PlayerName": pName, gName.replace(" ", "") + "score": score}
                    players.append(str)
                    with open(JSCORES_FILE_NAME, 'w') as f:
                     f.write(json.dumps(players))
                    i = len(players)

