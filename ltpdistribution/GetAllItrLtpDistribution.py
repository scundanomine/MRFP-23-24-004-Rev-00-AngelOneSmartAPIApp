import datetime
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList
from commonudm.GetterTimeDelta import getterTimeDelta
from ltpdistribution.GetBearishCandleLtpDistribution import getBearishCandleLtpDistribution
from ltpdistribution.GetBullishCandleLtpDistribution import getBullishCandleLtpDistribution
from ltpdistribution.GetterSpecificDistributionDf import getterSpecificDistributionDf
from ohlcdata.GetterFFDS import getterFFDS


def getAllItrLtpDistribution():
    cv = getterTimeDelta()
    exitTime = getterExitTime()
    while datetime.datetime.now() - cv < exitTime:
        gDf = getterRequiredSymbolAndTokenList()
        fFds = getterFFDS()
        for index, row in gDf.iterrows():
            uid = row['id']
            ldDf = getterSpecificDistributionDf("specificdistributiondf", uid)
            rowX = fFds.iloc[uid - 1]
            if rowX['0'] != ldDf.loc[2, "time"]:
                # queue operation for ltp distribution
                ldDf = ldDf.drop(0, axis=0)
                ldDf.index = list(range(2))
                ldDf.loc[len(ldDf)] = 0
                idx = 2
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
