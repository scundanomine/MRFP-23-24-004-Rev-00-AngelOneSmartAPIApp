import pandas as pd
import xlwings as xw
import multiprocessing


def setterPositionList(df=pd.DataFrame(), lock=multiprocessing.Lock()):
    lock.acquire()
    df.to_csv(
        "F:\\AT\\position\\positionstate\\PositionList.csv",
        index=False)
    lock.release()
