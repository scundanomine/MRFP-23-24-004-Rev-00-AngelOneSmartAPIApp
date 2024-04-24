import datetime
import pandas as pd
from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList
from commonudm.GetterTimeDelta import getterTimeDelta
from ltpdistribution.GetLtpDistributionWithQuery import getLtpDistributionWithQuery


def getFirstItrLtpDistribution():
    # startTime = time.time()
    # date calculation
    cv = getterTimeDelta()
    date = datetime.datetime.today() - cv
    date = date.strftime("%Y-%m-%d")
    gDf = getterRequiredSymbolAndTokenList()
    currentDateTime = datetime.datetime.now() - cv
    fromDateTime = currentDateTime + datetime.timedelta(minutes=1)
    toDateTime = currentDateTime + datetime.timedelta(minutes=4)
    for index, row in gDf.iterrows():
        uid = row['id']
        df = getLtpDistributionWithQuery(fromDateTime, toDateTime, uid, date)
        if len(df) == 3:
            df.to_csv(
                f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ltpdistribution\\ltpdistributionstate\\specificdistributiondf\\{uid}.csv")
        else:
            cdf = pd.DataFrame(columns=list(range(60)), index=list(range(3)))
            cdf[:] = 0
            tOne = fromDateTime.strftime("%Y-%m-%d %H:%M:00")
            tTwo = fromDateTime + datetime.timedelta(minutes=1)
            tTwo = tTwo.strftime("%Y-%m-%d %H:%M:00")
            tThree = fromDateTime + datetime.timedelta(minutes=2)
            tThree = tThree.strftime("%Y-%m-%d %H:%M:00")
            tList = [tOne, tTwo, tThree]
            cdf.insert(0, 'time', 0)
            cdf['time'] = tList
            df = df.reset_index()
            df.index = list(range(len(df)))
            for i in range(3):
                if len(df.loc[df['time'] == tList[i]]) != 0:
                    cdf.iloc[i] = df.loc[df['time'] == tList[i]]
            cdf.to_csv(
                f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ltpdistribution\\ltpdistributionstate\\specificdistributiondf\\{uid}.csv",
                index=False)
    # print(time.time() - startTime)


getFirstItrLtpDistribution()
