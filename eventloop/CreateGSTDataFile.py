import pandas as pd
import time


def createGSTDataFile(sid, symbol, data):
    # get df
    sdf = pd.DataFrame(data)

    # making entry for missing rows
    if len(sdf) < 10:
        k = ["", 0, 0, 0, 0, 0]
        for i in range(10 - len(sdf)):
            sdf.loc[len(sdf.index)] = k

    # rename ohlc
    sdf.rename(columns={0: "time", 1: "O", 2: "H", 3: "L", 4: "C", 5: "V"}, inplace=True)

    # add required columns
    new_cols = ['atr', 'g', 's', 't', 'p', 'atrV', 'vs']
    cols_to_add = [col for col in new_cols if col not in sdf.columns]
    sdf.loc[:, cols_to_add] = 0
    sdf["atr"] = 0
    sdf["p"] = "none"

    # create import function
    sdf.to_csv(
        f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\eventloop\\eventstate\\candlewisedata\\{sid}_{symbol}.csv",
        index=False)
