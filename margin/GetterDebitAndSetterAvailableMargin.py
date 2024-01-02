import xlwings as xw
import pandas as pd
import multiprocessing


def getterDebitAndSetterAvailableMargin(mr, lock):
    with lock:
        try:
            df = pd.read_csv(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\margin\\marginstate\\margin.csv")
            ma = df.loc[0, 'margin']
            df.loc[0, 'margin'] = ma - mr
            df.to_csv(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\margin\\marginstate\\margin.csv",
                index=False)
        except Exception as e:
            print(f"The exception while getter, debit and setter available margin is {e}")
