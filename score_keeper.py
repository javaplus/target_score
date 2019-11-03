import json


scoreMap = {}
FILENAME ="score.json"

def addScore(points, target):
    scoreMap[target] = scoreMap.get(target, 0) + points
    scoreMapAsJSON = json.dumps(scoreMap)
    f = open(FILENAME,"w")
    f.write(scoreMapAsJSON)
    f.close()


def getScoreForTarget(target):
    with open(FILENAME) as json_file:
        scoreMap = json.load(json_file)
    return scoreMap.get(target, 0)

def clearAllScores():
    scoreMap.clear()
    scoreMapAsJSON = json.dumps(scoreMap)
    f = open(FILENAME,"w")
    f.write(scoreMapAsJSON)
    f.close()
