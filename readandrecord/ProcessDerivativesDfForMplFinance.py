import pandas as pd
import datetime


def processDerivativesDfForMplFinance(df=pd.DataFrame()):
    df = df.loc[:, ['time', 'O', 'H', 'L', 'C', 'V', 'QOne', 'QTwo', 'QQOne', 'QQTwo']]
    dicT = {
        'O': 'Open',
        'H': 'High',
        'L': 'Low',
        'C': 'Close',
        'V': 'Volume'
    }
    df.rename(columns=dicT, inplace=True)
    for index, row in df.iterrows():
        if row['Open'] == 0:
            df = df.drop(index, axis=0)
        else:
            time = row['time']
            time = time[:16]
            time = time.replace('T', ' ')
            refDate = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M")
            df.loc[index, 'time'] = refDate
    df = df.set_index('time')
    return df

# cdf = getterSpecificCandleData(1, "RELIANCE-EQ")
# processDfForMplFinance(cdf)
