import pandas as pd
import multiprocessing


def setterEntryTriggeredList(df=pd.DataFrame(), lock=multiprocessing.Lock()):
    lock.acquire()
    df.to_csv("F:\\AT\\entrytriggeredlist\\entrytriggeredstate\\EntryTriggeredList.csv", index=False)
    lock.release()

