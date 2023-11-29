import pandas as pd
import xlwings as xw


def setterPositionList(df=pd.DataFrame()):
    # getting data from the sheet
    wb = xw.Book("../AngelOneSmartAPIApp/TA_Python.xlsm")
    dt = wb.sheets("Position")

    n = len(df)
    # clear the sheet
    dt.range(f"a2:r{n + 40}").clear_contents()

    # show the list on excell
    dt.range(f"a1:r{n+1}").options(pd.DataFrame, index=False).value = df

    df.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\position\\positionstate\\PositionList.csv",
        index=False)
