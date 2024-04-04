from exit.CheckBearishReversalPatternForExit import checkBearishReversalPatternForExit
from exit.CheckBullishReversalPatternForExit import checkBullishReversalPatternForExit
from marketstructure.GetterMarketStructureDf import getterMarketStructureDf


def getAllItrMarketTrend(cdf):
    # cdf = getterMarketStructureDf()
    index = 9
    # calculation for EMAs
    condensateBullishReversal = f"{cdf.loc[index - 1, 'bulRP']}, {cdf.loc[index - 2, 'bulRP']}"
    condensateBearishReversal = f"{cdf.loc[index - 1, 'berRP']}, {cdf.loc[index - 2, 'berRP']}"
    if cdf.loc[index - 1, 'C'] != 0 or cdf.loc[index, 'C'] != 0:
        if (cdf.loc[index, 'QOne'] >= 45 and cdf.loc[index, 'QTwo'] >= 30) or (checkBullishReversalPatternForExit(condensateBullishReversal) and cdf.loc[index, 'g'] == 'green'):
            cdf.loc[index, 'mTyp'] = "Bullish"
        elif cdf.loc[index, 'QOne'] <= -45 and cdf.loc[index, 'QTwo'] <= -30 or (checkBearishReversalPatternForExit(condensateBearishReversal) and cdf.loc[index, 'g'] == 'red'):
            cdf.loc[index, 'mTyp'] = "Bearish"
        elif cdf.loc[index, 'QOne'] >= -30 and cdf.loc[index, 'QOne'] <= 30:
            cdf.loc[index, 'mTyp'] = "SideWise"
        else:
            cdf.loc[index, 'mTyp'] = "NoTradingZone"

    return cdf
    # cdf.to_csv(
    #     f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\marketstructure\\marketstate\\MarketStructure.csv",
    #     index=False)


# getAllItrMarketTrend()
