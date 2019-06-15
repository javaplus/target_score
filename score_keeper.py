

scoreMap = {}

def addScore(points, target):
    scoreMap[target] = scoreMap.get(target, 0) + points

def getScoreForTarget(target):
    return scoreMap[target]

def clearAllScores():
    scoreMap.clear()
