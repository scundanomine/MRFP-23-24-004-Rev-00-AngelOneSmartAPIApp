import pandas as pd
import xlwings as xw
import multiprocessing


def setterPositionList(df=pd.DataFrame(), lock=multiprocessing.Lock()):
    lock.acquire()
    df.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\position\\positionstate\\PositionList.csv",
        index=False)
    lock.release()
