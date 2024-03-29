import pandas as pd
import xlwings as xw
import multiprocessing


def getterUpdateAndSetterExitInputs(row, lock=multiprocessing.Lock()):
    try:
        with lock:
            df = pd.read_csv(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\exit\\exitstate\\ExitInputs.csv")
            uid = row[0]
            df.iloc[uid - 1] = row
            df.to_csv(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\exit\\exitstate\\ExitInputs.csv",
                index=False)
    except Exception as e:
        print(f"Exception while getterUpdateAndSetterExitInputs upper is {e}")
        getterUpdateAndSetterExitInputs(row, lock)
    while True:
        try:
            wb = xw.Book(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            dt = wb.sheets("ExitInput")
            dt.range(f"a{uid + 1}:c{uid + 1}").value = row
            break
        except Exception as e:
            print(f"The exception while getterUpdateAndSetterExitInputs is {e}")


# getterUpdateAndSetterExitInputs([10, 0, 0])
