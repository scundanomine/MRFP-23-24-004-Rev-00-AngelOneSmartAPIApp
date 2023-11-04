import time


def traditionalPivotAlarm(srVar, dsVar, ltpC):
    # start_time = time.time()

    # SR area half width
    width = 0.04

    # alarm expiry in minutes
    alarmExp = 30

    alarmTimer = dsVar['alarmTimer']
    ltpP = dsVar["C"]
    refT = dsVar['refT']
    srType = dsVar["srT"]
    srValue = dsVar["srValue"]

    # condition for alarm timer and ltp data
    if alarmTimer > 0:
        alarmTimer = alarmExp * 60 - (time.time() - refT)
    # condition for no value
    elif ltpC == 0:
        pass
    # condition for checking pivot alarm
    else:
        alarmTimer = 0
        for i in range(1, 14):
            dtOne = srVar[i] * width / 100
            dtTwo = srVar[i + 1] * width / 100
            # print(srVar[i])
            diffCOne = srVar[i] + dtOne - ltpC
            diffPOne = srVar[i] + dtOne - ltpP
            diffCTwo = srVar[i + 1] - dtTwo - ltpC
            diffPTwo = srVar[i + 1] - dtTwo - ltpP

            # surface area condition
            if (diffCOne < 0 and diffPOne < 0) and (diffCTwo < 0 and diffPTwo < 0):
                continue
            elif (diffCOne < 0 and diffPOne < 0) and (diffCTwo > 0 and diffPTwo > 0):
                break
            else:
                alarmItr = alarmItr + 1
                print(f" {srVar[0]}: {srVar[1]} boom!!! {alarmItr}")
                srN.loc[uid - 1, 5] = alarmExp * 60
                srN.loc[uid - 1, 6] = (time.time() - start_time)
                break

    return alarmTimer, refT, srType, srValue
