import xlwings as xw
import pandas as pd
import multiprocessing


def getterCreditAndSetterAvailableMargin(mr, lock=multiprocessing.Lock()):
    try:
        lock.acquire()
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\margin\\marginstate\\margin.csv")
        lock.release()
        df.loc[0, 'margin'] = df.loc[0, 'margin'] + mr
        # wb = xw.Book(
        #     "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
        # # MAndP is margin and portfolio list
        # dt = wb.sheets("MAndP")
        # dt.range("a1:a2").options(pd.DataFrame, index=False).value = df
        lock.acquire()
        df.to_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\margin\\marginstate\\margin.csv",
            index=False)
        lock.release()
    except Exception as e:
        print(f"The exception while getter, credit and setter available margin is {e}")


# getterCreditAndSetterAvailableMargin(50000)
