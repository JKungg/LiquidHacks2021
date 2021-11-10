import json
import requests
from time import sleep
import goalHeatmap

response = requests.get("http://127.0.0.1:6721/session")
jsonData = response.json()


discPos = {'X' : None, 'Y' : None} # Initialize Dict


def getUserInfo(d):

# Filter through blue player stats.
    blueTeam = d['teams'][0]
    blueNames = {}
    for x in range(len(blueTeam)-1):
        # Get Blue Player Names
        bName = blueTeam['players'][x]['name']
        blueNames[f"player{x}"] = bName


# Filter through orange player stats.
    orangeTeam = d['teams'][1]
    orangeNames = {}
    for x in range(len(orangeTeam)-1):
        # Get Orange Player Names
        oName = orangeTeam['players'][x]['name']
        orangeNames[f"player{x}"] = oName


    blueStats = {
        "players" : blueNames
    }
    orangeStats = {
        "players" : orangeNames
    }
    return blueStats, orangeStats


def getDiscPos(rdata):
    # Get Disc Position from API
    discPos0 = rdata['disc']['position'][0] # x POS
    discPos1 = rdata['disc']['position'][1] # y POS
    goalHeatmap.saveGoalPos()
    return discPos0, discPos1


def getScoreData():
    # If Game Status is 'Score' Proceed with Disc Location Updates
    while True:
        r = requests.get("http://127.0.0.1:6721/session")
        rdata = r.json()
        gameStatus = rdata['game_status']
        # print(gameStatus)

        # If score, get data
        if gameStatus == 'score':
            lastScore = rdata['last_score']['disc_speed']
            getDiscPos(rdata)
            sleep(18)
        
        # If post/pre match pause sleep.
        elif gameStatus == 'post_match' or gameStatus == 'pre_match':
            sleep(12)
            continue

        # Continue repeating until score.
        elif gameStatus == 'playing' or gameStatus == 'round_start':
            sleep(5)
            continue
        # elif gameStatus == ''
        else:
            print("error encountered")
            break
    return rdata, lastScore



# getUserInfo(jsonData)
getScoreData()