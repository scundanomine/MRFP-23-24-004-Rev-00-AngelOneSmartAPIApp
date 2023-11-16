import pandas as pd


def condenseGSTData(uid, symbol):
    try:
        df = pd.read_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\eventloop\\eventstate\\candlewisedata\\{uid + 1}_{symbol}.csv")

        data = [df['C'][9], df['V'][9], df['atr'][9], df['atrPer'][9],
                f"0:{df['g'][9]}, 1:{df['g'][8]}, 2:{df['g'][7]}",
                f"0:{df['s'][9]}, 1:{df['s'][8]}, 2:{df['s'][7]}",
                f"0:{df['t'][9]}, 1:{df['t'][8]}, 2:{df['t'][7]}",
                f"0:{df['bulRP'][9]}, 1:{df['bulRP'][8]}, 2:{df['bulRP'][7]}",
                f"0:{df['berRP'][9]}, 1:{df['berRP'][8]}, 2:{df['berRP'][7]}",
                df['atrV'][9],
                f"0:{df['vs'][9]}, 1:{df['vs'][8]}, 2:{df['vs'][7]}",
                f"0:{df['roc'][9]}, 1:{df['roc'][8]}, 2:{df['roc'][7]}",
                f"0:{df['rsi'][9]}, 1:{df['rsi'][8]}, 2:{df['rsi'][7]}",
                df['rsi'][9],
                df['rsi'][8],
                df['rsi'][7],
                df['roc'][9]]
    except Exception as e:
        print(f"exception while getting the ul is {e}")
        data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return data
