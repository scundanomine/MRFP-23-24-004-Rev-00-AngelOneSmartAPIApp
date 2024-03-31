import pandas as pd


def getterSpecificTokenLivePartlyCandleDataFromWebSocket(token):
    try:
        gdf = pd.read_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\ETLAFlag.csv")
    except Exception as e:
        print(f"The exception while GetterSpecificTokenLivePartlyCandleDataFromWebSocket is {e}")
        gdf = getterSpecificTokenLivePartlyCandleDataFromWebSocket(token)
    return gdf


# print(getterSpecificTokenCandleDataFromWebSocket(25))
