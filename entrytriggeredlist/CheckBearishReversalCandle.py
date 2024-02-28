def checkBearishReversalCandle(candleData):
    candleList = ["doji", "spn_top", "shooting_star", "tweezer_t"]
    for listItem in candleList:
        if listItem in candleData:
            return True
    return False
