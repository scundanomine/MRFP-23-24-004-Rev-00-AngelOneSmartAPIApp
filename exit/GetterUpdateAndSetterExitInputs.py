import pandas as pd
import xlwings as xw


def getterUpdateAndSetterExitInputs(uid, row, lock):
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\BlackListET.csv")
        df.iloc[uid - 1] = row
        df.to_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\BlackListET.csv",
            index=False)
        wb = xw.Book(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
        dt = wb.sheets("ExitInputs")
    except Exception as e:
        print(f"The exception while getter, update and setter ET black list is {e}")
