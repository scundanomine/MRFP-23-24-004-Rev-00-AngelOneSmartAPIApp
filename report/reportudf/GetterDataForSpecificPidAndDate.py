import pandas as pd


def getterDataForSpecificPidAndDate(pid, date, folderName="exitdetails"):
    try:
        df = pd.read_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{date}\\{folderName}\\{pid}.csv")
        df = df[['pid', 'id', 'sector', 'symbol', 'token', "ot", "ltp", "lp", "q", "sl", "target", "mr", "tOP", "tOEx", "gol", 'oc', "po", "slo", "to", 'rFlag', 'eFlag', "tOEP", 'ltpP']]
    except Exception as e:
        print(f"The exception while getterDataForSpecificPidAndDate is {e}")
        df = pd.DataFrame(columns=['pid', 'id', 'sector', 'symbol', 'token', "ot", "ltp", "lp", "q", "sl", "target", "mr", "tOP", "tOEx", "gol", 'oc', "po", "slo", "to", 'rFlag', 'eFlag', "tOEP", 'ltpP'], index=[0])
        df[:] = 0
        df.loc[0, 'pid'] = pid
    srLst = df.to_dict('records')
    return srLst[0]


# print(getterDataForSpecificPidAndDate(6, "2024-01-25"))
