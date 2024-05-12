import datetime
from historicdata.GetterSpecificHistoricData import getterSpecificHistoricData
import time


def parsingWithDateTime():
    startTime = time.time()
    # get dummy df
    df = getterSpecificHistoricData("2024-04-16", 10)
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
    df.to_csv('E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\threadresearch\\mat.csv')
    # print(df)
    print(time.time() - startTime)


parsingWithDateTime()
