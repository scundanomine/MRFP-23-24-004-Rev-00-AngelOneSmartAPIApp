import pandas as pd


def setterPreNiftySL():
    # top is time of order placed, po is primary order, sl is stop loss order and to is target order and their values are open, executed, canceled or none.
    # mr is margin required, lp is limit price, q is the quantity, sl is the stop loss
    # gol is gain or loss, tOEP is reference time of entry placed, tOP is time of position taken and tOEx is time of exit
    df = pd.DataFrame([[0, 0]], columns=['BuySL', 'SellSL'])
    df.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\belliprogressionem\\state\\NiftySL.csv",
        index=False)
    return df


# setterPreNiftySL()
