import pandas as pd

from commonudm.GetterStockQtn import getterStockQtn


def setterDfThree():
    n = getterStockQtn()
    dfThree = pd.DataFrame(
        columns=['CC1', 'CC2', 'V', 'atr', 'atrPer', 'g', 's', 't', 'bulRP', 'berRP', 'atrV', 'vs', 'roc', 'rsi',
                 'rsi0', 'rsi1', 'rsi2', 'roc0', 'bulRPC', 'berRPC'], index=list(range(n)))
    dfThree[:] = 0
    dfThree['g'] = "none"
    dfThree['s'] = "none"
    dfThree['t'] = "none"
    dfThree['vs'] = "none"
    dfThree['rsi'] = 50
    dfThree['bulRP'] = "none"
    dfThree['berRP'] = "none"
    dfThree['rsi0'] = 50
    dfThree['rsi1'] = 50
    dfThree['rsi2'] = 50
    dfThree['bulRPC'] = "none"
    dfThree['berRPC'] = "none"
    dfThree.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\universallist\\liststate\\DfThree.csv",
        index=False)
    return dfThree


# print(setterDfThree())
