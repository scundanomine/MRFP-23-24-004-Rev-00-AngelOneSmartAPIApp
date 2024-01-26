import datetime
import time
import pandas as pd
from commonudm.GetterExitTime import getterExitTime
from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList
from commonudm.GetterTimeDelta import getterTimeDelta
from ohlcdata.GetterPDS import getterPDS
from smartwebsocketdata.GetterSpecificTokenCandleDataFromWebSocket import getterSpecificTokenCandleDataFromWebSocket
from traditionalpivotalarm.GetterPivotData import getterPivotData
from traditionalpivotalarm.GetterSRData import getterSRData
from traditionalpivotalarm.SetterPivotData import setterPivotData
from traditionalpivotalarm.TraditionalPivotAlarm import traditionalPivotAlarm


def checkTraditionalPivotAlarmsWithoutThreading(isLive=False):
    startTime = time.time()
    if isLive:
        cv = pd.to_timedelta(0)
    else:
        cv = getterTimeDelta()
    exitTime = getterExitTime()
    
    while datetime.datetime.now() - cv < exitTime:
        # get token and symbol
        dst = getterRequiredSymbolAndTokenList()

        # get sr data and sr list
        varSR = getterSRData()

        srLst = varSR.to_dict('records')

        # dcs and dcs list
        if not isLive:
            pds = getterPDS()
            pdsLst = pds.to_dict('records')
        else:
            pdsLst = []

        # getterPivotData
        pivDf = getterPivotData()
        
        dcsLst = pivDf.to_dict('records')

        for index, row in dst.iterrows():
            uid = row['id']
            token = row['token']
            if isLive:
                sdf = getterSpecificTokenCandleDataFromWebSocket(token)
                sdf = sdf.drop(['6', '7'], axis=1)
                recordedData = sdf.to_dict('records')[0]
            else:
                try:
                    recordedData = pdsLst[index]
                except Exception as e:
                    print(f"exception while getting recordedData is {e}")
                    recordedData = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0}
            prevTime, alarmTimer, refT, srType, srValue, nSR, gl = traditionalPivotAlarm(srLst[index], dcsLst[index],
                                                                                         recordedData['4'],
                                                                                         recordedData["0"])
            pivDf.loc[index] = [uid, prevTime, recordedData['4'], alarmTimer, refT, srType, srValue, nSR, gl]
        setterPivotData(pivDf)
        
        print(f"Execution time for Pivot alarm (TPA) is {time.time() - startTime}")
        time.sleep(5)


# checkTraditionalPivotAlarmsWithoutThreading()
