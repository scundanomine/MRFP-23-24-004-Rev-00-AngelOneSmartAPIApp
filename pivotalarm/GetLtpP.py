import pandas as pd
import xlwings as xw


def loadLtpP():
    def getLtpP():
        wb = xw.Book("../AngelOneSmartAPIApp/TA_Python.xlsm")
        dt = wb.sheets("Exchange")
        ltpX = pd.DataFrame(dt.range("e1:e202").value)
        ltpX.columns = ltpX.iloc[0]
        ltpX = ltpX[1:]
        ltpX.to_csv("pivot.csv", index=False)
        return ltpX

    while True:
        try:
            with open(f"pivot.csv", "r") as f:
                ltpP = pd.read_csv("pivot.csv")
            break
        except:
            ltpP = getLtpP()
    return ltpP


# print(loadLtpP())
