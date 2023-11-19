def checkBearishReversalPattern(patternData):
    patternList = ["Bearish_Engulfing", "shooting_star", "tweezer_top", "dark_cloud_cover", "evening_star"]
    for listItem in patternList:
        if listItem in patternData:
            return True
    return False
