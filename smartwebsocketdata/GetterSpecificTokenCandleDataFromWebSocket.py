import pandas as pd


def getterSpecificTokenCandleDataFromWebSocket(token):
    try:
        gdf = pd.read_csv(
                f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\smartwebsocketdata\\websocketstate\\tokenwisewholecandledata\\{token}.csv")
    except Exception as e:
        print(f"The exception while GetterSpecificTokenCandleDataFromWebSocket is {e}")
        gdf = getterSpecificTokenCandleDataFromWebSocket(token)

    return gdf


# print(getterSpecificTokenCandleDataFromWebSocket(25).to_dict('records')[0])
