from marketstructure.GetterMarketStructureDf import getterMarketStructureDf
import math


def getFirstItrThitaTwoForNiftyIndex():
    cdf = getterMarketStructureDf()
    # calculation for Qs
    for index, row in cdf.iterrows():
        if index != 0:
            if cdf.loc[index - 1, 'C'] != 0 or row['C'] != 0:
                dyTwo = math.tan(row['QOne'] * math.pi / 180) * 2
                dyOne = math.tan(cdf.loc[index - 1, 'QOne'] * math.pi / 180) * 2
                dzTwo = math.tan(row['QTwo'] * math.pi / 180) * 2
                dzOne = math.tan(cdf.loc[index - 1, 'QTwo'] * math.pi / 180) * 2
                cdf.loc[index, 'QQOne'] = math.atan((dyTwo - dyOne) / 4) * 180 / math.pi
                cdf.loc[index, 'QQTwo'] = math.atan((dzTwo - dzOne) / 4) * 180 / math.pi
    cdf = cdf.round(decimals=2)
    cdf.to_csv(
        f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\marketstructure\\marketstate\\MarketStructure.csv",
        index=False)


# print(getFirstItrThitaTwoForNiftyIndex())
