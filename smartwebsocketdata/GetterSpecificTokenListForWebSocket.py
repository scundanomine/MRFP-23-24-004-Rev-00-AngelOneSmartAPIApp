import pandas as pd


def getterSpecificTokenListForWebSocket(tokenListName="TokenList0"):
    try:
        df = pd.read_csv(
            f"F:\\AT\\smartwebsocketdata\\websocketstate\\tokenlist\\{tokenListName}.csv")
        df['0'] = df['0'].astype("str")
        lst = df['0'].tolist()
    except Exception as e:
        print(f"The exception while getterSpecificTokenListForWebSocket is {e}")
        lst = []
    return lst


# print(getterSpecificTokenListForWebSocket())
