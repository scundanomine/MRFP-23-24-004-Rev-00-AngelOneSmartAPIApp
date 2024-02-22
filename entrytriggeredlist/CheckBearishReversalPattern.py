def checkBearishReversalPattern(patternData):
    patternList = ["Bearish_Engulfing", "shooting_star", "evening_star"]
    for listItem in patternList:
        if listItem in patternData:
            return True
    return False
