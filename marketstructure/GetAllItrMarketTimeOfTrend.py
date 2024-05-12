from marketstructure.GetterMarketStructureDf import getterMarketStructureDf


def getAllItrMarketTimeOfTrend(cdf):
    # cdf = getterMarketStructureDf()
    # calculation for EMAs
    index = 9
    if index != 0:
        if cdf.loc[index - 1, 'C'] != 0 or cdf.loc[index, 'C'] != 0:
            if cdf.loc[index, 'mTyp'] != cdf.loc[index - 1, 'mTyp']:
                cdf.loc[index, 'trT'] = 0
            else:
                cdf.loc[index, 'trT'] = cdf.loc[index - 1, 'trT'] + 1

    return cdf
    # cdf.to_csv(
    #     f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\marketstructure\\marketstate\\MarketStructure.csv",
    #     index=False)


# getAllItrMarketTimeOfTrend()
