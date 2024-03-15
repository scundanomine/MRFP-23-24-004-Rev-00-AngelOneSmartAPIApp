from marketstructure.GetterMarketStructureDf import getterMarketStructureDf
import math


def getFirstItrThitaOneForNiftyIndex():
    cdf = getterMarketStructureDf()
    # calculation for EMAs
    for index, row in cdf.iterrows():
        if index != 0:
            if cdf.loc[index - 1, 'C'] != 0 or row['C'] != 0:
                cdf.loc[index, 'QOne'] = math.atan((row['emaOne'] - cdf.loc[index - 1, 'emaOne']) / 2) * 180 / math.pi
                cdf.loc[index, 'QTwo'] = math.atan((row['emaTwo'] - cdf.loc[index - 1, 'emaTwo']) / 2) * 180 / math.pi

    cdf.to_csv(
        f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\marketstructure\\marketstate\\MarketStructure.csv",
        index=False)


# print(getFirstItrThitaOneForNiftyIndex())
