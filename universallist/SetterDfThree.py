import pandas as pd


def setterDfThree():
    dfThree = pd.DataFrame(
        columns=['CC1', 'CC2', 'V', 'atr', 'atrPer', 'g', 's', 't', 'bulRP', 'berRP', 'atrV', 'vs', 'roc', 'rsi',
                 'rsi0', 'rsi1', 'rsi2', 'roc0'])
    dfThree.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\universallist\\liststate\\DfThree.csv",
        index=False)
    return dfThree


# setterDfThree()
