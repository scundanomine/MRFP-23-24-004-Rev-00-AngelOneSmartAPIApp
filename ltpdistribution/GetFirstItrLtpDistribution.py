from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList
from ltpdistribution.GetBearishCandleLtpDistribution import getBearishCandleLtpDistribution
from ltpdistribution.GetBullishCandleLtpDistribution import getBullishCandleLtpDistribution
from ltpdistribution.GetterSpecificDistributionDf import getterSpecificDistributionDf


def getFirstItrLtpDistribution():
    gDf = getterRequiredSymbolAndTokenList()
    for index, row in gDf.iterrows():
        uid = row['id']
        daDf = getterSpecificDistributionDf("specificohlcdf", uid)
        ldDf = getterSpecificDistributionDf("specificdistributiondf", uid)
        for idx, rowX in daDf.iterrows():
            if rowX['4'] != 0:
                if rowX['0'] <= rowX['4']:  # for bullish candle
                    ltpLst = getBullishCandleLtpDistribution(rowX)
                    ldDf[idx] = ltpLst
                else:  # for bearish candle
                    ltpLst = getBearishCandleLtpDistribution(rowX)
                    ldDf[idx] = ltpLst
            else:
                ldDf[idx, 'time'] = rowX["0"]
        ldDf.to_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ltpdistribution\\ltpdistributionstate\\specificdistributiondf\\{uid}.csv",
            index=False)