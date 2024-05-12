from exit.CheckBearishReversalPatternForExit import checkBearishReversalPatternForExit
from exit.CheckBullishReversalPatternForExit import checkBullishReversalPatternForExit
from marketstructure.GetterMarketStructureDf import getterMarketStructureDf


def getAllItrMarketTrendWithWeightedAvg(cdf):
    # cdf = getterMarketStructureDf()
    index = 9
    # calculation for EMAs
    condensateBullishReversal = cdf.loc[index - 1, 'bulRP']
    condensateBearishReversal = cdf.loc[index - 1, 'berRP']
    eqQOne = cdf.loc[index, 'QOne'] + cdf.loc[index-1, 'QOne']/2 + cdf.loc[index-2, 'QOne']/4 + cdf.loc[index-3, 'QOne']/8
    if cdf.loc[index - 1, 'C'] != 0 or cdf.loc[index, 'C'] != 0:
        if eqQOne >= 45 or (condensateBullishReversal == "Bullish_Engulfing" and cdf.loc[index, 'g'] == 'green'):
            cdf.loc[index, 'mTyp'] = "Bullish"
        elif eqQOne <= -45 or (condensateBearishReversal == "Bearish_Engulfing" and cdf.loc[index, 'g'] == 'red'):
            cdf.loc[index, 'mTyp'] = "Bearish"
        elif cdf.loc[index, 'g'] == 'green' and cdf.loc[index - 1, 'g'] == 'green' and cdf.loc[index - 2, 'g'] == 'green':
            cdf.loc[index, 'mTyp'] = "Bullish"
        elif cdf.loc[index, 'g'] == 'red' and cdf.loc[index - 1, 'g'] == 'red' and cdf.loc[index - 2, 'g'] == 'red':
            cdf.loc[index, 'mTyp'] = "Bearish"
        elif -30 <= eqQOne <= 30:
            cdf.loc[index, 'mTyp'] = "SideWise"
        else:
            cdf.loc[index, 'mTyp'] = "NTZ"

    return cdf
    # cdf.to_csv(
    #     f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\marketstructure\\marketstate\\MarketStructure.csv",
    #     index=False)


# getAllItrMarketTrend()
