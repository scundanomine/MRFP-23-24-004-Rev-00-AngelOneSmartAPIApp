import time
import pandas as pd
from commonudm.GetSymbolAndToken import getSymbolAndToken
from traditionalpivotalarm.GetSAndR import getSRData


def checkTraditionalPivotAlarmsWithoutThreading(niftySize=300):
    startTime = time.time()

    # get token and symbol
    dst = getSymbolAndToken()

    # get sr data and sr list
    varSR = getSRData()
    srLst = varSR.to_dict('records')

    # dcs and dcs list
    dcs = pd.read_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\traditionalpivotalarm\\pivotstate\\LiveCandleData.csv")
    dcsLst = dcs.to_dict('records')

    # define sub function


