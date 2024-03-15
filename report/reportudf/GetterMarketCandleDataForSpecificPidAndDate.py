import pandas as pd


def getterMarketCandleDataForSpecificPidAndDate(pid, date, folderName="positionmcandles"):
    try:
        df = pd.read_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{date}\\{folderName}\\{pid}.csv")
    except Exception as e:
        print(f"The exception while getterCandleDataForForSpecificPidAndDate is {e}")
        df = pd.DataFrame(columns=['time', 'O', 'H', 'L', 'C', 'V', 'atr', 'atrPer', 'g', 's', 't', 'bulRP', 'berRP', 'atrV', 'vs', 'roc', 'um', 'dm', 'rsi', 'emaOne', 'emaTwo', 'QOne', 'QTwo', 'QQOne', 'QQTwo', 'mTyp'], index=list(range(10)))
        df[:] = 0
    srLst = df.to_dict('records')
    return srLst


# print(getterMarketCandleDataForSpecificPidAndDate(6, "2024-01-25"))
