import pandas as pd
import multiprocessing


def getterSpecificTokenCandleDataFromWebSocket(token, lock=multiprocessing.Lock()):
    try:
        with lock:
            gdf = pd.read_csv(
                f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\smartwebsocketdata\\websocketstate\\tokenwisewholecandledata\\{token}.csv")
    except Exception as e:
        print(f"The exception while GetterSpecificTokenCandleDataFromWebSocket is {e}")
        gdf = pd.read_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\smartwebsocketdata\\websocketstate\\tokenwisewholecandledata\\{token}.csv")

    return gdf


# print(getterSpecificTokenCandleDataFromWebSocket(25))
