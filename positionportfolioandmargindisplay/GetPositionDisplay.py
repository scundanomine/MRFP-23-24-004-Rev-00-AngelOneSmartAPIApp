import pandas as pd
import xlwings as xw
import multiprocessing


def displayPositionList(lock=multiprocessing.Lock()):
    # getting data from the sheet
    wb = xw.Book(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
    dt = wb.sheets("Position")

    try:
        lock.acquire()
        dfC = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\position\\positionstate\\PositionList.csv")
        m = len(dfC)
        dt.range(f"a1:u{m + 4}").clear_contents()
        dt.range(f"a1:u{m + 1}").options(pd.DataFrame, index=False).value = dfC
        lock.release()
    except Exception as e:
        print(f"The exception while display position is {e}")


# displayPositionList()
