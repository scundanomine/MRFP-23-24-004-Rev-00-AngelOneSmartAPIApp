import pandas as pd


def setterDfOneForPastThirtyCandles():
    df = pd.DataFrame(
        columns=['time', 'O', 'H', 'L', 'C', 'V', 'atr', 'atrPer', 'g', 's', 't', 'bulRP', 'berRP', 'atrV', 'vs', 'roc',
                 'um', 'dm', 'rsi'], index=list(range(19)))
    df[:] = 0
    dfTwo = pd.DataFrame(
        columns=['time', 'O', 'H', 'L', 'C', 'V', 'atr', 'atrPer', 'g', 's', 't', 'bulRP', 'berRP', 'atrV', 'vs', 'roc',
                 'um', 'dm', 'rsi'], index=[0])
    dfTwo[:] = 0
    df.to_csv(
        'E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\pastthirtycandles\\pastthirycandlesstate\\dfOne.csv',
        index=False)
    dfTwo.to_csv(
        'E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\pastthirtycandles\\pastthirycandlesstate\\dfTwo.csv',
        index=False)


# setterDfOneForPastThirtyCandles()
