import pandas as pd
from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList
from historicdata.GetterSpecificHistoricData import getterSpecificHistoricData
from ltpdistribution.GetBearishCandleLtpDistribution import getBearishCandleLtpDistribution
from ltpdistribution.GetBullishCandleLtpDistribution import getBullishCandleLtpDistribution


def getLtpDistributionForAllCandles(date):
    # startTime = time.time()
    gDf = getterRequiredSymbolAndTokenList()
    for index, row in gDf.iterrows():
        uid = row['id']
        daDf = getterSpecificHistoricData(date, uid)
        dfSize = len(daDf)
        ldDf = pd.DataFrame(columns=list(range(60)), index=list(range(dfSize)))
        ldDf.index = daDf.index
        ldDf[:] = 0
        for idx, rowX in daDf.iterrows():
            if rowX['4'] != 0:
                if rowX['1'] <= rowX['4']:  # for bullish candle
                    ltpLst = getBullishCandleLtpDistribution(rowX)
                    ldDf.loc[idx] = ltpLst
                else:  # for bearish candle
                    ltpLst = getBearishCandleLtpDistribution(rowX)
                    ldDf.loc[idx] = ltpLst
        ldDf.to_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ltpdistribution\\ltpdistributionstate\\allcandledistributiondf\\{date}\\{uid}.csv")
    # print(time.time()-startTime)


# getLtpDistributionForAllCandles(date)
