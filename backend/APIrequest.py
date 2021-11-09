import json
import requests
from time import sleep

response = requests.get("http://127.0.0.1:6721/session")
jsonData = response.json()


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


    # If Game Status is 'Score' Proceed with Disc Location Updates
    while True:
        r = requests.get("http://127.0.0.1:6721/session")
        rdata = r.json()
        gameStatus = rdata['game_status']

        # If score, get data
        if gameStatus == 'score':
            lastScore = rdata['last_score']['disc_speed']
            sleep(12)
        
        # If post/pre match pause sleep.
        elif gameStatus == 'post_match' or 'pre_match':
            print("Current in post/pre match please wait!")
            sleep(15)

        # Continue repeating until score.
        elif gameStatus == 'playing':
            sleep(12)
        else:
            print("error encountered")
            break



    blueStats = {
        "players" : blueNames
    }
    orangeStats = {
        "players" : orangeNames
    }
    gameStats = {
        "last_score" : lastScore
    }
    return blueStats, orangeStats, gameStats



getUserInfo(jsonData)
