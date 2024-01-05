import xlwings as xw
import pandas as pd
import multiprocessing


def getCustomDfGainerOrLoser(lock=multiprocessing.Lock()):
    # startTime = time.time()
    while True:
        try:
            with lock:
                wb = xw.Book(
                    "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
                dt = wb.sheets("MAndP")
                df = pd.DataFrame(dt.range(f"m2:m3").value, columns=["GL"])
            df = df.astype("int64")
            break
        except Exception as e:
            print(f"Exception while GetCustomDfGainerOrLoser is {e}")
    return df


# print(getCustomDfGainerOrLoser())
