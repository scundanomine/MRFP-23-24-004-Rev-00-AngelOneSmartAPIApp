from exit.CheckBearishReversalPatternForExit import checkBearishReversalPatternForExit
from exit.CheckBullishReversalPatternForExit import checkBullishReversalPatternForExit
from marketstructure.GetterMarketStructureDf import getterMarketStructureDf


def getFirstItrMarketTrend():
    cdf = getterMarketStructureDf()
    # calculation for EMAs
    for index, row in cdf.iterrows():
        if index != 0:
            if cdf.loc[index - 1, 'C'] != 0 or row['C'] != 0:
                if (row['QOne'] >= 45 and row['QTwo'] >= 30) or (checkBullishReversalPatternForExit(cdf.loc[index - 1, 'bulRP']) and row['g'] == 'green'):
                    cdf.loc[index, 'mTyp'] = "Bullish"
                elif row['QOne'] <= -45 and row['QTwo'] <= -30 or (checkBearishReversalPatternForExit(cdf.loc[index - 1, 'berRP']) and row['g'] == 'red'):
                    cdf.loc[index, 'mTyp'] = "Bearish"
                elif row['QOne'] >= -30 and row['QOne'] <= 30:
                    cdf.loc[index, 'mTyp'] = "SideWise"
                else:
                    cdf.loc[index, 'mTyp'] = "NTZ"

    cdf.to_csv(
        f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\marketstructure\\marketstate\\MarketStructure.csv",
        index=False)


# getFirstItrMarketTrend()
