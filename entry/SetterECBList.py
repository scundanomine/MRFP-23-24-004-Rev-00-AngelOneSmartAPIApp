import pandas as pd
import multiprocessing


def setterECBList(df=pd.DataFrame(), lock=multiprocessing.Lock()):
    lock.acquire()
    df.to_csv("F:\\AT\\entry\\entrystate\\ECBList.csv", index=False)
    lock.release()

