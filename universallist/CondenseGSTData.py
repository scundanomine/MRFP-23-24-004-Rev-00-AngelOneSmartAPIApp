import pandas as pd


def condenseGSTData(uid, symbol, lock):
    try:
        lock.acquire()
        df = pd.read_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\eventloop\\eventstate\\candlewisedata\\{uid}_{symbol}.csv")
        lock.release()
        data = [df['C'][8], df['C'][9], df['V'][9], df['atr'][9], df['atrPer'][9],
                f"{df['g'][9]}, {df['g'][8]}, {df['g'][7]}",
                f"{df['s'][9]}, {df['s'][8]}, {df['s'][7]}",
                f"{df['t'][9]}, {df['t'][8]}, {df['t'][7]}",
                f"{df['bulRP'][8]}, {df['bulRP'][7]}",
                f"{df['berRP'][8]}, {df['berRP'][7]}",
                df['atrV'][9],
                f"{df['vs'][9]}, {df['vs'][8]}, {df['vs'][7]}",
                f"{df['roc'][9]}, {df['roc'][8]}, {df['roc'][7]}",
                f"{df['rsi'][9]}, {df['rsi'][8]}, {df['rsi'][7]}",
                df['rsi'][9],
                df['rsi'][8],
                df['rsi'][7],
                df['roc'][9]]
    except Exception as e:
        print(f"exception while getting the ul is {e}")
        data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return data
