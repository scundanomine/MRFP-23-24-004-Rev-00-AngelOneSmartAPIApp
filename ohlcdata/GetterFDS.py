import pandas as pd


def getterFDS():
    try:
        df = pd.read_csv(
            "F:\\AT\\ohlcdata\\ohlcstate\\futureohlcdatafile\\fds.csv")
    except Exception as e:
        # print(f"The exception while getterFDS is {e}")
        a = e
        df = getterFDS()
    return df


# print(getterFDS())
