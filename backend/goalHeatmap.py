import APIrequest as api
import matplotlib.pyplot as plt
import numpy as np

discPos = {}
def saveGoalPos():
    x, y = api.getDiscPos()
    discPos[x] = y
    return discPos


def showGoalPos():
    x  = discPos[0]
    y = discPos[1]
    plt.scatter(x, y)
    plt.show()

showGoalPos()