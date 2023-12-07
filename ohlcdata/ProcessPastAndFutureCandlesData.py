import pandas as pd
import datetime


def processPastAndFutureCandlesData(rfTime, flagZero, data):
    df = pd.DataFrame(data)
    if len(df) == 2 and flagZero is False:
        return df
    else:
        dfOne = pd.DataFrame(columns=list(range(6)), index=list(range(2)))
        dfOne[:] = 0
        delta = datetime.timedelta(minutes=1)
        for i in range(2):
            newDateF = rfTime.strftime("%Y-%m-%dT%H:%M:00+05:30")
            dfOne.loc[i, 0] = newDateF
            if len(df.loc[(df[0] == newDateF)]) != 0:
                dfOne.iloc[i] = df.loc[(df[0] == newDateF)]
            rfTime = rfTime + delta
        return dfOne

