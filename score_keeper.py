

scoreMap = {}

def addScore(points, target):
    scoreMap[target] = scoreMap.get(target, 0) + points

def getScoreForTarget(target):
    return scoreMap.get(target, 0)

def clearAllScores():
    scoreMap.clear()
