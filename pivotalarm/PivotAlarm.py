import pandas as pd
import xlwings as xw
from GetSAndR import *
from AngelOneSmartAPIApp.GetAccessToken import *
from pivotalarm.GetLtpP import *
import time


def pivotAlarm():
    start_time = time.time()
    srD = getSRData()
    ltpPList = loadLtpP()
    obj, toc = get_access_token()
    exchange = "NSE"
    width = 0.04
    srN = srD
    srN.insert(5, "bigS", 0)
    srN.insert(13, "bigM", 200000)
    alarmItr = 0
    srN.columns = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print("--- %s seconds ---" % (time.time() - start_time))
    for index, rows in srN.iterrows():
        uid = rows[0]
        ltpP = ltpPList["ltp"][uid - 1]
        try:
            ltp = obj.ltpData(exchange, rows[2], str(rows[3]))
            ltpC = ltp['data']['ltp']
        except:
            print(f"failed {rows[1]} uid!!!!!!!!!!!!!! {rows[0]}")
            continue
        for i in range(5, 13):
            dtOne = rows[i] * width / 100
            dtTwo = rows[i + 1] * width / 100
            # print(rows[i])
            diffCOne = rows[i] + dtOne - ltpC
            diffPOne = rows[i] + dtOne - ltpP
            diffCTwo = rows[i + 1] - dtTwo - ltpC
            diffPTwo = rows[i + 1] - dtTwo - ltpP

            # surface area condition
            if (diffCOne < 0 and diffPOne < 0) and (diffCTwo < 0 and diffPTwo < 0):
                continue
            elif (diffCOne < 0 and diffPOne < 0) and (diffCTwo > 0 and diffPTwo > 0):
                break
            else:
                alarmItr = alarmItr + 1
                print(f" {rows[0]}: {rows[1]} boom!!! {alarmItr}")
                break

        # ltpPList.loc[uid-1, "ltp"] = ltpC
        # break
    print("--- %s seconds ---" % (time.time() - start_time))


pivotAlarm()
