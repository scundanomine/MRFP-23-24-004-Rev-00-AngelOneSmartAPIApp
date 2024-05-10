from exit.CheckBearishReversalPatternForExit import checkBearishReversalPatternForExit
from exit.CheckBullishReversalPatternForExit import checkBullishReversalPatternForExit
from marketstructure.GetterMarketStructureDf import getterMarketStructureDf


def getAllItrMarketStrength(cdf):
    # cdf = getterMarketStructureDf()
    # calculation for EMAs
    index = 9
    if cdf.loc[index, 'mTyp'] == "Bullish":
        if cdf.loc[index, 'g'] == 'green' and cdf.loc[index, 's'] >= 1:
            cdf.loc[index, 'st'] = 2
        elif checkBullishReversalPatternForExit(cdf.loc[index - 1, 'bulRP']) and cdf.loc[index, 'g'] == 'green':
            cdf.loc[index, 'st'] = 3
        elif checkBullishReversalPatternForExit(cdf.loc[index - 1, 'bulRP']) and cdf.loc[index, 'g'] == 'green' and cdf.loc[index, 'roc'] <= -10:
            cdf.loc[index, 'st'] = 4
        elif cdf.loc[index, 'g'] == 'red' and cdf.loc[index, 's'] >= 1:
            cdf.loc[index, 'st'] = 0
        elif checkBearishReversalPatternForExit(cdf.loc[index - 1, 'berRP']) and cdf.loc[index, 'g'] == 'red':
            cdf.loc[index, 'st'] = 0
        elif checkBearishReversalPatternForExit(cdf.loc[index - 1, 'berRP']) and cdf.loc[index, 'g'] == 'red' and cdf.loc[index, 'roc'] >= 10:
            cdf.loc[index, 'st'] = -1
        else:
            cdf.loc[index, 'st'] = 1
    elif cdf.loc[index, 'mTyp'] == "Bearish":
        if cdf.loc[index, 'g'] == 'red' and cdf.loc[index, 's'] >= 1:
            cdf.loc[index, 'st'] = -2
        elif checkBearishReversalPatternForExit(cdf.loc[index - 1, 'berRP']) and cdf.loc[index, 'g'] == 'red':
            cdf.loc[index, 'st'] = -3
        elif checkBearishReversalPatternForExit(cdf.loc[index - 1, 'berRP']) and cdf.loc[index, 'g'] == 'red' and cdf.loc[index, 'roc'] >= 10:
            cdf.loc[index, 'st'] = -4
        elif cdf.loc[index, 'g'] == 'green' and cdf.loc[index, 's'] >= 1:
            cdf.loc[index, 'st'] = 0
        elif checkBullishReversalPatternForExit(cdf.loc[index - 1, 'bulRP']) and cdf.loc[index, 'g'] == 'green':
            cdf.loc[index, 'st'] = 0
        elif checkBullishReversalPatternForExit(cdf.loc[index - 1, 'bulRP']) and cdf.loc[index, 'g'] == 'green' and cdf.loc[index, 'roc'] <= -10:
            cdf.loc[index, 'st'] = 1
        else:
            cdf.loc[index, 'st'] = -1

    return cdf
    # cdf.to_csv(
    #     f"F:\\AT\\marketstructure\\marketstate\\MarketStructure.csv",
    #     index=False)

# getAllItrMarketStrength()
