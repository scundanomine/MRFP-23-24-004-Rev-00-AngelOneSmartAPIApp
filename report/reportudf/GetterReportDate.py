import pandas as pd


def getterReportDate():
    try:
        df = pd.read_csv(
            "F:\\AT\\report\\areportstate\\date.csv")
        rDate = df.loc[0, 'date']
    except Exception as e:
        print(f"The exception while getterReportDate is {e}")
        rDate = getterReportDate()
    return rDate

# print(getterReportDate())
