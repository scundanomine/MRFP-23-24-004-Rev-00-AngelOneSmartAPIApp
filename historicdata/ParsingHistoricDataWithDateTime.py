import datetime
import pandas as pd

from historicdata.GetterPreSpecificHistoricData import getterPreSpecificHistoricData
from historicdata.GetterSpecificHistoricData import getterSpecificHistoricData
import time


def parsingHistoricDataWithDateTime(date, uid):
    # get dummy df
    df = getterPreSpecificHistoricData(date, uid)
    df['time'] = df['0']
    for index, row in df.iterrows():
        if row['4'] == 0:
            df = df.drop(index, axis=0)
        else:
            timeX = row['time']
            timeX = timeX[:16]
            timeX = timeX.replace('T', ' ')
            refDate = datetime.datetime.strptime(timeX, "%Y-%m-%d %H:%M")
            df.loc[index, 'time'] = refDate
    df = df.set_index('time')
    df.to_csv(f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\historicdata\\historicdatastate\\{date}\\{uid}.csv")


# parsingHistoricDataWithDateTime("2024-04-15", 1)
