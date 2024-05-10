import pandas as pd
import multiprocessing


def setterEntryList(df=pd.DataFrame(), lock=multiprocessing.Lock()):
    lock.acquire()
    df.to_csv("F:\\AT\\entry\\entrystate\\EntryList.csv", index=False)
    lock.release()

