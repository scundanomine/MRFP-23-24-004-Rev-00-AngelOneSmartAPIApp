from traditionalpivotalarm.GetSAndR import *
from AngelOneSmartAPIApp.GetAccessToken import *
from pivotalarm.GetLtpP import *
from pivotalarm.SaveSRN import *
import time


def pivotAlarm():
    start_time = time.time()
    ltpPList = loadLtpP()
    obj, toc = get_access_token()
    exchange = "NSE"

    # SR area half width
    width = 0.04

    # for running application to given hours
    realTime = 6

    # alarm expiry in minutes
    alarmExp = 30

    srN = getSRData()
    srN.insert(6, "alrmTimer", 0.00)
    srN.insert(7, "refT", 0.00)
    srN.insert(8, "bigS", 0)
    srN.insert(16, "bigM", 200000)

    srN.columns = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    print("--- %s seconds ---" % (time.time() - start_time))
    x = 10
    # real time loop
    while x > 0:
        alarmItr = 0
        # print(srN)
        # srN = readSRN()
        # nifty 200 SR loop
        for rows in srN:
            uid = rows[0]
            if rows[5] > 0:
                srN.loc[uid - 1, 5] = alarmExp * 60 - ((time.time() - start_time) - rows[6])
                continue
            else:
                srN.loc[uid - 1, 5] = 0

            ltpP = ltpPList["ltp"][uid - 1]
            try:
                ltp = obj.ltpData(exchange, rows[2], str(rows[4]))
                ltpC = ltp['data']['ltp']
            except:
                print(f"failed {rows[1]} uid!!!!!!!!!!!!!! {rows[0]}")
                continue
            for i in range(7, 15):
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
                    srN.loc[uid - 1, 5] = alarmExp * 60
                    srN.loc[uid - 1, 6] = (time.time() - start_time)
                    break

            # ltpPList.loc[uid-1, "ltp"] = ltpC
        # loadRFT(srN[[5, 6]])
        saveSRN(srN)
        print("--- %s seconds ---" % (time.time() - start_time))
        x = x - 1


pivotAlarm()
