import datetime
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList
from commonudm.GetterTimeDelta import getterTimeDelta
from ltpdistribution.GetBearishCandleLtpDistribution import getBearishCandleLtpDistribution
from ltpdistribution.GetBullishCandleLtpDistribution import getBullishCandleLtpDistribution
from ltpdistribution.GetLtpDistributionWithQuery import getLtpDistributionWithQuery
from ltpdistribution.GetterSpecificDistributionDf import getterSpecificDistributionDf
from ohlcdata.GetterFFDS import getterFFDS


def getAllItrLtpDistribution():
    cv = getterTimeDelta()
    exitTime = getterExitTime()
    date = datetime.datetime.today() - cv
    date = date.strftime("%Y-%m-%d")
    while datetime.datetime.now() - cv < exitTime:
        gDf = getterRequiredSymbolAndTokenList()
        futureDateTime = datetime.datetime.now() - cv + datetime.timedelta(minutes=4)
        reqTime = futureDateTime.strftime("%Y-%m-%d %H:%M")
        for index, row in gDf.iterrows():
            uid = row['id']
            ldDf = getterSpecificDistributionDf("specificdistributiondf", uid)
            refTime = ldDf.loc[2, 'time']
            if refTime != reqTime:
                # queue operation for ltp distribution
                ldDf = ldDf.drop(0, axis=0)
                ldDf.index = list(range(2))
                ldDf.loc[len(ldDf)] = 0
                ldDf.loc[2, 'time'] = reqTime
                # get data from query
                df = getLtpDistributionWithQuery(futureDateTime, futureDateTime, uid, date)
                df = df.reset_index()
                if len(df.loc[df['time'] == reqTime]) != 0:
                    ldDf.iloc[2] = df.loc[df['time'] == reqTime]
                ldDf.to_csv(
                    f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ltpdistribution\\ltpdistributionstate\\specificdistributiondf\\{uid}.csv")
