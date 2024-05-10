import pandas as pd


def setterPreExitStrategyFlag():
    # top is time of order placed, po is primary order, sl is stop loss order and to is target order and their values are open, executed, canceled or none.
    # mr is margin required, lp is limit price, q is the quantity, sl is the stop loss
    # gol is gain or loss, tOEP is reference time of entry placed, tOP is time of position taken and tOEx is time of exit
    df = pd.DataFrame([['F', 'F']], columns=['xBF', 'xSF'])
    df.to_csv(
        "F:\\AT\\belliprogressionem\\state\\ExSFlag.csv",
        index=False)
    return df


# setterPreExitStrategyFlag()
