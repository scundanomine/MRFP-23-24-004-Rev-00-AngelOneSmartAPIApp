import datetime
import pandas as pd


def processDfForMplFinance(df=pd.DataFrame()):
    df = df.loc[: ['time', 'O', 'H', 'L', 'C', 'V']]
    dicT = {
        'O': 'Open',
        'H': 'High',
        'L': 'Low',
        'C': 'Close',
        'V': 'Volume'
    }
    df.rename(columns=dicT, inplace=True)

# cdf = getterSpecificCandleData(1, )

