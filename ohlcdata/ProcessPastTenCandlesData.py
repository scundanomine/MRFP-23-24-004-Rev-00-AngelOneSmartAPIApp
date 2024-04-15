import pandas as pd
import datetime


def processPastTenCandlesData(uid, a, rfTime, flagZero, df=pd.DataFrame(columns=list(range(6)), index=list(range(13)))):
    if len(df) == 13 and flagZero is False:
        dfx = df[:10]
        dfy = df[10:]
        dfx.to_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ohlcdata\\ohlcstate\\pasttenohlcdatafiles\\{uid}_{a}.csv",
            index=False)
        dfy.to_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ltpdistribution\\ltpdistributionstate\\specificohlcdf\\{uid}.csv",
            index=False)
    else:
        dfOne = pd.DataFrame(columns=list(range(6)), index=list(range(13)))
        dfOne[:] = 0
        delta = datetime.timedelta(minutes=1)
        for i in range(13):
            newDateF = rfTime.strftime("%Y-%m-%dT%H:%M:00+05:30")
            dfOne.loc[i, 0] = newDateF
            # query condition
            if len(df.loc[(df[0] == newDateF)]) != 0:
                dfOne.iloc[i] = df.loc[(df[0] == newDateF)]
            rfTime = rfTime + delta
        dfx = dfOne[:10]
        dfy = dfOne[10:]
        dfx.to_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ohlcdata\\ohlcstate\\pasttenohlcdatafiles\\{uid}_{a}.csv",
            index=False)
        dfy.to_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ltpdistribution\\ltpdistributionstate\\specificohlcdf\\{uid}.csv",
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
