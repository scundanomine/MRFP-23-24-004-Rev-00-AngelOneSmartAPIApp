import time

import pandas as pd
import datetime
import xlwings as xw

from commonudm.GetterPastTimeByMin import getterPastTimeByMin
from commonudm.GetterTimeDelta import getterTimeDelta
from marketstructure.GetterMarketStructureDf import getterMarketStructureDf


def displayPastFiveMarketTrend(cv):
    # getter initial past time by min
    dfPt = getterPastTimeByMin()
    pt = dfPt.loc[0, 'time']
    ct = datetime.datetime.now() - cv
    ct = ct.strftime("%Y-%m-%d %H:%M:00")
    if ct != pt:
        time.sleep(2)
        while True:
            try:
                # getting data from the sheet
                wb = xw.Book(
                    "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
                dt = wb.sheets("MAndP")
                df = getterMarketStructureDf()

                dt["A3"].value = df.loc[5, 'mTyp']
                dt["B3"].value = df.loc[6, 'mTyp']
                dt["C3"].value = df.loc[7, 'mTyp']
                dt["D3"].value = df.loc[8, 'mTyp']
                dt["E3"].value = df.loc[9, 'mTyp']
                break
            except Exception as e:
                print(f"The exception while getPositionDisplay is {e}")
        dfPt.loc[0, 'time'] = ct
        dfPt.to_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\commonudm\\resource\\PastTimeByMin.csv",
            index=False)


# cvp = getterTimeDelta()
# displayPastFiveMarketTrend(cvp)
