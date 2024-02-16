import pandas as pd


def getterCandleDataForForSpecificPidAndDate(pid, date, folderName="positioncandles"):
    try:
        df = pd.read_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{date}\\{folderName}\\{pid}.csv")
        df = df[['time', 'O', 'H', 'L', 'C', 'V', 'atr', 'atrPer', 'g', 's', 't', 'bulRP', 'berRP', 'rsi', 'atrV', 'vs', 'roc', 'um', 'dm']]
    except Exception as e:
        print(f"The exception while getterCandleDataForForSpecificPidAndDate is {e}")
        df = pd.DataFrame(columns=['time', 'O', 'H', 'L', 'C', 'V', 'atr', 'atrPer', 'g', 's', 't', 'bulRP', 'berRP', 'rsi', 'atrV', 'vs', 'roc', 'um', 'dm'], index=list(range(10)))
        df[:] = 0
    srLst = df.to_dict('records')
    return srLst


# print(getterCandleDataForForSpecificPidAndDate(6, "2024-01-25"))
