import pandas as pd

from candlestickdata.GetterSpecificCandleData import getterSpecificCandleData


def condenseGSTData(uid, symbol):
    try:
        df = getterSpecificCandleData(uid, symbol)
        data = [df['C'][8], df['C'][9], df['V'][9], df['atr'][9], df['atrPer'][9],
                df['g'][9],
                f"{df['s'][9]}, {df['s'][8]}, {df['s'][7]}",
                f"{df['t'][9]}, {df['t'][8]}",
                df['bulRP'][8],
                df['berRP'][8],
                df['atrV'][9],
                f"{df['vs'][9]}, {df['vs'][8]}, {df['vs'][7]}",
                f"{df['roc'][9]}, {df['roc'][8]}, {df['roc'][7]}",
                f"{df['rsi'][9]}, {df['rsi'][8]}, {df['rsi'][7]}",
                df['rsi'][9],
                df['rsi'][8],
                df['rsi'][7],
                df['roc'][9],
                f"{df['bulRP'][9]}, {df['bulRP'][8]}",
                f"{df['berRP'][9]}, {df['berRP'][8]}"]
    except Exception as e:
        print(f"exception while getting the ul is {e}")
        data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return data
