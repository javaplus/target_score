

scoreMap = {}

def addScore(points, target):
    scoreMap[target] = points

def getScoreForTarget(target):
    return scoreMap[target]