import pandas as pd
import xlwings as xw


def getCustomDfGainerOrLoser():
    # startTime = time.time()
    while True:
        try:
            wb = xw.Book(
                "F:\\AT\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            dt = wb.sheets("MAndP")
            df = pd.DataFrame(dt.range(f"m2:m3").value, columns=["GL"])
            df = df.astype("int64")
            break
        except Exception as e:
            print(f"Exception while GetCustomDfGainerOrLoser is {e}")
    return df


# print(getCustomDfGainerOrLoser())
