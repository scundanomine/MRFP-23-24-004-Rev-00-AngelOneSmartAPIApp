import pandas as pd


def getterFFDS():
    try:
        df = pd.read_csv(
            "F:\\AT\\ohlcdata\\ohlcstate\\futureohlcdatafile\\ffds.csv")
    except Exception as e:
        # print(f"The exception while getter future future ds is {e}")
        a = e
        df = getterFFDS()
    return df


# print(getterFDS())
