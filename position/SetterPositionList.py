import pandas as pd
import xlwings as xw
import multiprocessing


def setterPositionList(df=pd.DataFrame(), lock=multiprocessing.Lock()):
    # getting data from the sheet
    wb = xw.Book("../AngelOneSmartAPIApp/TA_Python.xlsm")
    dt = wb.sheets("Position")

    n = len(df)
    # clear the sheet
    lock.acquire()
    dt.range(f"a2:r{n + 40}").clear_contents()
    lock.release()

    # show the list on excell
    lock.acquire()
    dt.range(f"a1:r{n+1}").options(pd.DataFrame, index=False).value = df

    df.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\position\\positionstate\\PositionList.csv",
        index=False)
    lock.release()
