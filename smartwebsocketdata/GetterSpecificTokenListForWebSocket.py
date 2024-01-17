import pandas as pd


def getterSpecificTokenListForWebSocket(tokenListName="TokenList0"):
    try:
        df = pd.read_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\smartwebsocketdata\\websocketstate\\tokenlist\\{tokenListName}.csv")
        df['0'] = df['0'].astype("str")
        lst = df['0'].tolist()
    except Exception as e:
        print(f"The exception while getterSpecificTokenListForWebSocket is {e}")
        lst = []
    return lst


# print(getterSpecificTokenListForWebSocket())
