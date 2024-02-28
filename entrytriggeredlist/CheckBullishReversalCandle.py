def checkBullishReversalCandle(candleData):
    candleList = ["doji", "spn_top", "hammer", "tweezer_b"]
    for listItem in candleList:
        if listItem in candleData:
            return True
    return False
