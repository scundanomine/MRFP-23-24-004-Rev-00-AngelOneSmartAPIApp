import pandas as pd


def getterReportDateForRR():
    try:
        df = pd.read_csv(
            "F:\\AT\\commonudm\\resource\\ReportDate.csv")
    except Exception as e:
        print(f"The exception while getter getterReportDateForRR is {e}")
        df = getterReportDateForRR()
    return df.loc[0, 'rDate']


# print(getterReportDateForRR())
