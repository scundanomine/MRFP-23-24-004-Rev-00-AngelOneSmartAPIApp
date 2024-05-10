import pandas as pd
import datetime


def processPastTenCandlesData(uid, rfTime, df, flagZero=False):
    if len(df) == 10 or flagZero:
        df.to_csv(
            f"F:\\AT\\ohlcdata\\ohlcstate\\pasttenohlcdatafiles\\{uid}.csv",
            index=False)
    else:
        dfOne = pd.DataFrame(columns=list(range(6)), index=list(range(10)))
        dfOne[:] = 0
        delta = datetime.timedelta(minutes=1)
        for i in range(10):
            newDateF = rfTime.strftime("%Y-%m-%dT%H:%M:00+05:30")
            dfOne.loc[i, 0] = newDateF
            # query condition
            if len(df.loc[(df['0'] == newDateF)]) != 0:
                dfOne.iloc[i] = df.loc[(df['0'] == newDateF)]
            rfTime = rfTime + delta
        dfOne.to_csv(
            f"F:\\AT\\ohlcdata\\ohlcstate\\pasttenohlcdatafiles\\{uid}.csv",
            index=False)
        # print(dfOne)

# c = getRefDateConstant("30 Oct 2023  09:35:00.000")
# refDate = datetime.datetime.now() - c
# pastTenMinRefDate = refDate - datetime.timedelta(minutes=9)
# dfC = pd.DataFrame(columns=list(range(6)))
# dfC.loc[0] = ["2023-10-30T09:28:00+05:30", 500, 500, 502, 510, 10]
# dfC.loc[1] = ["2023-10-30T09:30:00+05:30", 700, 501, 601, 510, 10]
# dfC.loc[2] = ["2023-10-30T09:34:00+05:30", 600, 500, 802, 550, 10]
# processPastTenCandlesData(21, 20, pastTenMinRefDate, True, dfC)
