import pandas as pd
from commonudm.GetSymbolAndToken import getSymbolAndToken
import time


def getPreTokenWiseCandleData(sourceFolder, n=120):
    startTime = time.time()
    # getter symbol and token
    df = getSymbolAndToken()
    tokList = df['token'].tolist()
    for i in range(n):
        token = tokList[i]
        tdf = pd.DataFrame(columns=list(range(8)), index=[0])
        tdf[:] = 0
        tdf.to_csv(
            f"F:\\AT\\smartwebsocketdata\\websocketstate\\{sourceFolder}\\{token}.csv",
            index=False)
    print(f"Execution time is {time.time() - startTime}")


# getPreTokenWiseCandleData(120)
