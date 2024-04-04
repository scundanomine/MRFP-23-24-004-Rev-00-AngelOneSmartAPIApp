from exit.CheckBearishReversalPatternForExit import checkBearishReversalPatternForExit
from exit.CheckBullishReversalPatternForExit import checkBullishReversalPatternForExit
from marketstructure.GetterMarketStructureDf import getterMarketStructureDf


def getFirstItrMarketStrength():
    cdf = getterMarketStructureDf()
    # calculation for EMAs
    for index, row in cdf.iterrows():
        if index != 0:
            if row['mTyp'] == "Bullish":
                if row['g'] == 'green' and row['s'] >= 1:
                    cdf.loc[index, 'st'] = 2
                elif checkBullishReversalPatternForExit(cdf.loc[index - 1, 'bulRP']) and row['g'] == 'green':
                    cdf.loc[index, 'st'] = 3
                elif checkBullishReversalPatternForExit(cdf.loc[index - 1, 'bulRP']) and row['g'] == 'green' and row['roc'] <= -10:
                    cdf.loc[index, 'st'] = 4
                elif row['g'] == 'red' and row['s'] >= 1:
                    cdf.loc[index, 'st'] = 0
                elif checkBearishReversalPatternForExit(cdf.loc[index - 1, 'berRP']) and row['g'] == 'red':
                    cdf.loc[index, 'st'] = 0
                elif checkBearishReversalPatternForExit(cdf.loc[index - 1, 'berRP']) and row['g'] == 'red' and row['roc'] >= 10:
                    cdf.loc[index, 'st'] = -1
                else:
                    cdf.loc[index, 'st'] = 1
            elif row['mTyp'] == "Bearish":
                if row['g'] == 'red' and row['s'] >= 1:
                    cdf.loc[index, 'st'] = -2
                elif checkBearishReversalPatternForExit(cdf.loc[index - 1, 'berRP']) and row['g'] == 'red':
                    cdf.loc[index, 'st'] = -3
                elif checkBearishReversalPatternForExit(cdf.loc[index - 1, 'berRP']) and row['g'] == 'red' and row['roc'] >= 10:
                    cdf.loc[index, 'st'] = -4
                elif row['g'] == 'green' and row['s'] >= 1:
                    cdf.loc[index, 'st'] = 0
                elif checkBullishReversalPatternForExit(cdf.loc[index - 1, 'bulRP']) and row['g'] == 'green':
                    cdf.loc[index, 'st'] = 0
                elif checkBullishReversalPatternForExit(cdf.loc[index - 1, 'bulRP']) and row['g'] == 'green' and row['roc'] <= -10:
                    cdf.loc[index, 'st'] = 1
                else:
                    cdf.loc[index, 'st'] = -1

    cdf.to_csv(
        f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\marketstructure\\marketstate\\MarketStructure.csv",
        index=False)

# getFirstItrMarketStrength()
