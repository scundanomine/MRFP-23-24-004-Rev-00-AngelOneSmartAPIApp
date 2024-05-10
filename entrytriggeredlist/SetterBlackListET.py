import pandas as pd
import multiprocessing


def setterBlackListET(df=pd.DataFrame(), lock=multiprocessing.Lock()):
    lock.acquire()
    df.to_csv("F:\\AT\\entrytriggeredlist\\entrytriggeredstate\\BlackListET.csv", index=False)
    lock.release()
