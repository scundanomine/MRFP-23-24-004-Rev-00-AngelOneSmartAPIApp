import pandas as pd


def getterSpecificTokenLivePartlyCandleDataFromWebSocket(token):
    try:
        gdf = pd.read_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\smartwebsocketdata\\websocketstate\\tokenwisepartlycandledata\\{token}.csv")
    except:
        # print(f"The exception while getterSpecificTokenLivePartlyCandleDataFromWebSocket is {e}")
        gdf = getterSpecificTokenLivePartlyCandleDataFromWebSocket(token)
    return gdf


# print(getterSpecificTokenLivePartlyCandleDataFromWebSocket(13).loc[0, '4'])
