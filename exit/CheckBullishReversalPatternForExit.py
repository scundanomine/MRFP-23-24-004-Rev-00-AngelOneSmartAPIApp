def checkBullishReversalPatternForExit(patternData):
    patternList = ["Bullish_Engulfing", "hammer", "morning_star"]
    for listItem in patternList:
        if listItem in patternData:
            return True
    return False


# print(checkBullishReversalPatternForExit("Bullish_Engulfing"))
