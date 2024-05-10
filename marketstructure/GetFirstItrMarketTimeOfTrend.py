from marketstructure.GetterMarketStructureDf import getterMarketStructureDf


def getFirstItrMarketTimeOfTrend():
    cdf = getterMarketStructureDf()
    # calculation for EMAs
    for index, row in cdf.iterrows():
        if index != 0:
            if cdf.loc[index - 1, 'C'] != 0 or row['C'] != 0:
                if row['mTyp'] != cdf.loc[index - 1, 'mTyp']:
                    cdf.loc[index, 'trT'] = 0
                else:
                    cdf.loc[index, 'trT'] = cdf.loc[index - 1, 'trT'] + 1

    cdf.to_csv(
        f"F:\\AT\\marketstructure\\marketstate\\MarketStructure.csv",
        index=False)


# getFirstItrMarketTimeOfTrend()
