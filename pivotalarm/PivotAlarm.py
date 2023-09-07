import pandas as pd
import xlwings as xw
from GetSAndR import *
from AngelOneSmartAPIApp.GetAccessToken import *


def pivotAlarm():
    srD = getSRData()
    obj, toc = get_access_token()
    # ltp = obj.ltpData("NSE", "SBIN-EQ", "3045")
    # print("Ltp Data :", ltp['data']['ltp'])
    # srN = srD.drop(["id", "desc", "symbol", "token", "ltp"], axis='columns')
    srN = srD
    srN.insert(5, "bigS", 0)
    srN.insert(13, "bigM", 200000)
    # print(srN.iloc[1])
    alarmItr = 0
    srN.columns = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    for index, rows in srN.iterrows():
        ltp
        for i in range(5, 13):
            print(rows[i])
        break


pivotAlarm()
