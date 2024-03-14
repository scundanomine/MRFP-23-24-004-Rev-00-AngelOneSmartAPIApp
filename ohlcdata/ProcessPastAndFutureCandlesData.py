import pandas as pd
import datetime


def processPastAndFutureCandlesData(rfTime, flagZero, data):
    df = pd.DataFrame(data)
    if len(df) == 3 and flagZero is False:
        return df
    else:
        dfOne = pd.DataFrame(columns=list(range(6)), index=list(range(3)))
        dfOne[:] = 0
        delta = datetime.timedelta(minutes=1)
        for i in range(3):
            newDateF = rfTime.strftime("%Y-%m-%dT%H:%M:00+05:30")
            dfOne.loc[i, 0] = newDateF
            try:
                if len(df.loc[(df[0] == newDateF)]) != 0:
                    dfOne.iloc[i] = df.loc[(df[0] == newDateF)]
                rfTime = rfTime + delta
            except Exception as e:
                # print(f"Exception while processPastAndFutureCandlesData is {e}")
                a = e
        return dfOne

