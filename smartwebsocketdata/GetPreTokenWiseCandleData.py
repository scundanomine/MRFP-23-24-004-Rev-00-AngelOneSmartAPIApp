import pandas as pd
from commonudm.GetSymbolAndToken import getSymbolAndToken
import time


def getPreTokenWiseCandleData(n=500):
    startTime = time.time()
    # getter symbol and token
    df = getSymbolAndToken()
    tokList = df['token'].tolist()
    for i in range(n):
        token = tokList[i]
        tdf = pd.DataFrame(columns=list(range(8)), index=[0])
        tdf[:] = 0
        tdf.to_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\smartwebsocketdata\\websocketstate\\tokenwisepartlycandledata\\{token}.csv",
            index=False)
    print(f"Execution time is {time.time() - startTime}")


# getPreTokenWiseCandleData(120)
