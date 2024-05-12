import pandas as pd


def getterReportDate():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\areportstate\\date.csv")
        rDate = df.loc[0, 'date']
    except Exception as e:
        print(f"The exception while getterReportDate is {e}")
        rDate = getterReportDate()
    return rDate

# print(getterReportDate())
