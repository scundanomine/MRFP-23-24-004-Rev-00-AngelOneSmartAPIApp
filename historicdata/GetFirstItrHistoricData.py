import datetime

from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList
from commonudm.GetterTimeDelta import getterTimeDelta
from eventloop.CreateGSTDataFile import *
from historicdata.GetHistoricDataWithQuery import getHistoricDataWithQuery
from ohlcdata.ProcessPastTenCandlesData import processPastTenCandlesData


def getFirstItrHistoricData():
    print("Process for past 10 candles data started")
    startTime = time.time()
    cv = getterTimeDelta()
    date = datetime.datetime.today() - cv
    date = date.strftime("%Y-%m-%d")
    # getter required symbol and token
    gDf = getterRequiredSymbolAndTokenList()
    currentRefTime = datetime.datetime.now() - cv
    toDateTime = currentRefTime
    fromDateTime = currentRefTime - datetime.timedelta(minutes=10)
    for index, row in gDf.iterrows():
        uid = row['id']
        data = getHistoricDataWithQuery(fromDateTime, toDateTime, uid, date)
        if not data:
            data = [{'0': "", '1': 0, '2': 0, '3': 0, '4': 0, '5': 0}]
        dfT = pd.DataFrame(data)
        processPastTenCandlesData(uid, fromDateTime, dfT)

    print(f"The execution time is {time.time() - startTime}")


# getFirstItrHistoricData()
