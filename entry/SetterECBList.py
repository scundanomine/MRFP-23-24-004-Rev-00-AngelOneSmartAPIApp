import pandas as pd
import multiprocessing


def setterECBList(df=pd.DataFrame(), lock=multiprocessing.Lock()):
    lock.aquire()
    df.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\ECBList.csv", index=False)
    lock.release()

