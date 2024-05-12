import pandas as pd


def getterReportDateForRR():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\commonudm\\resource\\ReportDate.csv")
    except Exception as e:
        print(f"The exception while getter getterReportDateForRR is {e}")
        df = getterReportDateForRR()
    return df.loc[0, 'rDate']


# print(getterReportDateForRR())
