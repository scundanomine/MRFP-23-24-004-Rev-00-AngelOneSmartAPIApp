import datetime

from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList
from commonudm.GetterTimeDelta import getterTimeDelta
from eventloop.CreateGSTDataFile import *
from historicdata.GetHistoricDataWithQuery import getHistoricDataWithQuery
from ohlcdata.ProcessPastTenCandlesData import processPastTenCandlesData


def getFirstItrHistoricData():
    print("Process for past 10GetHistoricDataForSpecificUidWithToAndFromDateTime candles data started")
    startTime = time.time()
    cv = getterTimeDelta()
    date = datetime.datetime.today() - cv
    date = date.strftime("%Y-%m-%d")
    # getter required symbol and token
    gDf = getterRequiredSymbolAndTokenList()
    toDateTime = datetime.datetime.now()
    fromDateTime = toDateTime - datetime.timedelta(minutes=10)
    for index, row in gDf.iterrows():
        uid = row['id']
        data = getHistoricDataWithQuery(fromDateTime, toDateTime, uid, date)
        dfT = pd.DataFrame(data)
        processPastTenCandlesData(uid, fromDateTime, dfT)

    print(f"The execution time is {time.time() - startTime}")


# getFirstItrHistoricData()
